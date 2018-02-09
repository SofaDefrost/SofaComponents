# -*- coding: utf-8 -*-


"""
Component LCPForceFeedback

.. autofunction:: LCPForceFeedback

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def LCPForceFeedback(attachedTo , **kwargs):
    """LCP force feedback for the device


    Args:


    """
    return attachedTo.createObject("LCPForceFeedback" , **kwargs)
