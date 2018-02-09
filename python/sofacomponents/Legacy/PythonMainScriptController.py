# -*- coding: utf-8 -*-


"""
Component PythonMainScriptController

.. autofunction:: PythonMainScriptController

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PythonMainScriptController(attachedTo , **kwargs):
    """A Sofa controller scripted in python, looking for callbacks directly in the file (not in a class like the more general and powerful PythonScriptController


    Args:


    """
    return attachedTo.createObject("PythonMainScriptController" , **kwargs)
