# -*- coding: utf-8 -*-


"""
Component PointSetTopologyContainer

.. autofunction:: PointSetTopologyContainer

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PointSetTopologyContainer(attachedTo , name='PointSetTopologyContainer', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, filename='', position=array([], shape=(0, 3), dtype=float64), checkTopology=0, nbPoints=0, **kwargs):
    """Point set topology container


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 filename: Filename of the mesh

		 position: Initial position of points

		 checkTopology: Parameter to activate internal topology checks (might slow down the simulation)

		 nbPoints: Number of points


    """
    return attachedTo.createObject("PointSetTopologyContainer" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, filename=filename, position=position, checkTopology=checkTopology, nbPoints=nbPoints, **kwargs)
