import os
import torch
import numpy as np
from glob import glob
from torch.utils.data import Dataset
import h5py
import itertools
from torch.utils.data.sampler import Sampler
import random 
from scipy import ndimage
from scipy.ndimage import _ni_support
from scipy.ndimage.morphology import distance_transform_edt, binary_erosion,\
    generate_binary_structure
import cv2
from PIL import Image
# print("当前路径:", current_path)
from sam_utils import random_click,show_element
from torchvision import transforms
current_path = os.getcwd()
class ProstateDataset(Dataset):
    """ LA Dataset """
    def __init__(self,data_path=None, client_idx=None, freq_site_idx=None, split='train', transform=None, client_name=None):
        self.transform = transform
        self.client_name = ['BIDMC', 'HK', 'I2CVB', 'ISBI', 'ISBI_1.5', 'UCL'] if client_name is None else client_name 
        self.freq_list_clients = []
        if split=='train':
            data_path = data_path if data_path is not None else '/mnt/diskB/lyx/Prostate_processed_1024'
            self.image_list = glob('{}/{}/data_npy/*'.format(data_path,self.client_name[client_idx]))
            self.label_dir='{}/{}/label_npy'.format(data_path,self.client_name[client_idx])
            '''
            for i in range(len(self.client_name)):
                freq_list = glob('{}/{}/freq_amp_npy/*'.format(data_path,self.client_name[i]))
                length = len(freq_list)
                freq_list = random.sample(freq_list, int(length/8))
                self.freq_list_clients.append(freq_list)
            '''
        self.freq_site_index = freq_site_idx

        print("total {} slices".format(len(self.image_list)))

    def __len__(self):
        return len(self.image_list)
    def __getitem__(self, idx):
        raw_file = self.image_list[idx]
        
        mask_patches = []

        image_patch = np.load(raw_file)
        file_name = os.path.basename(raw_file)
        label_path = os.path.join(self.label_dir,file_name)
        mask_patch = np.load(label_path)

        mask =  np.squeeze(mask_patch)
        # print(mask.shape)
        newsize = (image_patch.shape[1],image_patch.shape[1])
        # print(newsize)
        # 只能(256,256)去resize,不能(256，256，1)
        mask=cv2.resize(mask, newsize, interpolation=cv2.INTER_NEAREST)
        # mask_patch = mask_patch.resize(newsize)
        # print('mask',mask_patch,mask_patch.size)
        inout = 1
        point_label = 1
        # print(list(np.array(mask)))
        pt = random_click(np.array(mask), point_label, inout)# np.expand_dims(random_click(np.array(mask), point_label, inout), axis=0)
        # mask =  np.squeeze(mask_patch)
        # print('pt',pt)
        # print('raw_inp',raw_inp.shape,np.transpose(raw_inp,(2,0,1)).shape)
        # 将numpy数组转换为PIL图像
        # pil_image = Image.fromarray(np.transpose(raw_inp,(2,0,1)))
        # print(pil_image.shape)
        # 重新调整图像大小为 (1024, 1024)
        # resized_image = pil_image.resize((1024, 1024))

        # 将PIL图像转换回numpy数组
        # raw_inp = np.transpose(np.array(resized_image),(2,0,1))
        # print('raw_inp',raw_inp.shape)
        # image_patch = raw_inp[..., 0:3]
        # mask_patch = raw_inp[..., 3:]
        '''
        # 将图像数据转换为PIL图像对象
        image_patch = Image.fromarray(image_patch.astype('uint8'))
        # 调整图像大小为 [1024, 1024, 3]
        resized_image = image_patch.resize((1024, 1024))
        # 将PIL图像对象转换为numpy数组
        image_patch = np.array(resized_image)
        print(image_patch.size,mask_patch.size)
        '''
        # image_patch=cv2.resize(image_patch, (1024,1024), interpolation=cv2.INTER_LINEAR)
        # mask_patch=cv2.resize(mask_patch, (1024,1024), interpolation=cv2.INTER_NEAREST)
        # image_patch = self.resize(image_patch,(1024,1024))
        # mask_patch = self.resize(mask_patch,(1024,1024))
        image_patches = image_patch.copy()

        # image_patches = 
        # print (image_patch.dtype)
        # print (mask_patch.dtype)
        '''
        disc_contour, disc_bg, cup_contour, cup_bg = _get_coutour_sample(mask_patch)
        # print ('raw', np.min(image_patch), np.max(image_patch))
        for tar_freq_domain in np.random.choice(self.freq_site_index, 2):
            tar_freq = np.random.choice(self.freq_list_clients[tar_freq_domain])
            tar_freq = np.load(tar_freq).transpose(2, 0, 1)
            # print('tar_freq',tar_freq.shape)
            # L1 = random.randint(2,5)/1000.0
            image_patch_freq_1 = source_to_target_freq(image_patch, tar_freq[...], L=0)
            image_patch_freq_1 = np.clip(image_patch_freq_1, 0, 255)
            # print (image_patch_freq_1.dtype)
            # print ('trans', np.min(image_patch_freq_1), np.max(image_patch_freq_1))
            image_patches = np.concatenate([image_patches,image_patch_freq_1], axis=-1)
        '''
        image_patches = image_patches.transpose(2, 0, 1)
        mask_patches = mask_patch.transpose(2, 0, 1)
        # contour_bg_mask = np.concatenate(contour_bg_mask, axis=-1)
        sample = {"image": image_patches.astype(np.float32)/ 255.0, "label": mask_patches.astype(np.float32), "pt":pt}
        
        return sample
