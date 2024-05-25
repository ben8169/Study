# Please write your name and student ID
__author__ = "Machine Learning"
__id__ = "2022000000"

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')



class my_MLP():
    def __init__(self):
        """
        This function does not need to be modified.
        """

        self.author = __author__
        self.id = __id__

        self.lr = 0.01
        self.neurons = 32
        self.N_hidden = 1
        self.batch_size = 8
        self.epochs = 20
        self.hidden_layers = []
        self.weights = []
        self.N_class = None
        

    def sigmoid(self, x):
        """
        Implement the sigmoid function for the given x.
        Note: You cannot use the Python math package. Only use numpy for this implementation.
        """

        return None # Problem 1: Implement the sigmoid function.


    def softmax(self, x):
        """
        Implement the softmax function for the given x.
        Note: You cannot use the Python math package. Only use numpy for this implementation.
        """
        
        return None # Problem 2: Implement the softmax function.


    def prime_sigmoid(self, x):
        """
        This function does not need to be modified.

        This function computes the derivative of the sigmoid function for the given x.
        """
        
        return x * (1 - x)


    def feed_forward(self, X_train):
        """
        Perform the forward propagation on the given X_train.
        For the current hidden layer information, compute the sigmoid of the product of the hidden layer weights and the input.
        Write the contents of the for loop to carry out this process.
        """

        hidden_layer = X_train # The first hidden layer information is the X_train value.
        self.hidden_layers[0] = hidden_layer # Store the X_train value as the first hidden layer.

        for i, weights in enumerate(self.weights):
            pass # Problem 3: Write the contents of the for loop.

        output = self.softmax(self.hidden_layers[-1]) # Apply softmax to the final layer to obtain the final output.
        return output

        
    def back_propagation(self, output, y_onehot):
        """
        Perform the backpropagation using the forward propagation results, output, and the true labels, y_onehot.
        
        Write the contents of the for loop to carry out this process.
        """
        
        delta_t = (output - y_onehot) * self.prime_sigmoid(self.hidden_layers[-1])

        for i in range(1, len(self.weights)+1):
            self.weights[-i] -= None
            delta_t = None

            # Problem 4: Write the contents of the for loop.

                # self.weights
                    # 1) Calculate the gradient of the cost function by computing the product of the previous hidden layer and delta_t.
                    # 2) Update the weights by subtracting the product of the computed gradient and the learning rate from the existing weights.

                # delta
                    # 3) Compute the product of the updated weights and delta_t.
                    # 4) Update delta_t by computing the product of the prime sigmoid value of the previous hidden layer and the final value from step 3.
            
            

    def fit(self, X_train, y_train):
        """
        This function does not need to be modified.

        This function trains the MLP model using the given training data X_train and y_train.
        """

        self.N_class = len(np.unique(y_train)) # Set the number of classes to classify
        y_onehot = np.eye(self.N_class)[y_train] # Convert y_train information to one-hot encoding

        # List containing the size information of the training layers: [input layer size, hidden layer size (number of neurons * number of layers), output layer size]
        total_layer_size = np.array([X_train.shape[1]] + [self.neurons]*self.N_hidden + [y_onehot.shape[1]])
        self.hidden_layers = [np.empty((self.batch_size, layer)) for layer in total_layer_size] # List to store the training layer information
        
        # Assign initial random weights
        self.weights = list()
        for i in range(total_layer_size.shape[0]-1): # Generate weights between all layers
            self.weights.append(np.random.uniform(-1,1,size=[total_layer_size[i], total_layer_size[i+1]]))
        self.weights = np.array(self.weights, dtype=object)

        # Repeat training for the number of epochs
        for epoch in range(self.epochs):
            shuffle = np.random.permutation(X_train.shape[0]) # Generate random training data indices
            X_batches = np.array_split(X_train[shuffle], X_train.shape[0]/self.batch_size) # Create X batch
            y_batches = np.array_split(y_onehot[shuffle], X_train.shape[0]/self.batch_size) # Create y batch
            
            for x_batch, y_batch in zip(X_batches, y_batches):
                output = self.feed_forward(x_batch) # Forward propagation step
                self.back_propagation(output, y_batch) # Backward propagation step (including cost function calculation from the lecture notes)


    def predict(self, X_test):
        """
        This function does not need to be modified.

        This function computes the predicted values y_pred for the evaluation data X_test based on the trained weights.
        """

        # List containing the size information of the evaluation layers
        test_layer_size = np.array([X_test.shape[1]] + [self.neurons]*self.N_hidden + [self.N_class])
        self.hidden_layers = [np.empty((X_test.shape[0], layer)) for layer in test_layer_size] # List to store the evaluation layer information

        output = self.feed_forward(X_test) # Forward propagation
        y_pred = output.argmax(axis=1) # Final predicted values

        return y_pred

    


















