# -*- coding: utf-8 -*-


"""
Component AngularSpringForceField

.. autofunction:: AngularSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def AngularSpringForceField(attachedTo , **kwargs):
    """Angular springs applied to rotational degrees of freedom of a rigid body or frame


    Args:


    """
    return attachedTo.createObject("AngularSpringForceField" , **kwargs)
