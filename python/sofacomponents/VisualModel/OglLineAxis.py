# -*- coding: utf-8 -*-


"""
Component OglLineAxis

.. autofunction:: OglLineAxis

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OglLineAxis(attachedTo , name='OglLineAxis', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, axis='xyz', size=10.0, thickness=1.0, draw=1, **kwargs):
    """Display scene axis


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 axis: Axis to draw

		 size: Size of the squared grid

		 thickness: Thickness of the lines in the grid

		 draw: Display the grid or not


    """
    return attachedTo.createObject("OglLineAxis" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, axis=axis, size=size, thickness=thickness, draw=draw, **kwargs)
