import tensorflow as tf
import os
import skimage
import numpy as np
import matplotlib.pyplot as plt



def load_data(data_directoriy):
    directories = [d for d in os.listdir(data_directoriy) if os.path.isdir(os.path.join(data_directoriy, d))]
    labels = []
    images = []

    for d in directories:
        label_directory = os.path.join(data_directoriy, d)
        file_names = [os.path.join(label_directory, f) for f in os.listdir(label_directory) if f.endswith(".ppm")]
        for f in file_names:
            images.append(skimage.data.imread(f))
            labels.append(int(d))
    return images, labels


if __name__ == '__main__':
    train_data_directory = os.path.join("", "belgium_ts/Training")
    test_data_directory = os.path.join("", "belgium_ts/Testing")
    images, labels = load_data(train_data_directory)
    images = np.asarray(images)
    labels = np.asarray(labels)

    # Make a histogram with 62 bins of the `labels` data
    plt.hist(labels, 62)
    plt.show()
