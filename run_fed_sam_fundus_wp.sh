python ./train_fed_sam_wopretrain.py --data Fundus --unseen_site 0 --gpu 1 --batch_size 3 --exp Fundus-1e-4-0-wp --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" --num_classes 2 # 2>&1 | tee log.log
# python ./train_fed_sam_wopretrain.py --data Fundus --unseen_site 1 --gpu 1 --batch_size 3 --exp Fundus-1e-4-1-wp --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" --num_classes 2 # 2>&1 | tee log.log
python ./train_fed_sam_wopretrain.py --data Fundus --unseen_site 2 --gpu 1 --batch_size 3 --exp Fundus-1e-4-2-wp --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" --num_classes 2 # 2>&1 | tee log.log
# python ./train_fed_sam_wopretrain.py --data Fundus --unseen_site 3 --gpu 1 --batch_size 3 --exp Fundus-1e-4-3-wp --base_lr 1e-4 --sam_ckpt "/mnt/diskB/lyx/FedSAM/FedSAM/SAM/sam_vit_b_01ec64.pth" --num_classes 2 # 2>&1 | tee log.log