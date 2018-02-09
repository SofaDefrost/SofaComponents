# -*- coding: utf-8 -*-


"""
Component TestResult

.. autofunction:: TestResult

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TestResult(attachedTo , name='TestResult', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, result='Fail', **kwargs):
    """This component stores the results of tests.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 result: 


    """
    return attachedTo.createObject("TestResult" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, result=result, **kwargs)
