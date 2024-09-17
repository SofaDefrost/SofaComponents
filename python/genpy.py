"""
A sofa scene to autogenerate the python wrapping function from the runtime informations.

"""

# -*- coding: utf-8 -*-
import re
import sys, os
import Sofa
from pathlib import Path

# from sphinx import make_mode
reserved = ["in", "with", "for", "if", "def", "class", "global"]

def sofa_to_python_typename(name, short=False):
    t = {"string":"str",
         "bool": "bool",
         "TagSet" : "object",
         "BoundingBox" : "object",
         "ComponentState" : "object",
         "RGBAColor" : "object",
         "OptionsGroup" : "object",
         "Material" : "object",
         "DisplayFlags" : "object",
         "d" : "float",
         "f" : "float",
         "i" : "int",
         "I" : "int",
         }

    SofaArray = "SofaArray"
    if short:
        SofaArray = "SofaArray"

    if name in t:
        return t[name]
    elif "Rigid" in name:
        return SofaArray
    elif "vector" in name:
        return SofaArray
    elif "set" in name:
        return SofaArray
    elif "Vec" in name:
        return SofaArray
    elif "Quat" in name:
        return SofaArray
    elif "map" in name:
        return "object"
    elif "fixed_array" in name:
        return SofaArray
    raise Exception("Missing type name,... ", name)


def sofa_datafields_to_constructor_arguments_list(data_fields, object_name, has_template=True):
    required_data_fields = []
    optional_data_fields = []

    for data_field in data_fields:
        if data_field.getName() in reserved:
            print("Warning: " + object_name + " contains a Data field which name is python keyword")
            continue

        if " " in data_field.getName():
            print("Warning: this is an invalid arguments name: '" + repr(data_field.getName()) + "'")
            continue

        if len(data_field.getName()) != 0:
            if data_field.isRequired():
                required_data_fields.append(data_field)
            else:
                optional_data_fields.append(data_field)

    result_params = ""
    if has_template:
        result_params = "template: Optional[str] = None, "
    result_params += ",".join([data.getName()+": "+sofa_to_python_typename(data.getValueTypeString()) for data in required_data_fields])
    result_params += ",".join([data.getName()+": Optional["+sofa_to_python_typename(data.getValueTypeString())+"] = None" for data in optional_data_fields])

    ordered_fields = sorted(data_fields, key=lambda x: x.getName())

    all = "\n           ".join( [ data.getName()+" ("+sofa_to_python_typename(data.getValueTypeString(), short=True)+"):   " + data.getHelp() for data in ordered_fields])
    all += "\n           template (str): the type of degree of freedom"
    return result_params, all

def sofa_datafields_to_doc(data_fields):
    p = ""
    for data_field in data_fields:
        if len(data_field.getName()) == 0:
            continue
        if " " in data_field.getName():
            continue

        if data_field.getName() in reserved:
            p += "\t\t " + data_field.getName() + ": " + str(
                data_field.getHelp()) + " (NB: use the kwargs syntax as name is a reserved word in python)\n\n"
        else:
            p += "\t\t " + data_field.getName() + ": " + str(data_field.getHelp()) + "\n\n"

    return p

def clean_sofa_text(t):
    t = t.replace("\n","")
    t = t.replace("'", "")
    return t

def sofa_datafields_to_typehints(data_fields, mode="Sofa"):
    p = ""
    p2 = ""
    for data_field in data_fields:
        if len(data_field.getName()) == 0:
            continue

        if " " in data_field.getName():
            continue

        if data_field.getName() in reserved:
            p += "    " + data_field.getName() + ": " + str(
                data_field.getHelp()) + " (NB: use the kwargs syntax as name is a reserved word in python)\n\n"
        else:
            p += f"    {data_field.getName()}: Data[{sofa_to_python_typename(data_field.getValueTypeString())}] \n    '{clean_sofa_text(data_field.getHelp())}'\n\n"
            p2 += f"        {data_field.getName()}: Optional[{sofa_to_python_typename(data_field.getValueTypeString())} | LinkPath] = None \n        '{clean_sofa_text(data_field.getHelp())}'\n\n"

    return p, p2

def makeInitFile(rootDir):
    entries = {}
    for dirpath, dirnames, filenames in os.walk(rootDir):
        initfile = open(dirpath + "/__init__.py", "wt")
        res = []
        fres = []
        fres2 = []
        for d in dirnames:
            res.append(d)
        for f in filenames:
            if f.endswith(".py") and f != "__init__.py":
                fres.append(f[:-3])
                res.append(f[:-3])
        listc = ""
        for r in res:
            listc += "    " + str(r) + "\n"

        initfile.write("# -*- coding: utf-8 -*-\n\n")
        initfile.write("""
\"\"\"
Sofa Component %s 

Summary:
========

%s
    
\"\"\"  
""" % (os.path.basename(dirpath), listc))
        
        #initfile.write("__all__=" + repr(fres) + "\n")
        #for r in fres:
        #    initfile.write(f"from {r} import {r}\n")
        #initfile.close()

        print(str((dirpath, dirnames, filenames)))


