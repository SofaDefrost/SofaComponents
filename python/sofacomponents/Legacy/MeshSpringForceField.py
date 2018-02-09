# -*- coding: utf-8 -*-


"""
Component MeshSpringForceField

.. autofunction:: MeshSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def MeshSpringForceField(attachedTo , **kwargs):
    """Spring force field acting along the edges of a mesh


    Args:


    """
    return attachedTo.createObject("MeshSpringForceField" , **kwargs)
