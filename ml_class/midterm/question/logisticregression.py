# Write your name and student ID
__author__ = "김지헌"
__id__ = "2022313356"

# Do not import and other Python libraries
import numpy as np


class LogisticRegression:
    def __init__(self, max_iter=500, penalty="l2", initialize = "one", random_seed = 1213):
        """
        This function doesn't need to be modified.
        """
        
        self.author = __author__
        self.id = __id__
        
        self.max_iter = max_iter
        self.penalty = penalty
        self.initialize = initialize
        self.random_seed = random_seed
        self.lr = 0.1
        self.lamb = 0.01
        np.random.seed(self.random_seed)

        if self.penalty not in ["l1", "l2"]:
            raise ValueError("Penalty must be l1 or l2")

        if self.initialize not in ["one", "LeCun", "random"]:
            raise ValueError("Only [LeCun, One, random] Initialization supported")

            
    def activation(self, z):
        """
        Calcuates sigmoid activation function of the input.
        """

        # Q1. Calculate the sigmoid activation function [1 point]
        a = 1/1+np.exp(-z)

        return a


    def fwpass(self, x):
        """
        Given x, compute the equation below:

        z = w1*x1 + w2*x2 + ... wk*xk + b
        """

        # Q2. Calculate the z value using the equation above [1 point]
        z = np.matmul(x,self.w)+self.b
        z = self.activation(z)
        return z


    def bwpass(self, x, err):
        """
        Given x and the error value err, compute and return the gradients "w_grad" for weights w and bias b.

        Refer to https://towardsdatascience.com/intuitions-on-l1-and-l2-regularisation-235f2db4c261 for differentiation based on l1 and l2.

        w_grad: (num_data, num_features)
        b_grad: (num_data, )

        Utilize lambda via self.lamb.
        """

        # Q3. Compute gradients for L1 and L2 regularization [3 points - 1.5 points each]
        if self.penalty == "l1":
            w_grad = np.sum(np.abs(x))
        elif self.penalty == "l2":
            w_grad = np.sum(np.power(x,2))
        
        b_grad = np.sum(err)

        return w_grad, b_grad

    
    def initialize_w(self, x):
        """
        This function doesn't need to be modified.
        Codes LeCun weight initialization technique to set the initial w.
        Initializes the w weights with random values in the same shape as w_library.
        """

        w_library = {
            "one":np.ones(x.shape[1]),
            "LeCun": np.random.uniform(low = -np.sqrt(1/x.shape[1]), high = np.sqrt(1/x.shape[1]), size = x.shape[1]),
            "random": np.random.rand(x.shape[1])
        }

        return w_library[self.initialize]


    def fit(self, x, y):
        """
        This function actually initializes the weights and iterates to compute w and b by differentiation.
        Only code the update process for self.w and self.b, as other functions perform the calculations.
        """

        self.w = self.initialize_w(x)
        self.b = 0
        for _ in range(self.max_iter):
            z = self.fwpass(x)
            err = -(y - z)
            w_grad, b_grad = self.bwpass(x, err)

            # Q4. Update w and b [1 point]
            self.w -=  self.lr * w_grad
            self.b -= self.lr * b_grad
        
        return self.w, self.b


    def predict(self, x):
        """
        This function doesn't need to be modified.
        Given the test input x, return 1 if the value passed through fwpass is greater than 0.5, 
        and 0 if it is less than or equal to 0.5.
        """
        z = self.fwpass(x)
 
        return (z>0.5).astype(int)

    
    def score(self, x, y):
        """
        This function doesn't need to be modified.
        """

        return np.mean(self.predict(x) == y)
    
    
    def feature_importance(self, coef, column_to_use):
        """
        This function doesn't need to be modified.
        Displays the importance of features used in this assignment in order.
        """
        a = np.argsort(abs(coef))[::-1] 

        coef = coef[a] 
        column_to_use = np.array(column_to_use)[a] 

        arr = []
        for i, (col, coef) in enumerate(zip(column_to_use, coef)):
          arr.append((i, col, coef)) 

        return np.array(arr)



