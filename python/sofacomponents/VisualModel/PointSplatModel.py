# -*- coding: utf-8 -*-


"""
Component PointSplatModel

.. autofunction:: PointSplatModel

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PointSplatModel(attachedTo , name='PointSplatModel', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, radius=1.0, textureSize=32, alpha=1.0, color='1 1 1 1', pointData=[], **kwargs):
    """A simple visualization for a cloud of points.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 radius: Radius of the spheres.

		 textureSize: Size of the billboard texture.

		 alpha: Opacity of the billboards. 1.0 is 100% opaque.

		 color: Billboard color.(default=[1.0,1.0,1.0,1.0])

		 pointData: scalar field modulating point colors


    """
    return attachedTo.createObject("PointSplatModel" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, radius=radius, textureSize=textureSize, alpha=alpha, color=color, pointData=pointData, **kwargs)
