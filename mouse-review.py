import glob
import os

BASE="/mnt/mouse/data/nnmouse"

imagesTr=f"{BASE}/raw/Dataset001_mouse/imagesTr"
labelsTr=f"{BASE}/raw/Dataset001_mouse/labelsTr"
resultsPath=f"{BASE}/results/Dataset001_mouse/nnUNetTrainer__nnUNetPlans__3d_fullres/fold_0/validation"

resultIndex = 0
labelNode = None
resultNode = None
volumeNode = None
resultPaths = glob.glob(f"{resultsPath}/*.nii.gz")

def load():
    global resultIndex, labelNode, volumeNode, resultNode, resultPaths
    for node in [labelNode, volumeNode, resultNode]:
        if node:
            slicer.mrmlScene.RemoveNode(node)
    resultPath = resultPaths[resultIndex]
    resultIndex += 1
    print(resultPath)
    resultNode = slicer.util.loadSegmentation(resultPath)
    labelFileName = resultPath.split("/")[-1]
    labelNode = slicer.util.loadSegmentation(f"{labelsTr}/{labelFileName}")
    subjectID = labelFileName[:-1*len(".nii.gz")]
    volumeFileName = f"{os.path.split(resultPath)[-1].split('.')[0]}_0000.nrrd"
    volumeNode = slicer.util.loadVolume(f"{imagesTr}/{subjectID}_0000.nii.gz", properties={"singleFile": True})
    #slicer.modules.volumes.logic().ApplyVolumeDisplayPreset(volumeNode.GetVolumeDisplayNode(), "CT_ABDOMEN")
    resultNode.GetDisplayNode().SetAllSegmentsOpacity2DFill(1.0)
    resultNode.GetDisplayNode().SetAllSegmentsOpacity2DOutline(0.0)
    labelNode.GetDisplayNode().SetAllSegmentsOpacity2DFill(0.0)
    labelNode.GetDisplayNode().SetAllSegmentsOpacity2DOutline(1.0)
    labelNode.GetDisplayNode().SetSliceIntersectionThickness(3)

button = qt.QPushButton("Next")
button.connect("clicked()", load)
button.show()

load()
