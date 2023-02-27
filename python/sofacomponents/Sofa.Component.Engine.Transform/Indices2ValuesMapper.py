# -*- coding: utf-8 -*-


"""
Component Indices2ValuesMapper

.. autofunction:: Indices2ValuesMapper

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Indices2ValuesMapper(attachedTo , name='Indices2ValuesMapper', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, inputValues=array([], dtype=float64), indices=array([], dtype=float64), values=array([], dtype=float64), outputValues=array([], dtype=float64), defaultValue=1.0, **kwargs):
    """?


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 inputValues: Already existing values (can be empty) 

		 indices: Indices to map value on 

		 values: Values to map indices on 

		 outputValues: New map between indices and values

		 defaultValue: Default value for indices without any value


    """
    return attachedTo.createObject("Indices2ValuesMapper" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, inputValues=inputValues, indices=indices, values=values, outputValues=outputValues, defaultValue=defaultValue, **kwargs)
