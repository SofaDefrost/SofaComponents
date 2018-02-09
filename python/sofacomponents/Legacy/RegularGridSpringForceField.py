# -*- coding: utf-8 -*-


"""
Component RegularGridSpringForceField

.. autofunction:: RegularGridSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def RegularGridSpringForceField(attachedTo , **kwargs):
    """Spring acting on the edges and faces of a regular grid


    Args:


    """
    return attachedTo.createObject("RegularGridSpringForceField" , **kwargs)
