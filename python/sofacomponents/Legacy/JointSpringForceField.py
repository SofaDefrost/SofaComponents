# -*- coding: utf-8 -*-


"""
Component JointSpringForceField

.. autofunction:: JointSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def JointSpringForceField(attachedTo , **kwargs):
    """Springs for Rigids


    Args:


    """
    return attachedTo.createObject("JointSpringForceField" , **kwargs)
