# -*- coding: utf-8 -*-


"""
Component RigidRigidMapping

.. autofunction:: RigidRigidMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def RigidRigidMapping(attachedTo , **kwargs):
    """Set the positions and velocities of points attached to a rigid parent


    Args:


    """
    return attachedTo.createObject("RigidRigidMapping" , **kwargs)
