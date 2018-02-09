# -*- coding: utf-8 -*-


"""
Component SkinningMapping

.. autofunction:: SkinningMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def SkinningMapping(attachedTo , **kwargs):
    """skin a model from a set of rigid dofs


    Args:


    """
    return attachedTo.createObject("SkinningMapping" , **kwargs)
