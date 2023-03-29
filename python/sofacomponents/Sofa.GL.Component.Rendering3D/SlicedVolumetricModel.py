# -*- coding: utf-8 -*-


"""
Component SlicedVolumetricModel

.. autofunction:: SlicedVolumetricModel

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SlicedVolumetricModel(attachedTo , name='SlicedVolumetricModel', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, alpha=0.20000000298023224, color=array([1., 1., 1., 1.], dtype=float32), nbSlices=100, **kwargs):
    """A simple visualization for a cloud of points.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 alpha: Opacity of the billboards. 1.0 is 100% opaque.

		 color: Billboard color.(default=1.0,1.0,1.0,1.0)

		 nbSlices: Number of billboards.


    """
    return attachedTo.createObject("SlicedVolumetricModel" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, alpha=alpha, color=color, nbSlices=nbSlices, **kwargs)
