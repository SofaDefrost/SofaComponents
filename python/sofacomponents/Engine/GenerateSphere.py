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

        
def GenerateSphere(attachedTo , name='GenerateSphere', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, output_TetrahedraPosition=[], tetrahedra=[], output_TrianglesPosition=[], triangles=[], BezierTetrahedronDegree=0, BezierTetrahedronWeights=[], isBezierTetrahedronRational=[], BezierTriangleDegree=0, BezierTriangleWeights=[], isBezierTriangleRational=[], radius=0.2, origin=[[0.0, 0.0, 0.0]], tessellationDegree=1, platonicSolid='icosahedron', **kwargs):
    """Generate a sphereical (Bezier) Tetrahedral and Triangular Mesh


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

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
    return attachedTo.createObject("GenerateSphere" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, output_TetrahedraPosition=output_TetrahedraPosition, tetrahedra=tetrahedra, output_TrianglesPosition=output_TrianglesPosition, triangles=triangles, BezierTetrahedronDegree=BezierTetrahedronDegree, BezierTetrahedronWeights=BezierTetrahedronWeights, isBezierTetrahedronRational=isBezierTetrahedronRational, BezierTriangleDegree=BezierTriangleDegree, BezierTriangleWeights=BezierTriangleWeights, isBezierTriangleRational=isBezierTriangleRational, radius=radius, origin=origin, tessellationDegree=tessellationDegree, platonicSolid=platonicSolid, **kwargs)