def wrapper_code(class_name, description, data_list, properties_doc, 
                 class_typehints, params_typehints, 
                 constructor_params_typehints,
                 constructor_params_docs):
    properties_doc = ""
    return f"""    
class {class_name}(Object):
    \"\"\"{description}\"\"\"

    def __init__(self, {constructor_params_typehints}):
        \"\"\"{description}
        
        Args:
           {constructor_params_docs}
        \"\"\"
        ...

{class_typehints}

    @dataclasses.dataclass
    class Parameters:
        \"\"\"Parameter for the construction of the {class_name} component\"\"\"

{params_typehints} 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return {class_name}.Parameters()
"""

def documentation_code(class_name):
    return """
import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
\"\"\"
Component %s

.. autofunction:: %s

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
\"\"\"
""" % (class_name, class_name)


def create_mechanical_object_from_templates(templates, root_node):
    templates = templates.split(',')
    if len(templates) == 0:
        return root_node
    if len(templates) == 1:
        root_node.addObject("MechanicalObject", template=templates[0], name='MO<' + templates[0] + '>')
        return root_node
    if len(templates) >= 2:        
        child1 = root_node.addChild("child1")        
        root_node.addObject("MechanicalObject", template=templates[0], name='MO<' + templates[0] + '>')
        child1.addObject("MechanicalObject", template=templates[1], name='M1<' + templates[1] + '>')
        return child1 
    raise Exception("Broken code "+str(templates))


def select_single_template(default_template, template_list):
    if default_template:
        return default_template
    for dim in ["Vec3", "Rigid3", "Vec2", "Rigid2", "Vec1", "Quatd"]:
        for template in template_list:
            if "Cuda" not in template and dim in template:
                return template

    for template in template_list:
        return template

    return ""


def create_typhint(pathname):
    from pathlib import Path
    path = Path(pathname).parent
    if not os.path.exists(str(path)):
        path.mkdir(parents=True)
    c="""
from typing import TypeVar, Generic, Optional as __optional__
import numpy.typing
from Sofa.Core import Node, Object, LinkPath
import numpy
from numpy.typing import ArrayLike

T = TypeVar("T", bound=object)

# This is a generic type 'T' implemented without PEP 695 (as it needs python 3.12)
class Data(Generic[T]):
    linkpath: LinkPath
    value: T

Optional = __optional__
SofaArray = numpy.ndarray | list
"""
    with open(pathname,"w") as w:
        w.write(c)

def create_sphinxdoc(code_model : dict, destination : str):
    """Generates the sphinx documentation for the corresponding code_model"""

    # for each entry in the code, 
    for component_qualified_name, entry in code_model.items():

        if entry["category"] == "class":
            context = entry["context"]
            name = entry["name"]
            description = entry["description"]

            attributes = "\n".join([f" - {a['name']} : {a['description']}" for a in entry["datafields"] ]) 
            links = "\n".join([f" - {a['name']} : {a['description']}" for a in entry["links"] ]) 

            context_path = context.replace(".","/")
            destination_pathname = Path(destination, context_path)
            if not os.path.exists(destination_pathname):
                destination_pathname.mkdir(parents=True)

            component_pathname = os.path.join(destination_pathname, name+".rst")
            outfile = open(component_pathname, "wt")
            qname = context+"."+name
            outfile.write(f"""{name}
{"-"*len(name)}

Context: {context}

{description}

Data:
{attributes}

Links:
{links}
""")
            print(f"Writing doc entry at: {destination_pathname}/ for {name}.rst")
        else:
            context = entry["context"]
            name = entry["name"]
            description = entry["description"]
            depth = entry["depth"]

            d = ["#", "*", "=", "-", "^", "=", "="]
            s = d[depth]
            
            content_modules = "\n".join([ f"   {a['name']}/index" for a in entry["content"].values() if a["type"] == "module" ])
            content_class = "\n".join([ f"   {a['name']}" for a in entry["content"].values() if a["type"] != "module" ])

            context_path = context.replace(".","/")
            destination_pathname = Path(destination, context_path, name)
            if not os.path.exists(destination_pathname):
                destination_pathname.mkdir(parents=True)

            component_pathname = os.path.join(destination_pathname, "index.rst")
            outfile = open(component_pathname, "wt")
            qname = context+"."+name
            outfile.write(f"""{name}
{s*len(name)}

.. toctree::
   :maxdepth: 4

{content_modules}
{content_class}

""")
            print(f"Writing doc module at: {destination_pathname}/ for {name}.rst")
                                      

