# -*- coding: utf-8 -*-


"""
Component BeamLinearMapping

.. autofunction:: BeamLinearMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BeamLinearMapping(attachedTo , **kwargs):
    """Set the positions and velocities of points attached to a beam using linear interpolation between DOFs


    Args:


    """
    return attachedTo.createObject("BeamLinearMapping" , **kwargs)
