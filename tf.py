import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

samples = 1000
dataset = np.zeros((samples, 5))

dataset[:, 0:3] = np.random.randint(0,2, (samples, 3))
dataset[:, 3] = np.random.uniform(0,1, samples)
dataset[:, 4] = np.random.uniform(0,1, samples)

labels = np.random.randint(0,4, samples)

dataset_train, dataset_test, labels_train, labels_test = train_test_split(dataset, labels, test_size=0.2, random_state=42)

lb = LabelBinarizer()
labels_train = lb.fit_transform(labels_train)
labels_test = lb.transform(labels_test)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
])

predictions = model(dataset_train[:1]).numpy()
print(predictions)
predictions = tf.nn.softmax(predictions).numpy()
print(predictions)