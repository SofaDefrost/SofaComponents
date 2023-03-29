# -*- coding: utf-8 -*-


"""
Component TopologyBoundingTrasher

.. autofunction:: TopologyBoundingTrasher

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TopologyBoundingTrasher(attachedTo , name='TopologyBoundingTrasher', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=1, position=array([], shape=(0, 3), dtype=float64), box=array([-1000., -1000., -1000.,  1000.,  1000.,  1000.]), drawBox=0, **kwargs):
    """A class to remove all elements going outside from the given Bounding Box.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 position: position coordinates of the topology object to interact with.

		 box: List of boxes defined by xmin,ymin,zmin, xmax,ymax,zmax

		 drawBox: Draw Boxes. (default = false)


    """
    return attachedTo.createObject("TopologyBoundingTrasher" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, position=position, box=box, drawBox=drawBox, **kwargs)
