import os
import sys
import argparse
import cv2
import yaml
import map
import urllib.parse as urlparse
import urllib
from io import StringIO
import numpy as np
from PIL import Image
import tensorflow as tf
from hed.utils.io import IO
from hed.models.vgg16 import Vgg16

class Hed_test():
    def start(self,img_path,txt_path,args = os.getcwd() + "/hed/configs/hed.yaml"):
        io = IO()
        self.cfgs = io.read_yaml_file(args)
        self.model = Vgg16(self.cfgs, run='testing')
        meta_model_file = "hed/models/hed-model-5000"
        saver = tf.train.Saver()
        session = self.get_session()
        saver.restore(session, meta_model_file)
        self.model.setup_testing(session)
        im = self.fetch_img(img_path)
        edgemap = session.run(self.model.predictions, feed_dict={self.model.images: [im]})
        self.save_egdemaps(edgemap,txt_path)


    def fetch_img(self,img_path):

        image = None
        image = Image.open(img_path)
        image = image.resize((self.cfgs['testing']['image_width'], self.cfgs['testing']['image_height']))
        image = np.array(image, np.float32)
        image = self.colorize(image)
        image = image[:, :, self.cfgs['channel_swap']]
        image -= self.cfgs['mean_pixel_value']
        return image


    def colorize(self, image):

        if image.ndim == 2:
            image = image[:, :, np.newaxis]
            image = np.tile(image, (1, 1, 3))
        elif image.shape[2] == 4:
            image = image[:, :, :3]

        return image

    def get_session(self):

        config = tf.ConfigProto(device_count = {'GPU': 0})
        sess = tf.Session(config=config)
        return sess;
        # num_threads = int(1)
        # gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=gpu_fraction)
        #
        # if num_threads:
        #     return tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, intra_op_parallelism_threads=num_threads))
        # else:
        #     return tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

    def save_egdemaps(self, em_maps, txt_path):

        # Take the edge map from the network from side layers and fuse layer
        em_maps = [e[0] for e in em_maps]
        em_maps = em_maps + [np.mean(np.array(em_maps), axis=0)]
        count = 1
        for idx, em in enumerate(em_maps):


            em[em < self.cfgs['testing_threshold']] = 0.0

            em = 255.0 * (1.0 - em)
            em = np.tile(em, [1, 1, 3])

            em = Image.fromarray(np.uint8(em))
            if(count == 1):
                cv_image = cv2.cvtColor(np.array(em), cv2.COLOR_RGB2BGR)
                self.generate_braille_text_image(cv_image,txt_path)
                break
            count+=1

    def generate_braille_text_image(self,image,txt_path):

        height, width = image.shape[:2]
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        res = cv2.resize(img_gray,None,fx=(76/width), fy=(75/height), interpolation = cv2.INTER_CUBIC)
        (thresh, im_bw) = cv2.threshold(res, 110, 255, cv2.THRESH_BINARY)

        hm,wm = res.shape

        fo = open(txt_path, "w",encoding="utf-8")

        for i in range(2,hm,3):
            for j in range(1,wm,2):
                cell = (im_bw[i-2][j-1],im_bw[i-1][j-1],im_bw[i][j-1],im_bw[i-2][j],im_bw[i-1][j],im_bw[i][j])
                fo.write(chr(map.map[cell]))
            fo.write("\n")

        fo.close()

# if __name__ == '__main__':
#     a = Hed_test()
#     a.start("/Users/adityachandra/Documents/SIH_Braille_files/neuron.jpg","/Users/adityachandra/Desktop/android.txt","hed/configs/hed.yaml")
