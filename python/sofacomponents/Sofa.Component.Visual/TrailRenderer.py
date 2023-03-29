# -*- coding: utf-8 -*-


"""
Component TrailRenderer

.. autofunction:: TrailRenderer

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TrailRenderer(attachedTo , name='TrailRenderer', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=1, position=array([], shape=(0, 3), dtype=float64), nbSteps=100, color=array([0., 1., 0., 1.], dtype=float32), thickness=1.0, **kwargs):
    """Render a trail behind particles


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 position: Position of the particles behind which a trail is rendered

		 nbSteps: Number of time steps to use to render the trail

		 color: Color of the trail

		 thickness: Thickness of the trail


    """
    return attachedTo.createObject("TrailRenderer" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, position=position, nbSteps=nbSteps, color=color, thickness=thickness, **kwargs)
