# -*- coding: utf-8 -*-


"""
Component VectorSpringForceField

.. autofunction:: VectorSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def VectorSpringForceField(attachedTo , **kwargs):
    """Spring force field acting along the edges of a mesh


    Args:


    """
    return attachedTo.createObject("VectorSpringForceField" , **kwargs)
