# -*- coding: utf-8 -*-


"""
Component PenalityContactForceField

.. autofunction:: PenalityContactForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def PenalityContactForceField(attachedTo , **kwargs):
    """Contact using repulsive springs


    Args:


    """
    return attachedTo.createObject("PenalityContactForceField" , **kwargs)
