# -*- coding: utf-8 -*-


"""
Component StandardTetrahedralFEMForceField

.. autofunction:: StandardTetrahedralFEMForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def StandardTetrahedralFEMForceField(attachedTo , name='StandardTetrahedralFEMForceField', printLog=0, tags=[], bbox=array([[ 1.79769313e+308,  1.79769313e+308,  1.79769313e+308],
       [-1.79769313e+308, -1.79769313e+308, -1.79769313e+308]]), componentState='Undefined', listening=0, isCompliance=0, rayleighStiffness=0.0, materialName='ArrudaBoyce', ParameterSet=array([], dtype=float64), AnisotropyDirections=array([], shape=(0, 3), dtype=float64), ParameterFile='myFile.param', tetrahedronInfo=[], edgeInfo=[], **kwargs):
    """Generic Tetrahedral finite elements


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 componentState: The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 materialName: the name of the material to be used

		 ParameterSet: The global parameters specifying the material

		 AnisotropyDirections: The global directions of anisotropy of the material

		 ParameterFile: the name of the file describing the material parameters for all tetrahedra

		 tetrahedronInfo: Internal tetrahedron data

		 edgeInfo: Internal edge data


    """
    return attachedTo.createObject("StandardTetrahedralFEMForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, componentState=componentState, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, materialName=materialName, ParameterSet=ParameterSet, AnisotropyDirections=AnisotropyDirections, ParameterFile=ParameterFile, tetrahedronInfo=tetrahedronInfo, edgeInfo=edgeInfo, **kwargs)
