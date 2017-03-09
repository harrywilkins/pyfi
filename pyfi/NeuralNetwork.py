import random

#   (Input Neuron)-----(synapse 0)-----\
#                                      |
#   (Input Neuron)-----(synapse 1)---(Output Neuron)
#                                      |
#   (Input Neuron)-----(synapse 2)-----/

class NeuralNetwork(): #Author Aidan Horton

    def __init__(self):
        #Input training data - not using numpy
        self.x = [[0, 0, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]]

        #The actual outputs of the X data
        self.y = [[0],
                  [0],
                  [1],
                  [1]]

        #Create synapses with a random weight between -1 and 1
        self.synapses = [[random.uniform(-1, 1)],
                         [random.uniform(-1, 1)],
                         [random.uniform(-1, 1)]]

    def Iterate(self):
        for i in range(10000):
            layer1 = self.x

            #Multiply matrix 'layer1' by 'synapses'
            #Pass output through 'Sigmoid' function

            #[x is (4 x 3)] * [synapses is (3 x 1)]
            #Resulting matrix is (4 x 1) - assign to 'layer2'
            layer2 = [[0],
                      [0],
                      [0],
                      [0]]

            #The amount of error betwen the prediction and the actual value
            layer2Error = self.y - layer1

            #This reduces the error in higher confidence predictions
            layer2Delta = layer2_error * Sigmoid(layer2, True)

            #Update the weights - Fix this to multiply matrices
            for index in range(len(self.synapses)):
                self.synapses[index] += layer1 * layer2Delta

    def MatrixMultiply(matrix1, matrix2):

    def Sigmoid(self, x, deriv = False): #Sigmoid function
        #X might be a list, so may need to alter this
        if deriv:
            return x * (1 - x)
        return 1 / (1 + exp(-x))
