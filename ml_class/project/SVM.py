__author__ = "name"
__id__ = "2023000000"

# Do not import and other Python libraries
import numpy as np
import matplotlib.pyplot as plt


# Write your code following the instructions
class SVMClassifier:
    def __init__(self,n_iters=100, lr = 0.0001, random_seed=3, lambda_param=0.01):
        """
        This function doesn't need to be modified.
        """
        self.author = __author__
        self.id = __id__
        self.n_iters = n_iters # number of iterations
        self.lr = lr  # learning rate
        self.lambda_param = lambda_param
        self.random_seed = random_seed
        np.random.seed(self.random_seed)


    def fit(self, x, y):
        """
        This function trains the model using x, y.
        You can reference the website below for gradient updates.
        reference: https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47
        Fill out the 6 "None"s from the code below.

        """
        n_samples, n_features = x.shape

        # hint: in order to use y for SVM, change zeros to -1.
        y_ =  None 
        
        # hint: reset w, a numpy array with random values between 0 to 1, with the size of (n_features, ).
        init_w = None 
        self.w = init_w
        self.b = 0 # reset b

        for _ in range(self.n_iters):
            for i in range(n_samples):
                x_i = x[i]
                y_i = y_[i]

                # hint: filter cases with y(i) * (w · x(i) + b) >= 1 using if statement.
                condition = None 
                if condition:
                    # hint: update W using the Gradient Loss Function equation.
                    self.w -= self.lr * None 
                else:
                    # hint: update W using the Gradient Loss Function equation.
                    self.w -= self.lr * None 
                    self.b -= self.lr * y_i

        return None 


    def predict(self, x):
        """
            Given x, [n_samples x features], use self.w and self.b from fit() to predict the value.

            @args:
                x with the shape of [n_samples x features]
            @returns:
                array with the shape of [n_samples, ]

            You can refer to the equation and pseudocode below:
                approximation = W·X - b
                if approximation >= 0 {
                    output = 1
                }
                else{
                    output = 0
                }
        """

        return 


    def get_accuracy(self, y_true, y_pred):
        """
            Calcuate the accuracy using y_true and y_pred.
            Do not use sklearn's accuracy_score. Only use numpy.
        """

        return 

