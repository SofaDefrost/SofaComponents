# -*- coding: utf-8 -*-


"""
Component VisualModelImpl

.. autofunction:: VisualModelImpl

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def VisualModelImpl(attachedTo , name='VisualModelImpl', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, position=array([], shape=(0, 3), dtype=float64), restPosition=array([], shape=(0, 3), dtype=float64), normal=array([], shape=(0, 3), dtype=float64), initRestPositions=0, useNormals=1, updateNormals=1, computeTangents=0, updateTangents=1, handleDynamicTopology=1, fixMergedUVSeams=1, keepLines=0, vertices=array([], shape=(0, 3), dtype=float64), texcoords=array([], shape=(0, 2), dtype=float32), tangents=array([], shape=(0, 3), dtype=float64), bitangents=array([], shape=(0, 3), dtype=float64), edges=array([], shape=(0, 2), dtype=int32), triangles=array([], shape=(0, 3), dtype=int32), quads=array([], shape=(0, 4), dtype=int32), vertPosIdx=array([], dtype=int32), vertNormIdx=array([], dtype=int32), filename='', texturename='', translation=array([0., 0., 0.]), rotation=array([0., 0., 0.]), scale3d=array([1., 1., 1.]), scaleTex=array([1., 1.], dtype=float32), translationTex=array([0., 0.], dtype=float32), material='Default Diffuse 1 0.75 0.75 0.75 1 Ambient 1 0.2 0.2 0.2 1 Specular 0 1 1 1 1 Emissive 0 0 0 0 0 Shininess 0 45 ', putOnlyTexCoords=0, srgbTexturing=0, materials=[], groups=[], **kwargs):
    """Generic visual model. If a viewer is active it will replace the VisualModel alias, otherwise nothing will be displayed.


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

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

		 filename:  Path to an ogl model

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


    """
    return attachedTo.createObject("VisualModelImpl" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, position=position, restPosition=restPosition, normal=normal, initRestPositions=initRestPositions, useNormals=useNormals, updateNormals=updateNormals, computeTangents=computeTangents, updateTangents=updateTangents, handleDynamicTopology=handleDynamicTopology, fixMergedUVSeams=fixMergedUVSeams, keepLines=keepLines, vertices=vertices, texcoords=texcoords, tangents=tangents, bitangents=bitangents, edges=edges, triangles=triangles, quads=quads, vertPosIdx=vertPosIdx, vertNormIdx=vertNormIdx, filename=filename, texturename=texturename, translation=translation, rotation=rotation, scale3d=scale3d, scaleTex=scaleTex, translationTex=translationTex, material=material, putOnlyTexCoords=putOnlyTexCoords, srgbTexturing=srgbTexturing, materials=materials, groups=groups, **kwargs)
