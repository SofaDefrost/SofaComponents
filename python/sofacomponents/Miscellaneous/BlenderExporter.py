# -*- coding: utf-8 -*-


"""
Component BlenderExporter

.. autofunction:: BlenderExporter

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def BlenderExporter(attachedTo , name='BlenderExporter', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=1, path='', baseName='', simulationType=0, step=2, nbPtsByHair=20, **kwargs):
    """Export the simulation result as blender point cache files


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 path: output path

		 baseName: Base name for the output files

		 simulationType: simulation type (0: soft body, 1: particles, 2:cloth, 3:hair)

		 step: save the  simulation result every step frames

		 nbPtsByHair: number of element by hair strand


    """
    return attachedTo.createObject("BlenderExporter" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, path=path, baseName=baseName, simulationType=simulationType, step=step, nbPtsByHair=nbPtsByHair, **kwargs)
