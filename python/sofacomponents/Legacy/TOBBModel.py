# -*- coding: utf-8 -*-


"""
Component TOBBModel

.. autofunction:: TOBBModel

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def TOBBModel(attachedTo , **kwargs):
    """Collision model which represents a set of OBBs


    Args:


    """
    return attachedTo.createObject("TOBBModel" , **kwargs)
