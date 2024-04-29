# Write your name and student ID
__author__ = "김지헌"
__id__ = "2022313356"

# Do not import and other Python libraries
import numpy as np


class SVMClassifier:
    def __init__(self,n_iters=100, lr = 0.0001, random_seed=3, lambda_param=0.01):
        """
        This function doesn't need to be modified.
        """

        self.author = __author__
        self.id = __id__
        self.n_iters = n_iters
        self.lr = lr 
        self.lambda_param = lambda_param
        self.random_seed = random_seed
        np.random.seed(self.random_seed)


    def fit(self, x, y):
        """
        This function trains the model using x, y.
        """

        n_samples, n_features = x.shape

        y_ = list(map(lambda x: -1 if x == 0 else x, y))
        
        init_w = np.random.rand(n_features)
        self.w = init_w
        self.b = 0 

        for _ in range(self.n_iters):
            for i in range(n_samples):
                x_i = x[i]
                y_i = y_[i]

                # Q1. Update the gradients [4 points - 1 point each] 
                condition = 1 - y_i*(np.matmul(self.w,x_i)+self.b)

                if condition:
                    self.w -= 2*self.lambda_param*self.w
                else:
                    self.w -= 2*(self.lambda_param*self.w + (x_i*y_i))
                    self.b -= 2*self.lambda_param*self.b
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

        # Q2. Complete the function predict() [5 points]
        output = []
        self.x = x
        for i in self.x:
            if (np.matmul(self.w*self.x)-self.b) >= 0:
                output.append(1)
            else:
                output.append(0)

        output = np.array(output) 
        return output


    def get_accuracy(self, y_true, y_pred):
        """
            This function doesn't need to be modified.
            Calcuates the accuracy using y_true and y_pred.
        """
        t = 0 

        for i, value in enumerate(y_pred):
            if y_true[i] == value:
                t += 1

        return t / len(y_pred)

