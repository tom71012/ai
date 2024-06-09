import numpy as np
from micrograd.engine import Value

class SimpleMLP:
    def __init__(self, input_size, hidden_size1, hidden_size2, output_size):
        self.W1 = Value(np.random.randn(input_size, hidden_size1))
        self.b1 = Value(np.zeros(hidden_size1))
        self.W2 = Value(np.random.randn(hidden_size1, hidden_size2))
        self.b2 = Value(np.zeros(hidden_size2))
        self.W3 = Value(np.random.randn(hidden_size2, output_size))
        self.b3 = Value(np.zeros(output_size))

    def forward(self, x):
        h1 = x.matmul(self.W1) + self.b1
        h1_relu = h1.relu()
        h2 = h1_relu.matmul(self.W2) + self.b2
        h2_relu = h2.relu()
        output = h2_relu.matmul(self.W3) + self.b3
        return output.softmax()

# 訓練和測試
from keras.datasets import mnist
import keras

# 載入數據集
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = np.asarray(x_train, dtype=np.float32) / 255.0
x_test = np.asarray(x_test, dtype=np.float32) / 255.0
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

# 初始化模型
model = SimpleMLP(input_size=784, hidden_size1=128, hidden_size2=64, output_size=10)

# 定義損失函數
loss_layer = CrossEntropyLoss()

# 訓練模型
batch_size = 32
steps = 20000
for step in range(steps):
    ri = np.random.permutation(x_train.shape[0])[:batch_size]
    Xb, yb = Value(x_train[ri]), Value(y_train[ri])
    y_pred = model.forward(Xb)
    loss = loss_layer(y_pred, yb)
    loss.backward()
    for p in [model.W1, model.b1, model.W2, model.b2, model.W3, model.b3]:
        p.data -= 0.01 * p.grad
        p.grad = 0
    if step % 1000 == 0:
        print(f"Step {step}: Loss {loss.data}")

# 測試模型
y_pred_test = model.forward(Value(x_test))
accuracy = np.mean(np.argmax(y_pred_test.data, axis=1) == np.argmax(y_test, axis=1))
print(f"Accuracy on test data: {accuracy * 100:.2f}%")