def create_stubs():
    blacklist = ["RequiredPlugin"]

    template_nodes = dict()
    not_created_objects = list()

    target_path = "out/"

    create_typhint(target_path + "Sofa/Component/TypeHints.py")

    code_model = {}

    for entry in Sofa.Core.ObjectFactory.components:

        args = {}
        if entry.className not in blacklist:
            # entry_templates = entry.templates
            entry_templates = ['']
            if len(entry.templates) > 0:
                entry_templates = [select_single_template(entry.defaultTemplate, entry.templates)]

            for entry_template in entry_templates:
                target = "unknown_target"
                object_name = entry.className + "<" + entry_template + ">"
                if object_name not in blacklist and entry.className not in blacklist:
                    try:
                        print("### Processing: " + object_name)
                        tmpnode = Sofa.Core.Node("tmpnode")
                        node = create_mechanical_object_from_templates(entry_template, tmpnode)
                        print("node: ", [n.name.value for n in node.objects])
                        if len(entry_template) == 0:
                            obj = node.addObject(entry.className, name=entry.className)
                        else:
                            obj = node.addObject(entry.className, template=entry_template, name=entry.className)
                        args = obj.getDataFields()
                        links = obj.getLinks()
                        target = obj.getTarget()
                        obj.getContext().removeObject(obj)
                    except Exception as e:
                        not_created_objects.append(object_name)
                        print("Unable to get DOC: " + str(e))
                        continue

                    if not target:
                        target = "unknown_target"

                    arguments_list, constructor_params_doc = sofa_datafields_to_constructor_arguments_list(args, object_name, len(entry.templates) > 0)
                    params_doc = sofa_datafields_to_doc(args)
                    class_typehint, params_typehint = sofa_datafields_to_typehints(args)
                    code = wrapper_code(entry.className, entry.description.strip(), arguments_list, params_doc, 
                                        class_typehint, params_typehint, 
                                        arguments_list, constructor_params_doc)

                    pathname = target_path + target.replace(".","/") + "/"
                    full_component_name = target + "." + entry.className

                    from pathlib import Path
                    path = Path(pathname)
                    if not os.path.exists(pathname):
                        path.mkdir(parents=True)

                    outfile = open(pathname + entry.className + ".py", "wt")
                    outfile.write("# -*- coding: utf-8 -*-\n\n")
                    outfile.write(documentation_code(entry.className))
                    outfile.write(code)
                    outfile.close()

                    if full_component_name in code_model:
                        raise Exception("Already existing entry")

                    code_model[full_component_name] = {
                        "context" : target,
                        "name" : entry.className,
                        "category" : "class",
                        
                        "description" : entry.description.strip(),
                        "links" :  [{"name": a.getName(),
                                         "type" : a.getValueTypeString(),
                                         "description": clean_sofa_text(a.getHelp()) } for a in links],
                        "datafields" : [{"name": a.getName(),
                                         "type" : clean_sofa_text(a.getValueTypeString()),
                                         "description": a.getHelp() } for a in args],
                        "examples" : []
                    }


                    def fill_context_model(context_model, target, name,type):
                        if len(target) <= 1:
                            return code_model
                        
                        target_name = ".".join(target)
                        parent_context = target[:-1]
                        current_context = target[-1]
                        if target_name not in code_model:
                            code_model[target_name] = {
                                "context" : ".".join(parent_context),
                                "name" : current_context,
                                "category" : "module",
                                "description" : "",
                                "content" : {},
                                "depth" : len(parent_context)
                            }
                        
                        if name not in code_model[target_name]["content"]:
                            code_model[target_name]["content"][name] = {"name":name, "type":type}  

                        fill_context_model(code_model, parent_context, current_context, "module")

                        return code_model
                    
                    fill_context_model(code_model, target.split("."), entry.className, "class")


    makeInitFile(target_path+"/Sofa")
    print("\n\n\nPROCESSING DONE")
    # make_mode.run_make_mode(sys.argv[2:])

    print('\n\n\nObjects that could not be created:')
    print(not_created_objects)
    return code_model

if __name__ == "__main__":
    print("Generating Sofa.Components stubs...")
    code_model = create_stubs()
    create_sphinxdoc(code_model, "../docs/sphinx/source/content/modules")
