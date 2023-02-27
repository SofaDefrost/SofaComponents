"""
A sofa scene to autogenerate the python wrapping function from the runtime informations.

"""

# -*- coding: utf-8 -*-
import re
import sys, os
import Sofa

# from sphinx import make_mode
reserved = ["in", "with", "for", "if", "def", "class", "global"]


def sofa_datafields_to_constructor_arguments_list(data_fields, object_name):
    result_params = ""
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

    for data_field in required_data_fields:
        result_params += ", " + data_field.getName()

    for data_field in optional_data_fields:
        try:
            result_params += ", " + data_field.getName() + "=" + repr(data_field.value)
        except Exception as e:
            print("sofa_datafields_to_constructor_arguments_list error: " + str(data_field) + "\n" + str(e))
            pass

    return result_params


def sofa_datafields_to_constructor_usage(data_fields):
    p = ""
    for data_field in data_fields:
        if data_field.getName() in reserved:
            continue

        if " " in data_field.getName():
            continue

        if len(data_field.getName()) != 0:
            p += ", " + data_field.getName() + "=" + str(data_field.getName())
    return p


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


def makeInitFile(rootDir):
    entries = {}
    for dirpath, dirnames, filenames in os.walk(rootDir):
        initfile = open(dirpath + "/__init__.py", "wt")
        res = []
        for d in dirnames:
            res.append(d)
        for f in filenames:
            if f.endswith(".py") and f != "__init__.py":
                res.append(f[:-3])
        listc = ""
        for r in res:
            listc += "    " + str(r) + "\n\n"

        initfile.write("# -*- coding: utf-8 -*-\n\n")
        initfile.write("""
\"\"\"
Module %s 

Content of the module
**********************

Summary:
========
.. autosummary::
     :toctree: _autosummary

%s

Content:
========

.. automodule::

%s
    
Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
\"\"\"  
""" % (os.path.basename(dirpath), listc, listc))
        initfile.write("__all__=" + repr(res) + "\n")
        for r in res:
            initfile.write("import " + str(r) + "\n")
        initfile.close()

        print(str((dirpath, dirnames, filenames)))


def wrapper_code(class_name, params, description, paramsmd, params2):
    return """
        
def %s(attachedTo %s, **kwargs):
    \"\"\"%s

    Args:

%s
    \"\"\"
    return attachedTo.createObject(\"%s\" %s, **kwargs)
""" % (class_name, params, description, paramsmd, class_name, params2)


def documentation_code(class_name):
    return """
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


def create_mechanical_object_from_templates(templates, template_nodes, root_node):
    if templates:
        all_templates = templates.split(',')
        check = all(
            item in Sofa.Core.ObjectFactory.getComponent('MechanicalObject').templates for item in all_templates)
        if check:
            if templates not in template_nodes:
                if len(all_templates) == 1:
                    node = root_node.addChild(templates)
                    print('Create MechanicalObject ' + templates + ' in root node')
                    node.addObject("MechanicalObject", template=templates, name='MO<' + templates + '>')
                    template_nodes[templates] = node
                    return node
                else:
                    parent = create_mechanical_object_from_templates(','.join(all_templates[:-1]), template_nodes, root_node)
                    if parent:
                        node = parent.addChild(all_templates[-1])
                        print('Create MechanicalObject ' + templates + ' in ' + node.getPathName())
                        node.addObject("MechanicalObject", template=all_templates[-1], name='MO<' + templates + '>')
                        template_nodes[templates] = node
                        return node
                    else:
                        print('problem')
                        return None
            else:
                return template_nodes[templates]
    return None


def select_single_template(default_template, template_list):
    if default_template:
        return default_template
    for dim in ["Vec3", "Rigid3", "Vec2", "Rigid2", "Vec1"]:
        for template in template_list:
            if "Cuda" not in template and dim in template:
                return template

    for template in template_list:
        return template

    return ""


def createScene(root_node):
    sys.argv = ['./mysphinx.py', '-M', 'html', 'source', 'build']
    blacklist = ["PythonMainScriptController",
                 "CapsuleCollisionModel",
                 "FileMessageHandlerComponent",
                 "MouseInteractor"
                 ]
    root_node.addObject("MechanicalObject")
    template_nodes = dict()

    not_created_objects = list()

    target_path = "sofacomponents/"
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
                        node = create_mechanical_object_from_templates(entry_template, template_nodes, root_node)

                        creation_node = node
                        if not creation_node:
                            creation_node = root_node

                        obj = creation_node.addObject(entry.className, template=entry_template, name=entry.className)
                        args = obj.getDataFields()
                        target = obj.getTarget()
                        obj.getContext().removeObject(obj)
                    except Exception as e:
                        not_created_objects.append(object_name)
                        print("Unable to get DOC:\n" + str(e))
                        continue

                    if not target:
                        target = "unknown_target"

                    arguments_list = sofa_datafields_to_constructor_arguments_list(args, object_name)
                    constructor_usage = sofa_datafields_to_constructor_usage(args)
                    paramsmd = sofa_datafields_to_doc(args)
                    code = wrapper_code(entry.className, arguments_list, entry.description, paramsmd, constructor_usage)

                    if not os.path.exists(target_path):
                        os.mkdir(target_path)

                    pathname = target_path + target + "/"
                    if not os.path.exists(pathname):
                        os.mkdir(pathname)
                    outfile = open(pathname + entry.className + ".py", "wt")
                    outfile.write("# -*- coding: utf-8 -*-\n\n")
                    outfile.write(documentation_code(entry.className))

                    outfile.write(code)

                    outfile.close()

    makeInitFile(target_path)
    print("\n\n\nPROCESSING DONE")
    # make_mode.run_make_mode(sys.argv[2:])

    print('\n\n\nObjects that could not be created:')
    print(not_created_objects)

    sys.exit(-1)
