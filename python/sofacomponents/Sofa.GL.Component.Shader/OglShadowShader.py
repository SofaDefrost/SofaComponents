# -*- coding: utf-8 -*-


"""
Component OglShadowShader

.. autofunction:: OglShadowShader

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def OglShadowShader(attachedTo , name='OglShadowShader', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, turnOn=1, passive=0, fileVertexShaders="[ 'shaders/hardShadows/shadowMapping.vert' , 'shaders/hardShadows/shadowMapping.vert' ]", fileFragmentShaders="[ 'shaders/hardShadows/shadowMapping.frag' , 'shaders/hardShadows/shadowMapping.frag' ]", fileGeometryShaders='[]', fileTessellationControlShaders='[]', fileTessellationEvaluationShaders='[]', geometryInputType=-1, geometryOutputType=-1, geometryVerticesOut=-1, tessellationOuterLevel=1.0, tessellationInnerLevel=1.0, indexActiveShader=0, backfaceWriting=0, clampVertexColor=1, **kwargs):
    """This component sets the shader system responsible of the shadowing.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 turnOn: Turn On the shader?

		 passive: Will this shader be activated manually or automatically?

		 fileVertexShaders: Set the vertex shader filename to load

		 fileFragmentShaders: Set the fragment shader filename to load

		 fileGeometryShaders: Set the geometry shader filename to load

		 fileTessellationControlShaders: Set the tessellation control filename to load

		 fileTessellationEvaluationShaders: Set the tessellation evaluation filename to load

		 geometryInputType: Set input types for the geometry shader

		 geometryOutputType: Set output types for the geometry shader

		 geometryVerticesOut: Set max number of vertices in output for the geometry shader

		 tessellationOuterLevel: For tessellation without control shader: default outer level (edge subdivisions)

		 tessellationInnerLevel: For tessellation without control shader: default inner level (face subdivisions)

		 indexActiveShader: Set current active shader

		 backfaceWriting: it enables writing to gl_BackColor inside a GLSL vertex shader

		 clampVertexColor: clamp the vertex color between 0 and 1


    """
    return attachedTo.createObject("OglShadowShader" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, turnOn=turnOn, passive=passive, fileVertexShaders=fileVertexShaders, fileFragmentShaders=fileFragmentShaders, fileGeometryShaders=fileGeometryShaders, fileTessellationControlShaders=fileTessellationControlShaders, fileTessellationEvaluationShaders=fileTessellationEvaluationShaders, geometryInputType=geometryInputType, geometryOutputType=geometryOutputType, geometryVerticesOut=geometryVerticesOut, tessellationOuterLevel=tessellationOuterLevel, tessellationInnerLevel=tessellationInnerLevel, indexActiveShader=indexActiveShader, backfaceWriting=backfaceWriting, clampVertexColor=clampVertexColor, **kwargs)
