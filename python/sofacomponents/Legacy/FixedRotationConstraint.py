# -*- coding: utf-8 -*-


"""
Component FixedRotationConstraint

.. autofunction:: FixedRotationConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def FixedRotationConstraint(attachedTo , **kwargs):
    """Prevents rotation around x or/and y or/and z axis


    Args:


    """
    return attachedTo.createObject("FixedRotationConstraint" , **kwargs)
