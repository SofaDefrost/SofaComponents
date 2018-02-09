# -*- coding: utf-8 -*-


"""
Component MergeVisualModels

.. autofunction:: MergeVisualModels

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MergeVisualModels(attachedTo , name='MergeVisualModels', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, position=[], restPosition=[], normal=[], initRestPositions=0, useNormals=1, updateNormals=1, computeTangents=0, updateTangents=1, handleDynamicTopology=1, fixMergedUVSeams=1, keepLines=0, vertices=[], texcoords=[], tangents=[], bitangents=[], edges=[], triangles=[], quads=[], vertPosIdx=[], vertNormIdx=[], fileMesh='', texturename='', translation=[[0.0, 0.0, 0.0]], rotation=[[0.0, 0.0, 0.0]], scale3d=[[1.0, 1.0, 1.0]], scaleTex=[[1.0, 1.0]], translationTex=[[0.0, 0.0]], material='Default Diffuse 1 0.75 0.75 0.75 1 Ambient 1 0.2 0.2 0.2 1 Specular 0 1 1 1 1 Emissive 0 0 0 0 0 Shininess 0 45 ', putOnlyTexCoords=0, srgbTexturing=0, materials='', groups='', blendTranslucency=1, premultipliedAlpha=0, useVBO=1, writeZTransparent=0, alphaBlend=0, depthTest=1, cullFace=0, lineWidth=1.0, pointSize=1.0, lineSmooth=0, pointSmooth=0, isToPrint=0, primitiveType='DEFAULT', blendEquation='GL_FUNC_ADD', sfactor='GL_SRC_ALPHA', dfactor='GL_ONE_MINUS_SRC_ALPHA', nb=1, **kwargs):
    """Merge several visual models


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 position: Vertices coordinates

		 restPosition: Vertices rest coordinates

		 normal: Normals of the model

		 initRestPositions: True if rest positions must be initialized with initial positions

		 useNormals: True if normal smoothing groups should be read from file

		 updateNormals: True if normals should be updated at each iteration

		 computeTangents: True if tangents should be computed at startup

		 updateTangents: True if tangents should be updated at each iteration

		 handleDynamicTopology: True if topological changes should be handled

		 fixMergedUVSeams: True if UV seams should be handled even when duplicate UVs are merged

		 keepLines: keep and draw lines (false by default)

		 vertices: vertices of the model (only if vertices have multiple normals/texcoords, otherwise positions are used)

		 texcoords: coordinates of the texture

		 tangents: tangents for normal mapping

		 bitangents: tangents for normal mapping

		 edges: edges of the model

		 triangles: triangles of the model

		 quads: quads of the model

		 vertPosIdx: If vertices have multiple normals/texcoords stores vertices position indices

		 vertNormIdx: If vertices have multiple normals/texcoords stores vertices normal indices

		 fileMesh:  Path to the model

		 texturename: Name of the Texture

		 translation: Initial Translation of the object

		 rotation: Initial Rotation of the object

		 scale3d: Initial Scale of the object

		 scaleTex: Scale of the texture

		 translationTex: Translation of the texture

		 material: Material

		 putOnlyTexCoords: Give Texture Coordinates without the texture binding

		 srgbTexturing: When sRGB rendering is enabled, is the texture in sRGB colorspace?

		 materials: List of materials

		 groups: Groups of triangles and quads using a given material

		 blendTranslucency: Blend transparent parts

		 premultipliedAlpha: is alpha premultiplied ?

		 useVBO: Use VBO for rendering

		 writeZTransparent: Write into Z Buffer for Transparent Object

		 alphaBlend: Enable alpha blending

		 depthTest: Enable depth testing

		 cullFace: Face culling (0 = no culling, 1 = cull back faces, 2 = cull front faces)

		 lineWidth: Line width (set if != 1, only for lines rendering)

		 pointSize: Point size (set if != 1, only for points rendering)

		 lineSmooth: Enable smooth line rendering

		 pointSmooth: Enable smooth point rendering

		 isToPrint: suppress somes data before using save as function

		 primitiveType: Select types of primitives to send (necessary for some shader types such as geometry or tesselation)

		 blendEquation: if alpha blending is enabled this specifies how source and destination colors are combined

		 sfactor: if alpha blending is enabled this specifies how the red, green, blue, and alpha source blending factors are computed

		 dfactor: if alpha blending is enabled this specifies how the red, green, blue, and alpha destination blending factors are computed

		 nb: number of input visual models to merge


    """
    return attachedTo.createObject("MergeVisualModels" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, position=position, restPosition=restPosition, normal=normal, initRestPositions=initRestPositions, useNormals=useNormals, updateNormals=updateNormals, computeTangents=computeTangents, updateTangents=updateTangents, handleDynamicTopology=handleDynamicTopology, fixMergedUVSeams=fixMergedUVSeams, keepLines=keepLines, vertices=vertices, texcoords=texcoords, tangents=tangents, bitangents=bitangents, edges=edges, triangles=triangles, quads=quads, vertPosIdx=vertPosIdx, vertNormIdx=vertNormIdx, fileMesh=fileMesh, texturename=texturename, translation=translation, rotation=rotation, scale3d=scale3d, scaleTex=scaleTex, translationTex=translationTex, material=material, putOnlyTexCoords=putOnlyTexCoords, srgbTexturing=srgbTexturing, materials=materials, groups=groups, blendTranslucency=blendTranslucency, premultipliedAlpha=premultipliedAlpha, useVBO=useVBO, writeZTransparent=writeZTransparent, alphaBlend=alphaBlend, depthTest=depthTest, cullFace=cullFace, lineWidth=lineWidth, pointSize=pointSize, lineSmooth=lineSmooth, pointSmooth=pointSmooth, isToPrint=isToPrint, primitiveType=primitiveType, blendEquation=blendEquation, sfactor=sfactor, dfactor=dfactor, nb=nb, **kwargs)
