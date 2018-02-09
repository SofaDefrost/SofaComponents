# -*- coding: utf-8 -*-


"""
Component TCylinderModel

.. autofunction:: TCylinderModel

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TCylinderModel(attachedTo , **kwargs):
    """Collision model which represents a set of rigid cylinders


    Args:


    """
    return attachedTo.createObject("TCylinderModel" , **kwargs)
