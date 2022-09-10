from tensorflow.keras import models, layers, utils, backend as K
import tensorflow as tf
import matplotlib.pyplot as plt
import shap

def binary_step_activation(x):
    return K.switch(x>0,tf.math.divide(x,x), tf.math.multiply(x,0))

model = models.Sequential(name="Perceptron", layers=[
    layers.Dense(
        name = "dense",
        input_dim = 3,
        units = 1,
        activation = binary_step_activation #'linear'
    )
])

model.summary()
