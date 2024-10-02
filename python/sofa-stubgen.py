import logging 
import importlib
import logging
import re
import Sofa

from argparse import ArgumentParser, Namespace
from pathlib import Path

import types 
import pybind11_stubgen 
import pybind11_stubgen.parser.interface as interface 
import pybind11_stubgen.parser.mixins.fix as fix
import pybind11_stubgen.parser.mixins.parse as parse
from pybind11_stubgen.structs import (
    Module, QualifiedName, Class, Identifier, Docstring, Field, Attribute, 
    Modifier, Annotation, Value, Import, Method, Function)

import genpy
from genpy import load_component_list, select_single_template, sofa_datafields_to_typehints


def parse_sofa_component_module(module, sofa_factory_id):
    print("Factory parsing ", sofa_factory_id)
    
    sofa_component = Module(Identifier("Sofa"))
    sofa_component.sub_modules.append( Module(Identifier("Component")) ) 
    sofa_component.sub_modules[-1].sub_modules.append( Module(Identifier("Component")) )

    return sofa_component

def get_or_create_module_for_target(module : Module, sofa_target : list[str]):    
    for target in sofa_target:
        if module.name == target:
            continue

        smodule = [x for x in module.sub_modules if getattr(x, "name") == target ]
        if len(smodule) == 0:
            smodule = [Module(Identifier(target))]
            module.sub_modules.append(smodule[0]) 

            smodule[0].imports.add(Import(Identifier("typing"), QualifiedName([Identifier("typing")])))
            smodule[0].imports.add(Import(Identifier("TypeHints"), QualifiedName([Identifier("Sofa.TypeHints")])))
            smodule[0].imports.add(Import(Identifier("Sofa"), QualifiedName([Identifier("Sofa")])))

        module = smodule[0]
    
    # At this point we have a valid module, ready to old the class
    return module

def get_attribute_value(data) -> str:
    name = data["name"]
    if isinstance(data["type"], list):
        type = "| ".join([genpy.sofa_to_python_typename(x) for x in data["type"]])
    else:
        type = genpy.sofa_to_python_typename(data["type"])    

    if len(name) == 0:
        return ""

    if " " in name:
        return ""

    if name in genpy.reserved:
        return "# help (NB: use the kwargs syntax as name is a reserved word in python)"
    
    return f"TypeHints.Data[{type}]"

def add_sofa_data_to_class(cclass: Class, datum : list):
    for data in datum:
        pygen_data = [x for x in cclass.fields if getattr(x.attribute, "name") == data["name"] ]
    
        if len(pygen_data) == 0:
            help = genpy.clean_sofa_text(data["help"])
            a = Value(get_attribute_value(data))
            pygen_data = Field( Attribute( Identifier(data["name"]), annotation=a, value=None, doc=Docstring(help)), modifier=None)
            cclass.fields.append(pygen_data)
        else:
            pygen_data = pygen_data[0]    

def add_sofa_component_to_module(module, component):
    component_class_name = component["className"]
    entry_templates = [n for n in component["creator"].keys()]
    component_description = component["description"]
        
    selected_template = select_single_template(entry_templates)
    selected_entry = component["creator"][selected_template]
    selected_class = selected_entry["class"]
    selected_object = selected_entry["object"]
    selected_target = selected_entry["target"]
    datum = selected_object["data"]   
    links = selected_object["link"]
        
    component_class = [x for x in module.classes if getattr(x, "name") == component_class_name ]
    if len(component_class) == 0:
        component_class = Class(Identifier(component_class_name),
                                     Docstring(component_description),
                                     [QualifiedName("Sofa.Core.Object".split("."))])
        module.classes.append(component_class)
    else:
        component_class = component_class[0]

    if not component_class.doc:
        component_class.doc = Docstring(component_description)
    add_sofa_data_to_class(component_class, datum)

    ### Add the parameters for easy construction. 
    component_parameter_class = Class(Identifier("Parameters"))
    component_class.classes.append(component_parameter_class)
    add_sofa_data_to_class(component_parameter_class, datum)
    
    component_class.methods.append(
        Method(
            Function(
                Identifier("new_parameter"),
                doc=Docstring("get parameters for a new object"), 
                returns=Value(component_class_name+".Parameters")
            ), 
            modifier="static")
        )
    print("Writing Sofa component... ", component_class_name)
    
def add_sofa_components_to_module(module, sofa_components):    
    for component in sofa_components:
        component_class_name = component["className"]
        entry_templates = [n for n in component["creator"].keys()]
        description = component["description"]
        
        selected_template = select_single_template(entry_templates)
        selected_entry = component["creator"][selected_template]
        selected_class = selected_entry["class"]
        selected_object = selected_entry["object"]
        component_target = selected_entry["target"]
        print("Processing: ", component_class_name, component_target)
        dest_module = get_or_create_module_for_target(module, component_target.split("."))
        add_sofa_component_to_module(dest_module, component)

    return module

cmdline_parser: ArgumentParser 

import pybind11_stubgen.printer
original_run = pybind11_stubgen.run 
def run(
    parser, 
    printer,
    module_name,
    out_dir,
    sub_dir,
    dry_run,
    writer):

    module = parser.handle_module(
        QualifiedName.from_str(module_name), importlib.import_module(module_name)
    )

    args = cmdline_parser.parse_args()
    
    sofa_components = load_component_list(args.sofa_preload_with)
    module = add_sofa_components_to_module(module, sofa_components)
    parser.finalize()

    if module is None:
        raise RuntimeError(f"Can't parse {module_name}")

    if dry_run:
        return

    #def print_value(attr):
    #    return attr.repr
    #printer.print_value = print_value


    def indent_lines(lines: list[str], by=4) -> list[str]:
        print("LINE IS ", lines)
        return [" " * by + line for line in lines]
    printer.indent_lines = indent_lines

    out_dir.mkdir(exist_ok=True, parents=True)
    writer.write_module(module, printer, to=out_dir, sub_dir=sub_dir)

old_arg_parse = pybind11_stubgen.arg_parser
def sofagen_arg_parse():
    global cmdline_parser
    cmdline_parser = old_arg_parse()
    cmdline_parser.add_argument(
        "--sofa-preload-with",
        help="The Sofa plugin with wich the factory is loaded & filtered with",
        default="Sofa.Component",
    )
    return cmdline_parser
pybind11_stubgen.arg_parser = sofagen_arg_parse


# Monkey patching main stub_parser_from_args so it includes Sofa Hook 
pybind11_stubgen.run = run
pybind11_stubgen.main()

