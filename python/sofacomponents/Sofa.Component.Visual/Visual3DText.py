# -*- coding: utf-8 -*-


"""
Component Visual3DText

.. autofunction:: Visual3DText

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def Visual3DText(attachedTo , name='Visual3DText', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, text='', position=array([0., 0., 0.], dtype=float32), scale=1.0, color=array([1., 1., 1., 1.], dtype=float32), depthTest=1, **kwargs):
    """Display 3D camera-oriented text


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 text: Test to display

		 position: 3d position

		 scale: text scale

		 color: text color. (default=[1.0,1.0,1.0,1.0])

		 depthTest: perform depth test


    """
    return attachedTo.createObject("Visual3DText" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, text=text, position=position, scale=scale, color=color, depthTest=depthTest, **kwargs)
