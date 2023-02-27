# -*- coding: utf-8 -*-


"""
Component PrecomputedConstraintCorrection

.. autofunction:: PrecomputedConstraintCorrection

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PrecomputedConstraintCorrection(attachedTo , name='PrecomputedConstraintCorrection', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, rotations=0, restDeformations=0, recompute=0, debugViewFrameScale=1.0, fileCompliance='', fileDir='', **kwargs):
    """Component computing constraint forces within a simulated body using the compliance method.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 rotations: 

		 restDeformations: 

		 recompute: if true, always recompute the compliance

		 debugViewFrameScale: Scale on computed node's frame

		 fileCompliance: Precomputed compliance matrix data file

		 fileDir: If not empty, the compliance will be saved in this repertory


    """
    return attachedTo.createObject("PrecomputedConstraintCorrection" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, rotations=rotations, restDeformations=restDeformations, recompute=recompute, debugViewFrameScale=debugViewFrameScale, fileCompliance=fileCompliance, fileDir=fileDir, **kwargs)
