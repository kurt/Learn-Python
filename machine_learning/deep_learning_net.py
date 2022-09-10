from tensorflow.keras import models, layers, utils, backend as K
import tensorflow as tf
import matplotlib.pyplot as plt
import shap


n_features = 10

model = models.Sequential(name="DeepNN", layers=[
    #hidden layer 1
    layers.Dense(name="h1", input_dim = n_features,
    units = int(round((n_features+1)/2)),
    activation = 'relu'),
    layers.Dropout(name = "drop1", rate = 0.2),

    #hidden layer 2
    layers.Dense(name = "h2", units = int(round((n_features+1)/4)),
    activation = 'relu'),
    layers.Dropout(name = "drop2", rate = 0.2),

    #layer output
    layers.Dense(name = "output", units = 1, activation = 'sigmoid')
])

model.summary()
