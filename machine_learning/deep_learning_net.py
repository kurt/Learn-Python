from tensorflow.keras import models, layers, utils, backend as K
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
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

utils.plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True)


# Optimizing the DNN
# define metrics
def Recall(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

def Precision(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

def F1(y_true, y_pred):
    precision = Precision(y_true, y_pred)
    recall = Recall(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall+K.epsilon()))

# compile the neural network
model.compile(optimizer='adam', loss='binary_crossentropy',
              metrics=['accuracy',F1])

## Data to train on

X = np.random.rand(1000,10)
y = np.random.choice([1,0], size=1000)


# train/validation
training = model.fit(x=X, y=y, batch_size=32, epochs=100, shuffle=True, verbose=0, validation_split=0.3)

# plot
metrics = [k for k in training.history.keys() if ("loss" not in k) and ("val" not in k)]
fig, ax = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(15,3))

# training
ax[0].set(title="Training")
ax11 = ax[0].twinx()
ax[0].plot(training.history['loss'], color='black')
ax[0].set_xlabel('Epochs')
ax[0].set_ylabel('Loss', color='black')
for metric in metrics:
    ax11.plot(training.history[metric], label=metric)
    ax11.set_ylabel("Score", color='steelblue')
ax11.legend()

# validation
ax[1].set(title="Validation")
ax22 = ax[1].twinx()
ax[1].plot(training.history['val_loss'], color='black')
ax[1].set_xlabel('Epochs')
ax[1].set_ylabel('Loss', color='black')
for metric in metrics:
    ax22.plot(training.history['val_'+metric], label=metric)
    ax22.set_ylabel("Score", color="steelblue")
plt.show()


def explainer_shap(model, x_names, x_instance, x_train=None, task="classification",top=10):
    if x_train is None:
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(x_instance)

    else:
        explainer = shap.DeepExplainer(model, data=x_train[:100])
        shap_values = explainer.shap_values(x_instance.reshape(1,-2))[0].reshape(-1)

    if task == "classification":
        shap.decision_plot(explainer.expected_value, shap_values, link='logit', feature_order='importance',
                           features=x_instance, feature_names=x_names, feature_display_range=slice(-1,-top-1,-1))
    #regression
    else:
        shap.waterfall_plot(explainer.expected_value[0], shap_values,
                            features=x_instance, feature_names=x_names, max_display=top)


list_feature_names = ["Hi", "Bye"]
i = 1
explainer_shap(model,
               x_names=list_feature_names,
               x_instance=X[i],
               x_train=X,
               task="classification", #task="regression"
               top=10)
