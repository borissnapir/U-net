import numpy as np
import utils.utils as utils
import tensorflow as tf

class DataGenerator:
    def __init__(self, config):
        self.config = config
        # load data here
        filenames = utils.get_files("../../data/oxford_iiit_pet/raw/images", extensions=(".jpg"))
        labels = utils.get_files("../../data/oxford_iiit_pet/raw/annotations/trimaps", extensions=(".png"))
        self.filenames = filenames
        self.labels = labels

        
    @tf.function
    def parse_function(self, filename, label):
        image_string = tf.io.read_file(filename)
        image = tf.image.decode_jpeg(image_string, channels=3)
        # This will convert to float values in [0, 1]
        image = tf.image.convert_image_dtype(image, tf.float32)
        image = tf.image.resize(image, [256, 256])

        mask_string = tf.io.read_file(label)
        mask = tf.image.decode_png(mask_string, channels=1)
        mask = tf.cast(mask, tf.float32)
        mask = tf.image.resize(mask, [256, 256])
        mask = tf.math.round(mask)
        # original mask is between 1 and 3, make it between 0 and 2
        mask = tf.subtract(mask, 1)
        return image, mask

    @tf.function
    def train_preprocess(self, image, mask):
        seed = 42
        # some random augmentations
        image = tf.image.random_flip_left_right(image, seed=seed)
        image = tf.image.random_brightness(image, max_delta=32.0 / 255.0, seed=seed)
        image = tf.image.random_saturation(image, lower=0.5, upper=1.5, seed=seed)
        # Make sure the image is still in [0, 1]
        image = tf.clip_by_value(image, 0.0, 1.0)

        mask = tf.image.random_flip_left_right(mask, seed=seed)
        return image, mask

    def get_dataset(self, batch_size):
        # prepare dataset
        dataset = tf.data.Dataset.from_tensor_slices((self.filenames, self.labels))
        dataset = dataset.shuffle(len(self.filenames))
        dataset = dataset.map(self.parse_function, num_parallel_calls=4)
        dataset = dataset.map(self.train_preprocess, num_parallel_calls=4)
        dataset = dataset.batch(batch_size)
        dataset = dataset.prefetch(1)
        return dataset
