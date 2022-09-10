from tensorflow.keras import models, layers, utils, backend as K
import matplotlib.pyplot as plt
import shap


model = models.Sequential(name="Perceptron", layers=[
    layers.Dense(
        name = "dense",
        input_dim = 3,
        units = 1,
        activation = 'linear'
    )
])

model.summary()
