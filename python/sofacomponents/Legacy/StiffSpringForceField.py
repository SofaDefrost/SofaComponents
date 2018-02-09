# -*- coding: utf-8 -*-


"""
Component StiffSpringForceField

.. autofunction:: StiffSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def StiffSpringForceField(attachedTo , **kwargs):
    """Stiff springs for implicit integration


    Args:


    """
    return attachedTo.createObject("StiffSpringForceField" , **kwargs)
