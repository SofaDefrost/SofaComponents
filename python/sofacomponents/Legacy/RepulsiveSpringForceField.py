# -*- coding: utf-8 -*-


"""
Component RepulsiveSpringForceField

.. autofunction:: RepulsiveSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def RepulsiveSpringForceField(attachedTo , **kwargs):
    """Springs which only repell


    Args:


    """
    return attachedTo.createObject("RepulsiveSpringForceField" , **kwargs)
