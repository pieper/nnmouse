#
# "left ventricle chamber": 102, -> 49
# "right ventricle chamber": 103, -> 50
#

import glob
import numpy

nnPath = f"{basePath}/nnmouse/raw/Dataset001_mouse/"
labelPath = f"{nnPath}/labelsTr"

for labelFile in glob.glob(f"{labelPath}/*.nii.gz"):
    labelNode = slicer.util.loadVolume(labelFile)
    labelArray = slicer.util.arrayFromVolume(labelNode)
    labelArray[labelArray == 102] = 49
    labelArray[labelArray == 103] = 50
    slicer.util.arrayFromVolumeModified(labelNode)
    slicer.util.saveNode(labelNode, labelFile)
    slicer.mrmlScene.RemoveNode(labelNode)