class Dataset(Dataset):
    """ LA Dataset """
    def __init__(self,data_path=None, client_idx=None, freq_site_idx=None, split='train', transform=None, client_name=None):
        self.transform = transform
        self.client_name = ['1', '4', '5', '6', '13', '16', '18', '20', '21'] if client_name is None else client_name 
        self.freq_list_clients = []
        if split=='train':
            data_path = data_path if data_path is not None else '/mnt/diskB/lyx/FeTS2022_FedDG_1024'
            self.image_list = glob('{}/{}/data_npy/*'.format(data_path,self.client_name[client_idx]))
            self.label_dir='{}/{}/label_npy'.format(data_path,self.client_name[client_idx])
            '''
            for i in range(len(self.client_name)):
                freq_list = glob('{}/{}/freq_amp_npy/*'.format(data_path,self.client_name[i]))
                length = len(freq_list)
                freq_list = random.sample(freq_list, int(length/8))
                self.freq_list_clients.append(freq_list)
            '''
        self.freq_site_index = freq_site_idx
        self.client_idx=client_idx
        print("total {} slices".format(len(self.image_list)))

    def __len__(self):
        return len(self.image_list)
    def __getitem__(self, idx):
        raw_file = self.image_list[idx]
        
        mask_patches = []

        image_patch = np.load(raw_file)
        file_name = os.path.basename(raw_file)
        label_path = os.path.join(self.label_dir,file_name)
        mask_patch = np.load(label_path)
        
        # mask =  np.squeeze(mask_patch)
        # print(mask.shape)
        newsize = (image_patch.shape[1],image_patch.shape[1])
        # print(newsize)
        # new_mask=[]
        # for i in range(mask.shape[-1]):
        #    new_mask.append(np.array(cv2.resize(mask, newsize, interpolation=cv2.INTER_NEAREST)))
        mask = mask_patch[:,:,0]
        # save mask
        '''
        mask_show= mask.copy()
        mask_show[mask_show==1]=255
        image = Image.fromarray(mask_show)
        image.save("../output/output-{}.jpg".format(self.client_name[self.client_idx]))
        '''
        mask=cv2.resize(mask, newsize, interpolation=cv2.INTER_NEAREST)
        # mask_patch = mask_patch.resize(newsize)
        # print('mask',mask_patch.size)
        inout = 1
        point_label = 1
        # print(list(np.array(mask)))
        pt = random_click(np.array(mask), point_label, inout)# np.expand_dims(random_click(np.array(mask), point_label, inout), axis=0)
        # print('pt',pt)
        # print('raw_inp',raw_inp.shape,np.transpose(raw_inp,(2,0,1)).shape)
        # 将numpy数组转换为PIL图像
        # pil_image = Image.fromarray(np.transpose(raw_inp,(2,0,1)))
        # print(pil_image.shape)
        # 重新调整图像大小为 (1024, 1024)
        # resized_image = pil_image.resize((1024, 1024))

        # 将PIL图像转换回numpy数组
        # raw_inp = np.transpose(np.array(resized_image),(2,0,1))
        # print('raw_inp',raw_inp.shape)
        # image_patch = raw_inp[..., 0:3]
        # mask_patch = raw_inp[..., 3:]
        '''
        # 将图像数据转换为PIL图像对象
        image_patch = Image.fromarray(image_patch.astype('uint8'))
        # 调整图像大小为 [1024, 1024, 3]
        resized_image = image_patch.resize((1024, 1024))
        # 将PIL图像对象转换为numpy数组
        image_patch = np.array(resized_image)
        print(image_patch.size,mask_patch.size)
        '''
        # image_patch=cv2.resize(image_patch, (1024,1024), interpolation=cv2.INTER_LINEAR)
        # mask_patch=cv2.resize(mask_patch, (1024,1024), interpolation=cv2.INTER_NEAREST)
        # image_patch = self.resize(image_patch,(1024,1024))
        # mask_patch = self.resize(mask_patch,(1024,1024))
        image_patches = image_patch.copy()

        # image_patches = 
        # print (image_patch.dtype)
        # print (mask_patch.dtype)
        '''
        disc_contour, disc_bg, cup_contour, cup_bg = _get_coutour_sample(mask_patch)
        # print ('raw', np.min(image_patch), np.max(image_patch))
        for tar_freq_domain in np.random.choice(self.freq_site_index, 2):
            tar_freq = np.random.choice(self.freq_list_clients[tar_freq_domain])
            tar_freq = np.load(tar_freq).transpose(2, 0, 1)
            # print('tar_freq',tar_freq.shape)
            # L1 = random.randint(2,5)/1000.0
            image_patch_freq_1 = source_to_target_freq(image_patch, tar_freq[...], L=0)
            image_patch_freq_1 = np.clip(image_patch_freq_1, 0, 255)
            # print (image_patch_freq_1.dtype)
            # print ('trans', np.min(image_patch_freq_1), np.max(image_patch_freq_1))
            image_patches = np.concatenate([image_patches,image_patch_freq_1], axis=-1)
        '''
        image_patches = image_patches.transpose(2, 0, 1)
        mask_patches = mask_patch.transpose(2, 0, 1)
        # show_element(mask_patches)
        # print(mask_patches.shape,image_patches.shape)
        # contour_bg_mask = np.concatenate(contour_bg_mask, axis=-1)
        return image_patches.astype(np.float32)/ 255.0, mask_patches.astype(np.float32), pt
    def save_one_npy(self,save_path):
        all_image,all_label,all_pt=np.array([]),np.array([]),np.array([])
        for idx in range(self.__len__()):
            image,label,pt=self.__getitem__(idx)
            all_image=np.append(all_image, image)
            all_label=np.append(all_label, label)
            all_pt=np.append(all_pt, pt)
            if idx%200==0:
                print(idx)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        np.save(os.path.join(save_path,'images.npy'),all_image)
        np.save(os.path.join(save_path,'labels.npy'),all_label)
        np.save(os.path.join(save_path,'pts.npy'),all_pt)

