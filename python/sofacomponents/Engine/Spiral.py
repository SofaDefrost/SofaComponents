# -*- coding: utf-8 -*-


"""
Component Spiral

.. autofunction:: Spiral

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Spiral(attachedTo , name='Spiral', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, rest_position=[], position=[], curvature=0.2, **kwargs):
    """This class truns on spiral any topological model


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 rest_position: Rest position coordinates of the degrees of freedom

		 position: Position coordinates of the degrees of freedom

		 curvature: Spiral curvature factor


    """
    return attachedTo.createObject("Spiral" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, rest_position=rest_position, position=position, curvature=curvature, **kwargs)
