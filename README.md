# FedSAM

## Introdcution

A framework for fine-tuning SAM (Segment Anything) in the federated learning paradigm for medical image segmentation, called **FedSAM**.

## Requirements

* Python==3.8.16

* torch==2.0.0

* torchvision==0.15.0

* numpy==1.24.3

* opencv_python==4.7.0.72

See the detail requirements in [requirements.txt](./requirements.txt)

## Model Training and Test

run [./run_fed_sam_FeTS.sh](./run_fed_sam_FeTS.sh) for federated learning in FeTS2022 Dataset (Brain Tumor).

run [./run_fed_sam_fundus.sh](./run_fed_sam_fundus.sh) for federated learning in Fundus Dataset.

run [./run_fed_sam_nuclei.sh](./run_fed_sam_nuclei.sh) for federated learning in Nuclei Dataset.

run [./run_fed_sam_prostate.sh](./run_fed_sam_prostate.sh) for federated learning in Prostate Cancer Dataset.

run [./run_fed_sam_ctlung.sh](./run_fed_sam_ctlung.sh) for  federated learning in Lung Dataset.
