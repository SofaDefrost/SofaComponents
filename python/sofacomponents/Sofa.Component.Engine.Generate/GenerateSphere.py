# -*- coding: utf-8 -*-


"""
Component GenerateSphere

.. autofunction:: GenerateSphere

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def GenerateSphere(attachedTo , name='GenerateSphere', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, output_TetrahedraPosition=array([[ 0.        ,  0.        ,  0.        ],
       [ 0.07229441, -0.10606276, -0.15337604],
       [-0.10206801,  0.01006172, -0.17169998],
       [ 0.08473626,  0.10380406, -0.14847385],
       [ 0.19911829, -0.01145768, -0.01485351],
       [ 0.08300602, -0.17643568,  0.04450227],
       [-0.10313736, -0.16313596, -0.05243419],
       [-0.07229441,  0.10606276,  0.15337604],
       [ 0.10206801, -0.01006172,  0.17169998],
       [-0.08473626, -0.10380406,  0.14847385],
       [-0.19911829,  0.01145768,  0.01485351],
       [-0.08300602,  0.17643568, -0.04450227],
       [ 0.10313736,  0.16313596,  0.05243419]]), tetrahedra=array([[ 0,  1,  2,  6],
       [ 0,  1,  3,  2],
       [ 0,  1,  4,  3],
       [ 0,  1,  5,  4],
       [ 0,  1,  6,  5],
       [ 0,  2,  3, 11],
       [ 0,  2, 10,  6],
       [ 0,  2, 11, 10],
       [ 0,  3,  4, 12],
       [ 0,  3, 12, 11],
       [ 0,  4,  5,  8],
       [ 0,  4,  8, 12],
       [ 0,  5,  6,  9],
       [ 0,  5,  9,  8],
       [ 0,  6, 10,  9],
       [ 0,  7,  8,  9],
       [ 0,  7,  9, 10],
       [ 0,  7, 10, 11],
       [ 0,  7, 11, 12],
       [ 0,  7, 12,  8]], dtype=int32), output_TrianglesPosition=array([[ 0.07229441, -0.10606276, -0.15337604],
       [-0.10206801,  0.01006172, -0.17169998],
       [ 0.08473626,  0.10380406, -0.14847385],
       [ 0.19911829, -0.01145768, -0.01485351],
       [ 0.08300602, -0.17643568,  0.04450227],
       [-0.10313736, -0.16313596, -0.05243419],
       [-0.07229441,  0.10606276,  0.15337604],
       [ 0.10206801, -0.01006172,  0.17169998],
       [-0.08473626, -0.10380406,  0.14847385],
       [-0.19911829,  0.01145768,  0.01485351],
       [-0.08300602,  0.17643568, -0.04450227],
       [ 0.10313736,  0.16313596,  0.05243419]]), triangles=array([[ 0,  1,  5],
       [ 0,  2,  1],
       [ 0,  3,  2],
       [ 0,  4,  3],
       [ 0,  5,  4],
       [ 1,  2, 10],
       [ 1,  9,  5],
       [ 1, 10,  9],
       [ 2,  3, 11],
       [ 2, 11, 10],
       [ 3,  4,  7],
       [ 3,  7, 11],
       [ 4,  5,  8],
       [ 4,  8,  7],
       [ 5,  9,  8],
       [ 6,  7,  8],
       [ 6,  8,  9],
       [ 6,  9, 10],
       [ 6, 10, 11],
       [ 6, 11,  7]], dtype=int32), BezierTetrahedronDegree=0, BezierTetrahedronWeights=array([], dtype=float64), isBezierTetrahedronRational=[], BezierTriangleDegree=0, BezierTriangleWeights=array([], dtype=float64), isBezierTriangleRational=[], radius=0.2, origin=array([0., 0., 0.]), tessellationDegree=1, platonicSolid='icosahedron', **kwargs):
    """Generate a sphereical (Bezier) Tetrahedral and Triangular Mesh


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 output_TetrahedraPosition: output array of 3d points of tetrahedra mesh

		 tetrahedra: output mesh tetrahedra

		 output_TrianglesPosition: output array of 3d points of triangle mesh

		 triangles: output triangular mesh

		 BezierTetrahedronDegree: order of Bezier tetrahedra

		 BezierTetrahedronWeights: weights of rational Bezier tetrahedra

		 isBezierTetrahedronRational: booleans indicating if each Bezier tetrahedron is rational or integral

		 BezierTriangleDegree: order of Bezier triangles

		 BezierTriangleWeights: weights of rational Bezier triangles

		 isBezierTriangleRational: booleans indicating if each Bezier triangle is rational or integral

		 radius: input sphere radius

		 origin: sphere center point

		 tessellationDegree: Degree of tessellation of each Platonic triangulation

		 platonicSolid: name of the Platonic triangulation used to create the spherical dome : either "tetrahedron", "octahedron" or "icosahedron"


    """
    return attachedTo.createObject("GenerateSphere" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, output_TetrahedraPosition=output_TetrahedraPosition, tetrahedra=tetrahedra, output_TrianglesPosition=output_TrianglesPosition, triangles=triangles, BezierTetrahedronDegree=BezierTetrahedronDegree, BezierTetrahedronWeights=BezierTetrahedronWeights, isBezierTetrahedronRational=isBezierTetrahedronRational, BezierTriangleDegree=BezierTriangleDegree, BezierTriangleWeights=BezierTriangleWeights, isBezierTriangleRational=isBezierTriangleRational, radius=radius, origin=origin, tessellationDegree=tessellationDegree, platonicSolid=platonicSolid, **kwargs)
