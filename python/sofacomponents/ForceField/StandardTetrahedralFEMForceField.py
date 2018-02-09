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

        
def StandardTetrahedralFEMForceField(attachedTo , name='StandardTetrahedralFEMForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, isCompliance=0, rayleighStiffness=0.0, materialName='ArrudaBoyce', ParameterSet=[], AnisotropyDirections=[], ParameterFile='myFile.param', tetrahedronInfo='', edgeInfo='', **kwargs):
    """Generic Tetrahedral finite elements


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

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
    return attachedTo.createObject("StandardTetrahedralFEMForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, materialName=materialName, ParameterSet=ParameterSet, AnisotropyDirections=AnisotropyDirections, ParameterFile=ParameterFile, tetrahedronInfo=tetrahedronInfo, edgeInfo=edgeInfo, **kwargs)
