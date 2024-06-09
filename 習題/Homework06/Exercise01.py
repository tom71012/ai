import numpy as np
from micrograd.engine import Value

class CrossEntropyLoss:
    def __init__(self):
        pass

    def __call__(self, y_pred, y_true):
        # calculate cross entropy loss
        num_samples = y_pred.data.shape[0]
        # avoid numerical instability by adding epsilon
        epsilon = 1e-9
        loss = -(1/num_samples) * np.sum(y_true.data * np.log(y_pred.data + epsilon))
        return Value(loss)

# test
from keras.datasets import mnist
import keras

# load data
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = np.asarray(x_train, dtype=np.float32) / 255.0
x_test = np.asarray(x_test, dtype=np.float32) / 255.0
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

# initialize weights
W = Value(np.random.randn(784, 10))

# create loss layer
loss_layer = CrossEntropyLoss()

# train
batch_size = 32
steps = 20000
for step in range(steps):
    ri = np.random.permutation(x_train.shape[0])[:batch_size]
    Xb, yb = Value(x_train[ri]), Value(y_train[ri])
    y_pred = Xb.matmul(W).softmax()
    loss = loss_layer(y_pred, yb)
    loss.backward()
    W.data -= 0.01 * W.grad
    W.grad = 0
    if step % 1000 == 0:
        print(f"Step {step}: Loss {loss.data}")

# test
y_pred_test = Value(x_test).matmul(W).softmax()
accuracy = np.mean(np.argmax(y_pred_test.data, axis=1) == np.argmax(y_test, axis=1))
print(f"Accuracy on test data: {accuracy * 100:.2f}%")