class CenterCrop(object):
    def __init__(self, output_size):
        self.output_size = output_size

    def __call__(self, sample):
        image, label = sample['image'], sample['label']

        # pad the sample if necessary
        if label.shape[0] <= self.output_size[0] or label.shape[1] <= self.output_size[1] or label.shape[2] <= \
                self.output_size[2]:
            pw = max((self.output_size[0] - label.shape[0]) // 2 + 3, 0)
            ph = max((self.output_size[1] - label.shape[1]) // 2 + 3, 0)
            pd = max((self.output_size[2] - label.shape[2]) // 2 + 3, 0)
            image = np.pad(image, [(pw, pw), (ph, ph), (pd, pd)], mode='constant', constant_values=0)
            label = np.pad(label, [(pw, pw), (ph, ph), (pd, pd)], mode='constant', constant_values=0)

        (w, h, d) = image.shape

        w1 = int(round((w - self.output_size[0]) / 2.))
        h1 = int(round((h - self.output_size[1]) / 2.))
        d1 = int(round((d - self.output_size[2]) / 2.))

        label = label[w1:w1 + self.output_size[0], h1:h1 + self.output_size[1], d1:d1 + self.output_size[2]]
        image = image[w1:w1 + self.output_size[0], h1:h1 + self.output_size[1], d1:d1 + self.output_size[2]]

        return {'image': image, 'label': label}


class RandomCrop(object):
    """
    Crop randomly the image in a sample
    Args:
    output_size (int): Desired output size
    """

    def __init__(self, output_size):
        self.output_size = output_size

    def __call__(self, sample):
        image, label = sample['image'], sample['label']

        # pad the sample if necessary
        if label.shape[0] <= self.output_size[0] or label.shape[1] <= self.output_size[1] or label.shape[2] <= \
                self.output_size[2]:
            pw = max((self.output_size[0] - label.shape[0]) // 2 + 3, 0)
            ph = max((self.output_size[1] - label.shape[1]) // 2 + 3, 0)
            pd = max((self.output_size[2] - label.shape[2]) // 2 + 3, 0)
            image = np.pad(image, [(pw, pw), (ph, ph), (pd, pd)], mode='constant', constant_values=0)
            label = np.pad(label, [(pw, pw), (ph, ph), (pd, pd)], mode='constant', constant_values=0)

        (w, h, d) = image.shape
        # if np.random.uniform() > 0.33:
        #     w1 = np.random.randint((w - self.output_size[0])//4, 3*(w - self.output_size[0])//4)
        #     h1 = np.random.randint((h - self.output_size[1])//4, 3*(h - self.output_size[1])//4)
        # else:
        w1 = np.random.randint(0, w - self.output_size[0])
        h1 = np.random.randint(0, h - self.output_size[1])
        d1 = np.random.randint(0, d - self.output_size[2])

        label = label[w1:w1 + self.output_size[0], h1:h1 + self.output_size[1], d1:d1 + self.output_size[2]]
        image = image[w1:w1 + self.output_size[0], h1:h1 + self.output_size[1], d1:d1 + self.output_size[2]]
        return {'image': image, 'label': label}


class RandomRotFlip(object):
    """
    Crop randomly flip the dataset in a sample
    Args:
    output_size (int): Desired output size
    """

    def __call__(self, sample):
        image, label = sample['image'], sample['label']
        k = np.random.randint(0, 4)
        image = np.rot90(image, k)
        label = np.rot90(label, k)
        axis = np.random.randint(0, 2)
        image = np.flip(image, axis=axis).copy()
        label = np.flip(label, axis=axis).copy()

        return {'image': image, 'label': label}


class RandomNoise(object):
    def __init__(self, mu=0, sigma=0.1):
        self.mu = mu
        self.sigma = sigma

    def __call__(self, sample):
        image, label = sample['image'], sample['label']
        noise = np.clip(self.sigma * np.random.randn(image.shape[0], image.shape[1], image.shape[2]), -2*self.sigma, 2*self.sigma)
        noise = noise + self.mu
        image = image + noise
        return {'image': image, 'label': label}


class CreateOnehotLabel(object):
    def __init__(self, num_classes):
        self.num_classes = num_classes

    def __call__(self, sample):
        image, label = sample['image'], sample['label']
        onehot_label = np.zeros((self.num_classes, label.shape[0], label.shape[1], label.shape[2]), dtype=np.float32)
        for i in range(self.num_classes):
            onehot_label[i, :, :, :] = (label == i).astype(np.float32)
        return {'image': image, 'label': label,'onehot_label':onehot_label}


class ToTensor(object):
    """Convert ndarrays in sample to Tensors."""

    def __call__(self, sample):
        image = sample['image']
        image = image.reshape(1, image.shape[0], image.shape[1], image.shape[2]).astype(np.float32)
        if 'onehot_label' in sample:
            return {'image': torch.from_numpy(image), 'label': torch.from_numpy(sample['label']).long(),
                    'onehot_label': torch.from_numpy(sample['onehot_label']).long()}
        else:
            return {'image': torch.from_numpy(image), 'label': torch.from_numpy(sample['label']).long()}


class TwoStreamBatchSampler(Sampler):
    """Iterate two sets of indices

    An 'epoch' is one iteration through the primary indices.
    During the epoch, the secondary indices are iterated through
    as many times as needed.
    """
    def __init__(self, primary_indices, secondary_indices, batch_size, secondary_batch_size):
        self.primary_indices = primary_indices
        self.secondary_indices = secondary_indices
        self.secondary_batch_size = secondary_batch_size
        self.primary_batch_size = batch_size - secondary_batch_size

        assert len(self.primary_indices) >= self.primary_batch_size > 0
        assert len(self.secondary_indices) >= self.secondary_batch_size > 0

    def __iter__(self):
        primary_iter = iterate_once(self.primary_indices)
        secondary_iter = iterate_eternally(self.secondary_indices)
        return (
            primary_batch + secondary_batch
            for (primary_batch, secondary_batch)
            in zip(grouper(primary_iter, self.primary_batch_size),
                    grouper(secondary_iter, self.secondary_batch_size))
        )

    def __len__(self):
        return len(self.primary_indices) // self.primary_batch_size

def iterate_once(iterable):
    return np.random.permutation(iterable)


def iterate_eternally(indices):
    def infinite_shuffles():
        while True:
            yield np.random.permutation(indices)
    return itertools.chain.from_iterable(infinite_shuffles())


def grouper(iterable, n):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3) --> ABC DEF"
    args = [iter(iterable)] * n
    return zip(*args)

def low_freq_mutate_np( amp_src, amp_trg, L=0.1 ):
    a_src = np.fft.fftshift( amp_src, axes=(-2, -1) )
    a_trg = np.fft.fftshift( amp_trg, axes=(-2, -1) )

    _, h, w = a_src.shape
    b = (  np.floor(np.amin((h,w))*L)  ).astype(int)
    c_h = np.floor(h/2.0).astype(int)
    c_w = np.floor(w/2.0).astype(int)
    # print (b)
    h1 = c_h-b
    h2 = c_h+b+1
    w1 = c_w-b
    w2 = c_w+b+1

    ratio = random.randint(1,10)/10
    # print('a_src,a_trg',a_src.shape,a_trg.shape)
    # return a_src
    a_src[:,h1:h2,w1:w2] = a_trg[:,h1:h2,w1:w2]
    # a_src[:,h1:h2,w1:w2] = a_src[:,h1:h2,w1:w2] * ratio + a_trg[:,h1:h2,w1:w2] * (1- ratio)
    # a_src[:,h1:h2,w1:w2] = a_trg[:,h1:h2,w1:w2]
    a_src = np.fft.ifftshift( a_src, axes=(-2, -1) )
    # a_trg[:,h1:h2,w1:w2] = a_src[:,h1:h2,w1:w2]
    # a_trg = np.fft.ifftshift( a_trg, axes=(-2, -1) )
    return a_src
    
def source_to_target_freq( src_img, amp_trg, L=0.1 ):
    # exchange magnitude
    # input: src_img, trg_img
    src_img = src_img.transpose((2, 0, 1))
    src_img_np = src_img #.cpu().numpy()
    fft_src_np = np.fft.fft2( src_img_np, axes=(-2, -1) )

    # extract amplitude and phase of both ffts
    amp_src, pha_src = np.abs(fft_src_np), np.angle(fft_src_np)

    # mutate the amplitude part of source with target
    amp_src_ = low_freq_mutate_np( amp_src, amp_trg, L=L )

    # mutated fft of source
    fft_src_ = amp_src_ * np.exp( 1j * pha_src )

    # get the mutated image
    src_in_trg = np.fft.ifft2( fft_src_, axes=(-2, -1) )
    src_in_trg = np.real(src_in_trg)

    return src_in_trg.transpose(1, 2, 0)

client_name = ['1', '4', '5', '6', '13', '16', '18', '20', '21']
data_path = '/mnt/diskB/lyx/FeTS2022_FedDG_1024'
save_path = '/mnt/diskB/lyx/FeTS2022_FedDG_1024_npy'
client_num = len(client_name)
source_site_idx = [i for i in range(client_num)]
freq_site_idx = source_site_idx.copy()
for client_idx in range(client_num):
    dataset = Dataset(client_idx=client_idx, data_path=data_path,freq_site_idx=freq_site_idx,
                    split='train', transform = transforms.Compose([
                    ToTensor(),
                    ]),client_name=client_name)
    dataset.save_one_npy(os.path.join(save_path,str(client_idx)))