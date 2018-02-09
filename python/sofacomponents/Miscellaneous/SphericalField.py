# -*- coding: utf-8 -*-


"""
Component SphericalField

.. autofunction:: SphericalField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SphericalField(attachedTo , name='SphericalField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, inside=0, radius=1.0, center=[[0.0, 0.0, 0.0]], **kwargs):
    """A spherical implicit field.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 inside: If true the field is oriented inside (resp. outside) the sphere. (default = false)

		 radius: Radius of Sphere emitting the field. (default = 1)

		 center: Position of the Sphere Surface. (default=0 0 0)


    """
    return attachedTo.createObject("SphericalField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, inside=inside, radius=radius, center=center, **kwargs)
