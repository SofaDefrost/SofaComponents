# -*- coding: utf-8 -*-


"""
Component CompositingVisualLoop

.. autofunction:: CompositingVisualLoop

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def CompositingVisualLoop(attachedTo , name='CompositingVisualLoop', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, vertFilename='shaders/compositing.vert', fragFilename='shaders/compositing.frag', **kwargs):
    """Visual loop enabling multipass rendering. Needs multiple fbo data and a compositing shader


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 vertFilename: Set the vertex shader filename to load

		 fragFilename: Set the fragment shader filename to load


    """
    return attachedTo.createObject("CompositingVisualLoop" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, vertFilename=vertFilename, fragFilename=fragFilename, **kwargs)
