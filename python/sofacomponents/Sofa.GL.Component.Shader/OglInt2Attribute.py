# -*- coding: utf-8 -*-


"""
Component OglInt2Attribute

.. autofunction:: OglInt2Attribute

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OglInt2Attribute(attachedTo , name='OglInt2Attribute', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, id='', indexShader=0, value=array([], shape=(0, 2), dtype=int32), handleDynamicTopology=1, **kwargs):
    """OglInt2Attribute


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 id: Set an ID name

		 indexShader: Set the index of the desired shader you want to apply this parameter

		 value: internal Data

		 handleDynamicTopology: Activate handling of topological changes on the values of this attribute (resizes only)


    """
    return attachedTo.createObject("OglInt2Attribute" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, id=id, indexShader=indexShader, value=value, handleDynamicTopology=handleDynamicTopology, **kwargs)