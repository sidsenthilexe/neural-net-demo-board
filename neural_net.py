import tensorflow as tf
print('tf version ', tf.__version__)
gpu = tf.config.list_physical_devices('GPU')

if gpu :
    print('gpu')
print(tf.config.list_physical_devices)
