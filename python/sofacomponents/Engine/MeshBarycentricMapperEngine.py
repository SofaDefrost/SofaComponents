# -*- coding: utf-8 -*-


"""
Component MeshBarycentricMapperEngine

.. autofunction:: MeshBarycentricMapperEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MeshBarycentricMapperEngine(attachedTo , name='MeshBarycentricMapperEngine', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, InputMeshName='', InputPositions=[], MappedPointPositions=[], BarycentricPositions=[], TableElements=[], computeLinearInterpolation=0, LinearInterpolationIndices=[], LinearInterpolationValues=[], **kwargs):
    """This class maps a set of points in a topological model and provide barycentric coordinates


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 InputMeshName: Name and path of Input mesh Topology

		 InputPositions: Initial positions of the master points

		 MappedPointPositions: Initial positions of the mapped points

		 BarycentricPositions: Output : Barycentric positions of the mapped points

		 TableElements: Output : Table that provides the element index to which each input point belongs

		 computeLinearInterpolation: if true, computes a linear interpolation (debug)

		 LinearInterpolationIndices: Indices of a linear interpolation

		 LinearInterpolationValues: Values of a linear interpolation


    """
    return attachedTo.createObject("MeshBarycentricMapperEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, InputMeshName=InputMeshName, InputPositions=InputPositions, MappedPointPositions=MappedPointPositions, BarycentricPositions=BarycentricPositions, TableElements=TableElements, computeLinearInterpolation=computeLinearInterpolation, LinearInterpolationIndices=LinearInterpolationIndices, LinearInterpolationValues=LinearInterpolationValues, **kwargs)
