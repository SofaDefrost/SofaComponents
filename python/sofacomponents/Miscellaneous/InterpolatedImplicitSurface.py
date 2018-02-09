# -*- coding: utf-8 -*-


"""
Component InterpolatedImplicitSurface

.. autofunction:: InterpolatedImplicitSurface

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def InterpolatedImplicitSurface(attachedTo , name='InterpolatedImplicitSurface', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, file='', maxDomains=1, dx=0.0, dy=0.0, dz=0.0, **kwargs):
    """Deprecated. This class is forwarding DiscreteGridField.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 file: MHD file for the distance map

		 maxDomains: Number of domains available for caching

		 dx: x translation

		 dy: y translation

		 dz: z translation


    """
    return attachedTo.createObject("InterpolatedImplicitSurface" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, file=file, maxDomains=maxDomains, dx=dx, dy=dy, dz=dz, **kwargs)
