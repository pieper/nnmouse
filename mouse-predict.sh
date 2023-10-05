#!/bin/bash

BASE=/mnt/mouse/data/nnmouse

export nnUNet_raw=${BASE}/raw
export nnUNet_preprocessed=${BASE}/preprocessed
export nnUNet_results=${BASE}/results

DATA=${BASE}/sample-data-nnmouse
time nnUNetv2_predict -i ${DATA} -o ${DATA} -d 1 -c 3d_fullres --save_probabilities

