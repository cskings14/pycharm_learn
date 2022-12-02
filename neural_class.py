import numpy as np

"""
We are now going to use batches.
Batches are the number of samples going through the network.
Batches help with generalization, speed of network training, and less memory.
Most batch sizes are 32.
"""

# inputs = [1, 2, 3, 2.5]   this is only one sample
#  Let's use a batch instead

input = [[1, 2, 3, 2.5],  # inputs is also 3 x 4
         [2.0, 5.0, -1.0, 2.0],
         [-1.5, 2.7, 3.3, -0.8]]

weight = [[0.2, 0.8, -0.5, 1.0],  # weights is 3 x 4
          [0.5, -0.91, 0.26, -0.5],
          [-0.26, -0.27, 0.17, 0.87]]

bias = [2, 3, 0.5]

# outputs = np.dot(weights, inputs) + biases
"""
# this would be a shape error
# Right now, it is trying to multiply input number left to right by
# weights up to down. This doesn't work because it is missing another row.
# We have to instead transpose the weights.
We need to change weights into a numpy array to transpose it.
"""
outputs = np.dot(input, np.array(weight).T) + bias

# print(outputs)

#  We are now going to add another layer

weights2 = [[0.1, -0.14, 0.5],  # weights is 3 x 4
            [-0.5, 0.12, -0.33],
            [-0.44, 0.73, -0.13]]

biases2 = [-1, 2, -0.5]

layer1_outputs = np.dot(input, np.array(weight).T) + bias

layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2

#

"""
We will now make a class
"""

# We will now make the hidden layers
# We don't really change hidden layers which is why it is called hidden

"""
To initialize weights, we will use random small numbers.
Most of the time, biases start out as 0.
"""
np.random.seed(0)
X = [[1, 2, 3, 2.5],  # It is called x to show a training data set
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):  # inputs and neurons are switched to not transpose every time
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


layer1 = Layer_Dense(4, 5)  # the first number of layer 2 has the be the same as the last number for layer 1.
layer2 = Layer_Dense(5, 2)

layer1.forward(X)
# print(layer1.output)
layer2.forward(layer1.output)

print(layer2.output)
