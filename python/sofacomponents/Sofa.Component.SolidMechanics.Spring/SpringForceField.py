# -*- coding: utf-8 -*-


"""
Component SpringForceField

.. autofunction:: SpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SpringForceField(attachedTo , name='SpringForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, stiffness=100.0, damping=5.0, showArrowSize=0.009999999776482582, drawMode=0, spring=[], springsIndices1=array([], dtype=int32), springsIndices2=array([], dtype=int32), **kwargs):
    """Springs


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 stiffness: uniform stiffness for the all springs

		 damping: uniform damping for the all springs

		 showArrowSize: size of the axis

		 drawMode: The way springs will be drawn:
- 0: Line
- 1:Cylinder
- 2: Arrow

		 spring: pairs of indices, stiffness, damping, rest length

		 springsIndices1: List of indices in springs from the first mstate

		 springsIndices2: List of indices in springs from the second mstate


    """
    return attachedTo.createObject("SpringForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, stiffness=stiffness, damping=damping, showArrowSize=showArrowSize, drawMode=drawMode, spring=spring, springsIndices1=springsIndices1, springsIndices2=springsIndices2, **kwargs)
