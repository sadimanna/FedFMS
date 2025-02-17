﻿# FedFMS

## 😆 Introdcution

Develop federated foundation models for medical image segmentation.

(1) A framework for fine-tuning all the parameters of SAM ([Segment Anything Model](https://github.com/facebookresearch/segment-anything)) in the federated learning paradigm for medical image segmentation, called **FedSAM**.

(2) A framework for fine-tuning MSA ([Medical SAM Adapter](https://github.com/KidsWithTokens/Medical-SAM-Adapter)) in the federated learning paradigm for medical image segmentation, called **FedMSA**.

Welcome to read our paper, which provides detailed descriptions of the methods and experimental results:
[FedFMS: Exploring Federated Foundation Models for Medical Image Segmentation](https://arxiv.org/abs/2403.05408)

> **FedFMS: Exploring Federated Foundation Models for Medical Image Segmentation**  
> Yuxi Liu, Guibo Luo\*, Yuesheng Zhu\*
> *MICCAI2024*

## 🌟 Citation

If you find this work is helpful to your research, please consider citing our paper:

```bibtex
@inproceedings{liu2024fedfms,
  title={Fedfms: Exploring federated foundation models for medical image segmentation},
  author={Liu, Yuxi and Luo, Guibo and Zhu, Yuesheng},
  booktitle={International Conference on Medical Image Computing and Computer-Assisted Intervention},
  pages={283--293},
  year={2024},
  organization={Springer}
}
```

**Thanks for your interest in our work!**

## 📝 Requirements

* Python==3.8.16

* torch==2.0.0

* torchvision==0.15.0

* numpy==1.24.3

* opencv_python==4.7.0.72

See the detail requirements in [requirements.txt](./requirements.txt)

## 🚀 Model Training and Test

#### run FedSAM

run [./run_ft/run_fed_sam_FeTS_ft.sh](./run_ft/run_fed_sam_FeTS_ft.sh) for federated learning in FeTS2022 Dataset (Brain Tumor).

run [./run_ft/run_fed_sam_fundus_ft.sh](./run_ft/run_fed_sam_fundus_ft.sh) for federated learning in Fundus Dataset.

run [./run_ft/run_fed_sam_nuclei_ft.sh](./run_ft/run_fed_sam_nuclei_ft.sh) for federated learning in Nuclei Dataset.

run [./run_ft/run_fed_sam_prostate_ft.sh](./run_ft/run_fed_sam_prostate_ft.sh) for federated learning in Prostate Cancer Dataset.

run [./run_ft/run_fed_sam_ctlung_ft.sh](./run_ft/run_fed_sam_ctlung_ft.sh) for  federated learning in Lung Dataset.

#### run FedMSA

run [./run_fed_sam_FeTS.sh](./run_fed_sam_FeTS.sh) for federated learning in FeTS2022 Dataset (Brain Tumor).

run [./run_fed_sam_fundus.sh](./run_fed_sam_fundus.sh) for federated learning in Fundus Dataset.

run [./run_fed_sam_nuclei.sh](./run_fed_sam_nuclei.sh) for federated learning in Nuclei Dataset.

run [./run_fed_sam_prostate.sh](./run_fed_sam_prostate.sh) for federated learning in Prostate Cancer Dataset.

run [./run_fed_sam_ctlung.sh](./run_fed_sam_ctlung.sh) for  federated learning in Lung Dataset.

## 📚 Data sources

#### FeTS2022 Dataset

[Federated Tumor Segmentation Challenge | FeTS Challenge 2021 (fets-ai.github.io)](https://fets-ai.github.io/Challenge/)

#### Fundus Dataset

[REFUGE Challenge Dataset | Papers With Code](https://paperswithcode.com/dataset/refuge-challenge)

[Glaucoma Fundus Imaging Datasets | Kaggle](https://www.kaggle.com/datasets/arnavjain1/glaucoma-datasets)

[Drishti-GS - RETINA DATASET FOR ONH SEGMENTATION (kaggle.com)](https://www.kaggle.com/datasets/lokeshsaipureddi/drishtigs-retina-dataset-for-onh-segmentation)

#### Nuclei Dataset

[Prostate cANcer graDe Assessment (PANDA) Challenge | Kaggle](https://www.kaggle.com/competitions/prostate-cancer-grade-assessment/discussion/146364)

[MoNuSAC-2020 - Home (biomedicalimaging.org)](https://biomedicalimaging.org/2020/wp-content/uploads/static-html-to-wp/data/dff0d41695bbae509355435cd32ecf5d/index-26.htm)

[TNBC_dataset | Kaggle](https://www.kaggle.com/datasets/shahed7/tnbc-dataset)

[MonuSeg-2018 | Kaggle](https://www.kaggle.com/datasets/tuanledinh/monuseg2018)

#### Prostate Cancer Dataset

[Evaluation of prostate segmentation algorithms for MRI: The PROMISE12 challenge - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1361841513001734)

[Initiative for Collaborative Computer Vision Benchmarking (i2cvb.github.io)](https://i2cvb.github.io/)

[NCI-ISBI 2013 Challenge - Automated Segmentation of Prostate Structures - The Cancer Imaging Archive (TCIA) Public Access - Cancer Imaging Archive Wiki](https://wiki.cancerimagingarchive.net/display/Public/NCI-ISBI+2013+Challenge+-+Automated+Segmentation+of+Prostate+Structures)

#### Lung Dataset

[CT Lung &amp; Heart &amp; Trachea segmentation | Kaggle](https://www.kaggle.com/sandorkonya/ct-lung-heart-trachea-segmentation)
