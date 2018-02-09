# -*- coding: utf-8 -*-


"""
Component DefaultPipeline

.. autofunction:: DefaultPipeline

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def DefaultPipeline(attachedTo , name='DefaultPipeline', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, verbose=0, draw=0, depth=6, **kwargs):
    """The default collision detection and modeling pipeline


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 verbose: Display extra informations at each computation step. (default=false)

		 draw: Draw the detected collisions. (default=false)

		 depth: Max depth of bounding trees. (default=6, min=?, max=?)


    """
    return attachedTo.createObject("DefaultPipeline" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, verbose=verbose, draw=draw, depth=depth, **kwargs)
