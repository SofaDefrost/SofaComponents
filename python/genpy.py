"""
A sofa scene to autogenerate the python wrapping function from the runtime informations.

"""

# -*- coding: utf-8 -*-
import re
import sys, os
import Sofa
from sphinx import make_mode
reserved = ["in","with", "for", "if", "def", "class", "global"]
def kv2params(kw):
    p=""
    req = []
    opt = []
    for k in kw:
        if k.name in reserved:
            print("Warning: this is an invalid arguments as it is a python keyword")
            continue

        if k.name.find(" ")!=-1:
            print("Warning: this is an invalid arguments name: "+repr(k.name))
            continue

        if len(k.name) != 0:
            if k.isRequired():
                req.append(k)
            else:
                opt.append(k)
                    
    for k in req:
        p+=", "+k.name

    for k in opt:
        p+=", "+k.name+"="+repr(k.value)
    
    return p

def kv2call(kw):
    p=""
    for k in kw:
        if k.name in reserved:
            continue

        if k.name.find(" ")!=-1:
            continue


        if len(k.name) != 0:
            p+=", "+k.name+"="+str(k.name)
    return p

def kv2doc(kw):
    p=""
    for k in kw:
        if len(k.name) == 0:
            continue
        if k.name.find(" ")!=-1:
            continue

        if k.name in reserved:
            p+="\t\t "+k.name+": "+str(k.getHelp())+" (NB: use the kwargs syntax as name is a reserved word in python)\n\n"
        else:
            p+="\t\t "+k.name+": "+str(k.getHelp())+"\n\n"

    return p

def makeInitFile(rootDir):
    entries = {}
    for dirpath, dirnames, filenames in os.walk(rootDir):
        initfile = open(dirpath+"/__init__.py", "wt")
        res = []
        for d in dirnames:
            res.append(d)
        for f in filenames:
            if f.endswith(".py") and f != "__init__.py":
                res.append(f[:-3])
        listc=""
        for r in res:
            listc+="    "+str(r)+"\n\n"       
                
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
        initfile.write("__all__="+repr(res)+"\n")
        for r in res:
            initfile.write("import "+str(r)+"\n")
        initfile.close()

        print(str((dirpath, dirnames, filenames)))

def createScene(rootNode):
    sys.argv = ['./mysphinx.py', '-M', 'html', 'source', 'build']
    backlist=["PythonMainScriptController"]
    rootNode.createObject("MechanicalObject")
    
    for (name, desc) in Sofa.getAvailableComponents():
        categories = ["Legacy"]
        args = {}
        if name not in backlist:
            try:
                print("Processing: " + name)
                obj = rootNode.createObject(name)
                #args = obj.getDataFields()
                args=obj.getListOfDataFields()
                categories = obj.getCategories()
            except Exception,e:
                print("UNable to get DOC")
                pass
        params = kv2params(args)
        params2 = kv2call(args)
        paramsmd = kv2doc(args)
        code = """
        
def %s(attachedTo %s, **kwargs):
    \"\"\"%s

    Args:

%s
    \"\"\"
    return attachedTo.createObject(\"%s\" %s, **kwargs)
""" % (name, params, desc, paramsmd, name, params2)

        targetpath="sofacomponents/"

        if not os.path.exists(targetpath):
            os.mkdir(targetpath)

        pathname = targetpath+categories[0]+"/"
        if not os.path.exists(pathname):
            os.mkdir(pathname)
        outfile=open(pathname+name+".py", "wt")
        outfile.write("# -*- coding: utf-8 -*-\n\n")
        outfile.write("""
\"\"\"
Component %s

.. autofunction:: %s

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
\"\"\"
""" % (name, name) )


        outfile.write(code)

    outfile.close()

    makeInitFile(targetpath)
    print("PROCESSIn DONE")
    #make_mode.run_make_mode(sys.argv[2:]) 
    sys.exit(-1)
