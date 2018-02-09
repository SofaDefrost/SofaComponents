# -*- coding: utf-8 -*-


"""
Component SphereLoader

.. autofunction:: SphereLoader

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SphereLoader(attachedTo , name='SphereLoader', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, filename='', position=[], listRadius=[], scale=[[0.0, 0.0, 0.0]], translation=[[0.0, 0.0, 0.0]], **kwargs):
    """Loader for sphere model description files


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 filename: Filename of the object

		 position: Sphere centers

		 listRadius: Radius of each sphere

		 scale: Scale applied to sphere positions & radius

		 translation: Translation applied to sphere positions


    """
    return attachedTo.createObject("SphereLoader" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, filename=filename, position=position, listRadius=listRadius, scale=scale, translation=translation, **kwargs)
