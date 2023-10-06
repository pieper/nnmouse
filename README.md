# nnmouse
Sample scripts for training nnU-Net on mouse fetus data

## Background
This is an experiment to use [nnU-Net](https://github.com/MIC-DKFZ/nnUNet/tree/master) for segmenting mouse embryo scans for comparison to [MEMOS](https://github.com/SlicerMorph/SlicerMEMOS).

Model was trained on the `mouse_fetus` data from here: http://bit.ly/monai

## Prerequisites
Install nnU-Net version 2 as described on their web site.  I used miniconda on a Ubuntu machine.

## Processing scripts
Creation of the model used the following helper scripts running in [3D Slicer version 5.4.0](https://slicer.org).  The Python code was just pasted into the python console.  The training shell script was run in bash.  Paths need to be adjusted based on where you keep the data.

mouse-prep.py	: converts the naming convention for compatibility with nnU-Net requirements.

mouse-remap.py : ensures that the labelmaps indices are sequentially numbered, which is a requirement for nnU-Net.

mouse-json.py : builds the required json file to describe the segmentation process.

mouse-train.sh : used for planning and training.  First run `bash mouse-train.sh plan` which takes several minutes, then `bash mouse-train.sh train` which will take several days to train 5 folds of the model depending on your CPU and GPU configuration (tested on a 16 core A100 GPU with 20GB and training time is about 1.5 days per fold).

mouse-review.py : creates a simple interface to load and review data from fold 0 in 3D Slicer.

mouse-predict.sh : shows how to run the trained model on a new dataset.


## Preliminary results for one fold

In 2D the ground truth is outline and the fill is the model.  
![image](https://github.com/pieper/nnmouse/assets/126077/b9f466db-8f9e-45ed-9bfc-683e79170a55)

For the 3D view the ground truth is on the left and the model results are on the right.

![image](https://github.com/pieper/nnmouse/assets/126077/140415b3-7206-4a0f-83e2-1e14d9d8d929)

# More information

Slides presenting some of this work and other models trained using the same approach are [available here](https://docs.google.com/presentation/d/1zlTCcGPwYRzuZnXhJ3RHJ7_AQM4Nr8aU8Me1A6TQJjM/edit#slide=id.p1).  This material was prepared as part of the [SlicerMorph Train the Trainers 2023 event](https://discourse.slicer.org/t/slicermorph-train-the-trainers-event/30998).
