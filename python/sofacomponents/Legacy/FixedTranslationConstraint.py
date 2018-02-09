# -*- coding: utf-8 -*-


"""
Component FixedTranslationConstraint

.. autofunction:: FixedTranslationConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def FixedTranslationConstraint(attachedTo , **kwargs):
    """Attach given rigids to their initial positions but they still can have rotations


    Args:


    """
    return attachedTo.createObject("FixedTranslationConstraint" , **kwargs)
