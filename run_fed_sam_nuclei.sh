python ./train_fed_sam.py --data Nuclei --unseen_site 0 --gpu 3 --batch_size 4 --exp nuclei-new-0 --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" # 2>&1 | tee log.log
python ./train_fed_sam.py --data Nuclei --unseen_site 1 --gpu 3 --batch_size 4 --exp nuclei-new-1 --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" # 2>&1 | tee log.log
# python ./train_fed_sam.py --data Nuclei --unseen_site 2 --gpu 3 --batch_size 4 --exp nuclei-new-2 --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" # 2>&1 | tee log.log
# python ./train_fed_sam.py --data Nuclei --unseen_site 3 --gpu 3 --batch_size 4 --exp nuclei-new-3 --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" # 2>&1 | tee log.log
python ./train_fed_sam.py --data Nuclei --unseen_site 4 --gpu 3 --batch_size 4 --exp nuclei-new-4 --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" # 2>&1 | tee log.log
python ./train_fed_sam.py --data Nuclei --unseen_site 5 --gpu 3 --batch_size 4 --exp nuclei-new-5 --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" # 2>&1 | tee log.log
python ./train_fed_sam.py --data Nuclei --unseen_site 6 --gpu 3 --batch_size 4 --exp nuclei-new-6 --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" # 2>&1 | tee log.log