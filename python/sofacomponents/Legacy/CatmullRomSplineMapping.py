# -*- coding: utf-8 -*-


"""
Component CatmullRomSplineMapping

.. autofunction:: CatmullRomSplineMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def CatmullRomSplineMapping(attachedTo , **kwargs):
    """Map positions between points of a curve based on catmull-rom weights


    Args:


    """
    return attachedTo.createObject("CatmullRomSplineMapping" , **kwargs)
