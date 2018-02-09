# -*- coding: utf-8 -*-


"""
Component RigidMapping

.. autofunction:: RigidMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def RigidMapping(attachedTo , **kwargs):
    """Set the positions and velocities of points attached to a rigid parent


    Args:


    """
    return attachedTo.createObject("RigidMapping" , **kwargs)
