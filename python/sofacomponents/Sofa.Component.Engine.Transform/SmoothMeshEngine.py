# -*- coding: utf-8 -*-


"""
Component SmoothMeshEngine

.. autofunction:: SmoothMeshEngine

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SmoothMeshEngine(attachedTo , name='SmoothMeshEngine', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, input_position=array([], shape=(0, 3), dtype=float64), input_indices=array([], dtype=int32), output_position=array([], shape=(0, 3), dtype=float64), nb_iterations=1, showInput=0, showOutput=0, **kwargs):
    """Compute the laplacian smoothing of a mesh


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 input_position: Input position

		 input_indices: Position indices that need to be smoothed, leave empty for all positions

		 output_position: Output position

		 nb_iterations: Number of iterations of laplacian smoothing

		 showInput: showInput

		 showOutput: showOutput


    """
    return attachedTo.createObject("SmoothMeshEngine" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, input_position=input_position, input_indices=input_indices, output_position=output_position, nb_iterations=nb_iterations, showInput=showInput, showOutput=showOutput, **kwargs)
