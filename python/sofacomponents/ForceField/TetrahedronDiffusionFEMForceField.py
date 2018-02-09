# -*- coding: utf-8 -*-


"""
Component TetrahedronDiffusionFEMForceField

.. autofunction:: TetrahedronDiffusionFEMForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TetrahedronDiffusionFEMForceField(attachedTo , name='TetrahedronDiffusionFEMForceField', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, isCompliance=0, rayleighStiffness=0.0, constantDiffusionCoefficient=1.0, tetraDiffusionCoefficient=[], scalarDiffusion=0, anisotropyRatio=1.0, transverseAnisotropyArray=[], tagMechanics='meca', drawConduc=0, **kwargs):
    """Isotropic or anisotropic diffusion on Tetrahedral Meshes


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 isCompliance: Consider the component as a compliance, else as a stiffness

		 rayleighStiffness: Rayleigh damping - stiffness matrix coefficient

		 constantDiffusionCoefficient: Constant diffusion coefficient

		 tetraDiffusionCoefficient: Diffusion coefficient for each tetrahedron, by default equal to constantDiffusionCoefficient.

		 scalarDiffusion: if true, diffuse only on the first dimension.

		 anisotropyRatio: Anisotropy ratio (r²>1).
 Default is 1.0 = isotropy.

		 transverseAnisotropyArray: Data to handle topology on tetrahedra

		 tagMechanics: Tag of the Mechanical Object.

		 drawConduc: To display conductivity map.


    """
    return attachedTo.createObject("TetrahedronDiffusionFEMForceField" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, isCompliance=isCompliance, rayleighStiffness=rayleighStiffness, constantDiffusionCoefficient=constantDiffusionCoefficient, tetraDiffusionCoefficient=tetraDiffusionCoefficient, scalarDiffusion=scalarDiffusion, anisotropyRatio=anisotropyRatio, transverseAnisotropyArray=transverseAnisotropyArray, tagMechanics=tagMechanics, drawConduc=drawConduc, **kwargs)
