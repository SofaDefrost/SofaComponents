# -*- coding: utf-8 -*-


"""
Component TextureInterpolation

.. autofunction:: TextureInterpolation

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TextureInterpolation(attachedTo , name='TextureInterpolation', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, input_states=[], input_coordinates=[], output_coordinates=[], scalarField=1, min_value=0.0, max_value=0.0, manual_scale=0, drawPotentiels=0, showIndicesScale=9.999999747378752e-05, vertexPloted=0, graph='', **kwargs):
    """Create texture coordinate for a given field


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 input_states: input array of state values.

		 input_coordinates: input array of coordinates values.

		 output_coordinates: output array of texture coordinates.

		 scalarField: To interpolate only the first dimension of input field (useful if this component need to be templated in higher dimension).

		 min_value: minimum value of state value for interpolation.

		 max_value: maximum value of state value for interpolation.

		 manual_scale: compute texture interpolation on manually scale defined above.

		 drawPotentiels: Debug: view state values.

		 showIndicesScale: Debug : scale of state values displayed.

		 vertexPloted: Vertex index of values display in graph for each iteration.

		 graph: Vertex state value per iteration


    """
    return attachedTo.createObject("TextureInterpolation" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, input_states=input_states, input_coordinates=input_coordinates, output_coordinates=output_coordinates, scalarField=scalarField, min_value=min_value, max_value=max_value, manual_scale=manual_scale, drawPotentiels=drawPotentiels, showIndicesScale=showIndicesScale, vertexPloted=vertexPloted, graph=graph, **kwargs)
