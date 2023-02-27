# -*- coding: utf-8 -*-


"""
Component OglIntVariable

.. autofunction:: OglIntVariable

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OglIntVariable(attachedTo , name='OglIntVariable', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, id='', indexShader=0, value=0, **kwargs):
    """OglIntVariable


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 id: Set an ID name

		 indexShader: Set the index of the desired shader you want to apply this parameter

		 value: Set Uniform Value


    """
    return attachedTo.createObject("OglIntVariable" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, id=id, indexShader=indexShader, value=value, **kwargs)
