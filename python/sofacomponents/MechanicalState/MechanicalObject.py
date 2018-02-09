# -*- coding: utf-8 -*-


"""
Component MechanicalObject

.. autofunction:: MechanicalObject

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MechanicalObject(attachedTo , name='MechanicalObject', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, position=[[0.0, 0.0, 0.0]], velocity=[[0.0, 0.0, 0.0]], force=[[0.0, 0.0, 0.0]], externalForce=[[0.0, 0.0, 0.0]], derivX=[], free_position=[], free_velocity=[], rest_position=[], constraint='', mappingJacobian='', reset_position=[], reset_velocity=[], restScale=1.0, useTopology=1, showObject=0, showObjectScale=0.10000000149011612, showIndices=0, showIndicesScale=0.019999999552965164, showVectors=0, showVectorsScale=9.999999747378752e-05, drawMode=0, showColor=[[1.0, 1.0, 1.0, 1.0]], isToPrint=0, translation=[[0.0, 0.0, 0.0]], rotation=[[0.0, 0.0, 0.0]], scale3d=[[1.0, 1.0, 1.0]], translation2=[[0.0, 0.0, 0.0]], rotation2=[[0.0, 0.0, 0.0]], size=1, reserve=0, **kwargs):
    """mechanical state vectors


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 position: position coordinates of the degrees of freedom

		 velocity: velocity coordinates of the degrees of freedom

		 force: force vector of the degrees of freedom

		 externalForce: externalForces vector of the degrees of freedom

		 derivX: dx vector of the degrees of freedom

		 free_position: free position coordinates of the degrees of freedom

		 free_velocity: free velocity coordinates of the degrees of freedom

		 rest_position: rest position coordinates of the degrees of freedom

		 constraint: constraints applied to the degrees of freedom

		 mappingJacobian: mappingJacobian applied to the degrees of freedom

		 reset_position: reset position coordinates of the degrees of freedom

		 reset_velocity: reset velocity coordinates of the degrees of freedom

		 restScale: optional scaling of rest position coordinates (to simulated pre-existing internal tension).(default = 1.0)

		 useTopology: Shall this object rely on any active topology to initialize its size and positions

		 showObject: Show objects. (default=false)

		 showObjectScale: Scale for object display. (default=0.1)

		 showIndices: Show indices. (default=false)

		 showIndicesScale: Scale for indices display. (default=0.02)

		 showVectors: Show velocity. (default=false)

		 showVectorsScale: Scale for vectors display. (default=0.0001)

		 drawMode: The way vectors will be drawn:
- 0: Line
- 1:Cylinder
- 2: Arrow.

The DOFS will be drawn:
- 0: point
- >1: sphere. (default=0)

		 showColor: Color for object display. (default=[1 1 1 1])

		 isToPrint: suppress somes data before using save as function. (default=false)

		 translation: Translation of the DOFs

		 rotation: Rotation of the DOFs

		 scale3d: Scale of the DOFs in 3 dimensions

		 translation2: Translation of the DOFs, applied after the rest position has been computed

		 rotation2: Rotation of the DOFs, applied the after the rest position has been computed

		 size: Size of the vectors

		 reserve: Size to reserve when creating vectors. (default=0)


    """
    return attachedTo.createObject("MechanicalObject" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, position=position, velocity=velocity, force=force, externalForce=externalForce, derivX=derivX, free_position=free_position, free_velocity=free_velocity, rest_position=rest_position, constraint=constraint, mappingJacobian=mappingJacobian, reset_position=reset_position, reset_velocity=reset_velocity, restScale=restScale, useTopology=useTopology, showObject=showObject, showObjectScale=showObjectScale, showIndices=showIndices, showIndicesScale=showIndicesScale, showVectors=showVectors, showVectorsScale=showVectorsScale, drawMode=drawMode, showColor=showColor, isToPrint=isToPrint, translation=translation, rotation=rotation, scale3d=scale3d, translation2=translation2, rotation2=rotation2, size=size, reserve=reserve, **kwargs)
