# -*- coding: utf-8 -*-


"""
Component GenericConstraintCorrection

.. autofunction:: GenericConstraintCorrection

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def GenericConstraintCorrection(attachedTo , name='GenericConstraintCorrection', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, complianceFactor=1.0, **kwargs):
    """

    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 complianceFactor: Factor applied to the position factor and velocity factor used to calculate compliance matrix


    """
    return attachedTo.createObject("GenericConstraintCorrection" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, complianceFactor=complianceFactor, **kwargs)
