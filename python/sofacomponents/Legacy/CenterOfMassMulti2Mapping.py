# -*- coding: utf-8 -*-


"""
Component CenterOfMassMulti2Mapping

.. autofunction:: CenterOfMassMulti2Mapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def CenterOfMassMulti2Mapping(attachedTo , **kwargs):
    """Set the point to the center of mass of the DOFs it is attached to


    Args:


    """
    return attachedTo.createObject("CenterOfMassMulti2Mapping" , **kwargs)
