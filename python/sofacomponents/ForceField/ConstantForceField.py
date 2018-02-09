# -*- coding: utf-8 -*-


"""
Component ConstantForceField

.. autofunction:: ConstantForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ConstantForceField(attachedTo , name='ConstantForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, indices=[], indexFromEnd=0, forces=[], force=[[0.0, 0.0, 0.0]], totalForce=[[0.0, 0.0, 0.0]], arrowSizeCoef=0.0, showColor='0.2 0.9 0.3 1', **kwargs):
    """Constant forces applied to given degrees of freedom


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 indices: indices where the forces are applied

		 indexFromEnd: Concerned DOFs indices are numbered from the end of the MState DOFs vector. (default=false)

		 forces: applied forces at each point

		 force: applied force to all points if forces attribute is not specified

		 totalForce: total force for all points, will be distributed uniformly over points

		 arrowSizeCoef: Size of the drawn arrows (0->no arrows, sign->direction of drawing. (default=0)

		 showColor: Color for object display (default: [0.2,0.9,0.3,1.0])


    """
    return attachedTo.createObject("ConstantForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, indices=indices, indexFromEnd=indexFromEnd, forces=forces, force=force, totalForce=totalForce, arrowSizeCoef=arrowSizeCoef, showColor=showColor, **kwargs)
