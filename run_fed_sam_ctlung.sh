python ./train_fed_sam.py --data CTLung --unseen_site 0 --gpu 0 --batch_size 4 --exp CTLung-new-0 --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" 
python ./train_fed_sam.py --data CTLung --unseen_site 1 --gpu 0 --batch_size 4 --exp CTLung-new-1 --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" # 2>&1 | tee log.log
python ./train_fed_sam.py --data CTLung --unseen_site 2 --gpu 0 --batch_size 4 --exp CTLung-new-2 --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" # 2>&1 | tee log.log
python ./train_fed_sam.py --data CTLung --unseen_site 3 --gpu 0 --batch_size 4 --exp CTLung-new-3 --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" # 2>&1 | tee log.log
python ./train_fed_sam.py --data CTLung --unseen_site 4 --gpu 0 --batch_size 4 --exp CTLung-new-4 --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" # 2>&1 | tee log.log