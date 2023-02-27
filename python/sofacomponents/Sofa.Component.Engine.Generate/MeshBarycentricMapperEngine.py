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

        
def MeshBarycentricMapperEngine(attachedTo , name='MeshBarycentricMapperEngine', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, inputPositions=array([], shape=(0, 3), dtype=float64), mappedPointPositions=array([], shape=(0, 3), dtype=float64), barycentricPositions=array([], shape=(0, 3), dtype=float64), tableElements=array([], dtype=int32), computeLinearInterpolation=0, linearInterpolationIndices=array([], shape=(0, 1), dtype=int32), linearInterpolationValues=array([], shape=(0, 1), dtype=float64), **kwargs):
    """This class maps a set of points in a topological model and provide barycentric coordinates


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 inputPositions: Initial positions of the master points

		 mappedPointPositions: Initial positions of the points to be mapped

		 barycentricPositions: Output : Barycentric positions of the mapped points

		 tableElements: Output : Table that provides the index of the element to which each input point belongs

		 computeLinearInterpolation: if true, computes a linear interpolation (debug)

		 linearInterpolationIndices: Indices of a linear interpolation

		 linearInterpolationValues: Values of a linear interpolation


    """
    return attachedTo.createObject("MeshBarycentricMapperEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, inputPositions=inputPositions, mappedPointPositions=mappedPointPositions, barycentricPositions=barycentricPositions, tableElements=tableElements, computeLinearInterpolation=computeLinearInterpolation, linearInterpolationIndices=linearInterpolationIndices, linearInterpolationValues=linearInterpolationValues, **kwargs)
