import json

basePath = "/mnt/mouse/data"
nnPath = f"{basePath}/nnmouse/raw/Dataset001_mouse/"

nnjson = {
    "channel_names": {
        "0": "CT"
    },
    "labels": {
        "background": 0,
		"left lung": 1,
		"cranial lobe": 2,
		"middle lobe": 3,
		"caudal lobe": 4,
		"accessory lobe": 5,
		"left kidney": 6,
		"right kidney": 7,
		"stomach wall": 8,
		"stomach lumen": 9,
		"medial lobe of liver": 10,
		"left lobe of liver ": 11,
		"right lobe of liver": 12,
		"caudate lobe of liver": 13,
		"left adrenal": 14,
		"right adrenal": 15,
		"rectum": 16,
		"bladder": 17,
		"left ventricle": 18,
		"right ventricle": 19,
		"left thymic rudiment": 20,
		"right thymic rudiment": 21,
		"third ventricle": 22,
		"mesencephalic vesicle": 23,
		"fourth ventricle": 24,
		"cerebral aqueduct": 25,
		"left lateral ventricle": 26,
		"right lateral ventricle": 27,
		"right olfactory bulb": 28,
		"left olfacotory bulb": 29,
		"right thalamus ": 30,
		"left thalamus": 31,
		"right hypothamalus ": 32,
		"left hypothalmus": 33,
		"right septal area": 34,
		"left septal area": 35,
		"left neopallial cortex abd amygdala": 36,
		"right neopallial cortex and amygdala": 37,
		"right striatum": 38,
		"left striatum ": 39,
		"right ventricular zone": 40,
		"left ventricular zone": 41,
		"pons": 42,
		"left cerebellar primordium ": 43,
		"right cerebellar primordium": 44,
		"midbrain": 45,
		"medulla oblongata": 46,
		"spinal cord": 47,
		"vertebrae": 48,
		"left ventricle chamber": 49,
		"right ventricle chamber": 50,
    },
    "numTraining": 83,
    "file_ending": ".nii.gz"
}

fp = open(f"{nnPath}/dataset.json", "w")
fp.write(json.dumps(nnjson))
fp.close()
