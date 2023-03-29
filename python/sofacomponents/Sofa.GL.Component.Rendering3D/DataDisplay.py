# -*- coding: utf-8 -*-


"""
Component DataDisplay

.. autofunction:: DataDisplay

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DataDisplay(attachedTo , name='DataDisplay', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, position=array([], shape=(0, 3), dtype=float64), restPosition=array([], shape=(0, 3), dtype=float64), normal=array([], shape=(0, 3), dtype=float64), maximalRange=1, pointData=array([], dtype=float64), triangleData=array([], dtype=float64), quadData=array([], dtype=float64), pointTriangleData=array([], dtype=float64), pointQuadData=array([], dtype=float64), colorNaN=array([0., 0., 0., 1.], dtype=float32), userRange=array([ 1., -1.], dtype=float32), currentMin=0.0, currentMax=0.0, shininess=-1.0, transparency=1.0, **kwargs):
    """Rendering of meshes colored by data


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 position: Vertices coordinates

		 restPosition: Vertices rest coordinates

		 normal: Normals of the model

		 maximalRange: Keep the maximal range through all timesteps

		 pointData: Data associated with nodes

		 triangleData: Data associated with triangles

		 quadData: Data associated with quads

		 pointTriangleData: Data associated with nodes per triangle

		 pointQuadData: Data associated with nodes per quad

		 colorNaN: Color used for NaN values.(default=[0.0,0.0,0.0,1.0])

		 userRange: Clamp to this values (if max>min)

		 currentMin: Current min range

		 currentMax: Current max range

		 shininess: Shininess for rendering point-based data [0,128].  <0 means no specularity

		 transparency: transparency draw objects with transparency, the value varies between 0. and 1. Where 1. means no transparency and 0 full transparency


    """
    return attachedTo.createObject("DataDisplay" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, position=position, restPosition=restPosition, normal=normal, maximalRange=maximalRange, pointData=pointData, triangleData=triangleData, quadData=quadData, pointTriangleData=pointTriangleData, pointQuadData=pointQuadData, colorNaN=colorNaN, userRange=userRange, currentMin=currentMin, currentMax=currentMax, shininess=shininess, transparency=transparency, **kwargs)
