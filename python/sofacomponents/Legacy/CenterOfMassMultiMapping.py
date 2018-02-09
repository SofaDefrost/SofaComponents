# -*- coding: utf-8 -*-


"""
Component CenterOfMassMultiMapping

.. autofunction:: CenterOfMassMultiMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def CenterOfMassMultiMapping(attachedTo , **kwargs):
    """Set the point to the center of mass of the DOFs it is attached to


    Args:


    """
    return attachedTo.createObject("CenterOfMassMultiMapping" , **kwargs)
