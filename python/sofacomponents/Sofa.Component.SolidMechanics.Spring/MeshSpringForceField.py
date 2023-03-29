# -*- coding: utf-8 -*-


"""
Component MeshSpringForceField

.. autofunction:: MeshSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MeshSpringForceField(attachedTo , name='MeshSpringForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, stiffness=100.0, damping=5.0, showArrowSize=0.009999999776482582, drawMode=0, spring=[], springsIndices1=array([], dtype=int32), springsIndices2=array([], dtype=int32), indices1=array([], dtype=int32), indices2=array([], dtype=int32), lengths=array([], dtype=float64), linesStiffness=0.0, linesDamping=0.0, trianglesStiffness=0.0, trianglesDamping=0.0, quadsStiffness=0.0, quadsDamping=0.0, tetrahedraStiffness=0.0, tetrahedraDamping=0.0, cubesStiffness=0.0, cubesDamping=0.0, noCompression=0, drawMinElongationRange=8.0, drawMaxElongationRange=15.0, drawSpringSize=8.0, localRange=array([-1, -1], dtype=int32), **kwargs):
    """Spring force field acting along the edges of a mesh


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

		 indices1: Indices of the source points on the first model

		 indices2: Indices of the fixed points on the second model

		 lengths: List of lengths to create the springs. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, 0 will be applied everywhere

		 linesStiffness: Stiffness for the Lines

		 linesDamping: Damping for the Lines

		 trianglesStiffness: Stiffness for the Triangles

		 trianglesDamping: Damping for the Triangles

		 quadsStiffness: Stiffness for the Quads

		 quadsDamping: Damping for the Quads

		 tetrahedraStiffness: Stiffness for the Tetrahedra

		 tetrahedraDamping: Damping for the Tetrahedra

		 cubesStiffness: Stiffness for the Cubes

		 cubesDamping: Damping for the Cubes

		 noCompression: Only consider elongation

		 drawMinElongationRange: Min range of elongation (red eongation - blue neutral - green compression)

		 drawMaxElongationRange: Max range of elongation (red eongation - blue neutral - green compression)

		 drawSpringSize: Size of drawed lines

		 localRange: optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitionning)


    """
    return attachedTo.createObject("MeshSpringForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, stiffness=stiffness, damping=damping, showArrowSize=showArrowSize, drawMode=drawMode, spring=spring, springsIndices1=springsIndices1, springsIndices2=springsIndices2, indices1=indices1, indices2=indices2, lengths=lengths, linesStiffness=linesStiffness, linesDamping=linesDamping, trianglesStiffness=trianglesStiffness, trianglesDamping=trianglesDamping, quadsStiffness=quadsStiffness, quadsDamping=quadsDamping, tetrahedraStiffness=tetrahedraStiffness, tetrahedraDamping=tetrahedraDamping, cubesStiffness=cubesStiffness, cubesDamping=cubesDamping, noCompression=noCompression, drawMinElongationRange=drawMinElongationRange, drawMaxElongationRange=drawMaxElongationRange, drawSpringSize=drawSpringSize, localRange=localRange, **kwargs)
