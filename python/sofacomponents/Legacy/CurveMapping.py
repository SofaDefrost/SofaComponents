# -*- coding: utf-8 -*-


"""
Component CurveMapping

.. autofunction:: CurveMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def CurveMapping(attachedTo , **kwargs):
    """Mapping allowing one or more rigid objects follow a trajectory determined by a set of points


    Args:


    """
    return attachedTo.createObject("CurveMapping" , **kwargs)
