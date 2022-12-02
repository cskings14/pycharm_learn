#  Each neuron has a unique connection to every single previous neuron
#  If there are 4 neurons feeding into the neuron that we are building,
#  There outputs will be the neuron that we are building's inputs
"""
O  \
O - 0 (neuron that we are building)
O  /
O  |
"""
inputs = [1, 2, 3, 2.5]  # all of these are random numbers

weights = [0.2, 0.8, -0.5, 1.0]  # each input has a weight

bias = 2  # each neuron has a bias

output1 = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + inputs[3] * weights[3] + bias

#  The first step for a neuron is to the inputs times their weights + the bias
print(output1)











# Now, we are going to make 3 neurons from 4 inputs

# inputs2 = [1, 2, 3, 2.5]  # There is still the 4 same outputs

# weights1 = [0.2, 0.8, -0.5, 1.0]  # each neuron will have 3 unique weights connected to it
# weights2 = [0.5, -0.91, 0.26, -0.5]
# weights3 = [-0.26, -0.27, 0.17, 0.87]
#
# bias1 = 2  # each neuron will have its own bias
# bias2 = 3
# bias3 = 0.5
#
# output2 = [
#     inputs2[0] * weights1[0] + inputs2[1] * weights1[1] + inputs2[2] * weights1[2] + inputs2[3] * weights1[3] + bias1,
#     inputs2[0] * weights2[0] + inputs2[1] * weights2[1] + inputs2[2] * weights2[2] + inputs2[3] * weights2[3] + bias2,
#     inputs2[0] * weights3[0] + inputs2[1] * weights3[1] + inputs2[2] * weights3[2] + inputs2[3] * weights3[3] + bias3]
#
# print(output2)
#  To get the desired outputs, we can't change the inputs (that are from other hidden layers).
#  We have to change the weights and the biases to get better desired inputs.














# Now, lets simplify the code


# inputss = inputs2 = [1, 2, 3, 2.5]
#
# weightss = [[0.2, 0.8, -0.5, 1.0],
#             [0.5, -0.91, 0.26, -0.5],
#             [-0.26, -0.27, 0.17, 0.87]]
#
# biases = [2, 3, 0.5]

# layer_outputs = [] #  Output of current layer
# for neuron_weights, neuron_bias in zip(weightss, biases):
#     neuron_output = 0  #  Output of given neuron
#     for n_input, weight in zip(inputss, neuron_weights):
#         neuron_output += n_input*weight
#     neuron_output += neuron_bias
#     layer_outputs.append(neuron_output)

# print(layer_outputs)


















# we are now going to actually use numpy

import numpy as np


inputss = inputs2 = [1, 2, 3, 2.5]

weightss = [[0.2, 0.8, -0.5, 1.0], #  weightss is a matrix of 3 vectors
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

outputss = np.dot(weightss, inputss) + biases
print(outputss)
#  weightss has to go first in order for it to work






