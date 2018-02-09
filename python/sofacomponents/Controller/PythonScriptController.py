# -*- coding: utf-8 -*-


"""
Component PythonScriptController

.. autofunction:: PythonScriptController

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PythonScriptController(attachedTo , name='PythonScriptController', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, handleEventTriggersUpdate=0, filename='', classname='', variables=[], timingEnabled=1, autoreload=0, **kwargs):
    """A Sofa controller scripted in python


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 handleEventTriggersUpdate: Event handling frequency controls the controller update frequency

		 filename: Python script filename

		 classname: Python class implemented in the script to instanciate for the controller

		 variables: Array of string variables (equivalent to a c-like argv)

		 timingEnabled: Set this attribute to true or false to activate/deactivate the gathering of timing statistics on the python execution time. Default value is setto true.

		 autoreload: Automatically reload the file when the source code is changed. Default value is set to false


    """
    return attachedTo.createObject("PythonScriptController" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, handleEventTriggersUpdate=handleEventTriggersUpdate, filename=filename, classname=classname, variables=variables, timingEnabled=timingEnabled, autoreload=autoreload, **kwargs)
