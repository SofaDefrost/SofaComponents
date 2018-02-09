# -*- coding: utf-8 -*-


"""
Component CenterOfMassMapping

.. autofunction:: CenterOfMassMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def CenterOfMassMapping(attachedTo , **kwargs):
    """Set the point to the center of mass of the DOFs it is attached to


    Args:


    """
    return attachedTo.createObject("CenterOfMassMapping" , **kwargs)
