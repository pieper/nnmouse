#!/bin/bash

BASE=/mnt/mouse/data/nnmouse

export nnUNet_raw=${BASE}/raw
export nnUNet_preprocessed=${BASE}/preprocessed
export nnUNet_results=${BASE}/results

case "$1" in
	"")
		echo usage "nntrain.sh [plan | train]"
		exit 1;;
	"plan")
		echo plan
		nnUNetv2_plan_and_preprocess -d 001 --verify_dataset_integrity;;
	"train")
		echo train
		nnUNetv2_train 1 3d_fullres 0 -device cuda
		nnUNetv2_train 1 3d_fullres 1 -device cuda
		nnUNetv2_train 1 3d_fullres 2 -device cuda
		nnUNetv2_train 1 3d_fullres 3 -device cuda
		nnUNetv2_train 1 3d_fullres 4 -device cuda;;
	*)
		echo "command not known: $1";;
esac
