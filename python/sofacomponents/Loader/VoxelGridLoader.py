# -*- coding: utf-8 -*-


"""
Component VoxelGridLoader

.. autofunction:: VoxelGridLoader

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

        
def VoxelGridLoader(attachedTo , name='VoxelGridLoader', printLog=0, tags=[], bbox='1.79769e+308 1.79769e+308 1.79769e+308 -1.79769e+308 -1.79769e+308 -1.79769e+308', listening=0, filename='', position=[], hexahedra=[], voxelSize=[[1.0, 1.0, 1.0]], resolution=[[0, 0, 0]], ROI=[[0, 0, 0, 65535, 65535, 65535]], header=0, segmentationHeader=0, idxInRegularGrid=[], bgValue=[], dataValue=[], generateHexa=1, **kwargs):
    """Voxel loader based on RAW files


    Args:

		 name: object name

		 printLog: if true, emits extra messages at runtime.

		 tags: list of the subsets the objet belongs to

		 bbox: this object bounding box

		 listening: if true, handle the events, otherwise ignore the events

		 filename: Filename of the object

		 position: Coordinates of the nodes loaded

		 hexahedra: Hexahedra loaded

		 voxelSize: Dimension of one voxel

		 resolution: Resolution of the voxel file

		 ROI: Region of interest (xmin, ymin, zmin, xmax, ymax, zmax)

		 header: Header size in bytes

		 segmentationHeader: Header size in bytes

		 idxInRegularGrid: indices of the hexa in the grid.

		 bgValue: Background values (to be ignored)

		 dataValue: Active data values

		 generateHexa: Interpret voxel as either hexa or points


    """
    return attachedTo.createObject("VoxelGridLoader" , name=name, printLog=printLog, tags=tags, bbox=bbox, listening=listening, filename=filename, position=position, hexahedra=hexahedra, voxelSize=voxelSize, resolution=resolution, ROI=ROI, header=header, segmentationHeader=segmentationHeader, idxInRegularGrid=idxInRegularGrid, bgValue=bgValue, dataValue=dataValue, generateHexa=generateHexa, **kwargs)
