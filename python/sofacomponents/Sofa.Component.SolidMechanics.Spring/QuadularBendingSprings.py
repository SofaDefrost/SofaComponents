# -*- coding: utf-8 -*-


"""
Component QuadularBendingSprings

.. autofunction:: QuadularBendingSprings

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def QuadularBendingSprings(attachedTo , name='QuadularBendingSprings', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, stiffness=100000.0, damping=1.0, edgeInfo=[], **kwargs):
    """Springs added to a quad mesh to prevent bending


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

		 edgeInfo: Internal edge data


    """
    return attachedTo.createObject("QuadularBendingSprings" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, stiffness=stiffness, damping=damping, edgeInfo=edgeInfo, **kwargs)
