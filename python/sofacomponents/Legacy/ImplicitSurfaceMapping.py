# -*- coding: utf-8 -*-


"""
Component ImplicitSurfaceMapping

.. autofunction:: ImplicitSurfaceMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def ImplicitSurfaceMapping(attachedTo , **kwargs):
    """Compute an iso-surface from a set of particles


    Args:


    """
    return attachedTo.createObject("ImplicitSurfaceMapping" , **kwargs)
