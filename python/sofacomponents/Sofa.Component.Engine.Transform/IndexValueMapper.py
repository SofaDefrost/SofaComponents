# -*- coding: utf-8 -*-


"""
Component IndexValueMapper

.. autofunction:: IndexValueMapper

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def IndexValueMapper(attachedTo , name='IndexValueMapper', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, inputValues=array([], dtype=float64), indices=array([], dtype=int32), value=0.0, outputValues=array([], dtype=float64), defaultValue=1.0, **kwargs):
    """Input values to output values mapper. Includes indices rules, such as replacement, resize


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 inputValues: Already existing values (can be empty) 

		 indices: Indices to map value on 

		 value: Value to map indices on 

		 outputValues: New map between indices and values

		 defaultValue: Default value for indices without any value


    """
    return attachedTo.createObject("IndexValueMapper" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, inputValues=inputValues, indices=indices, value=value, outputValues=outputValues, defaultValue=defaultValue, **kwargs)
