__author__ = "김지헌"
__id__ = "2022313356"

# Do not import and other Python libraries
import numpy as np
import matplotlib.pyplot as plt


# Write your code following the instructions
class SVMClassifier:
    def __init__(self,n_iters=1000, lr = 0.0001, random_seed=3, lambda_param=0.01):
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
        y_ =  [-1 if i<=0 else 1 for i in y]
        # y_ =  [1 if i==1 else -1 for i in y]
        
        # hint: reset w, a numpy array with random values between 0 to 1, with the size of (n_features, ).
        init_w = np.random.rand(n_features,)
        self.w = init_w
        self.b = 0 # reset b

        for _ in range(self.n_iters):
            for i in range(n_samples):
                x_i = x[i]
                y_i = y_[i]

                # hint: filter cases with y(i) * (w · x(i) + b) >= 1 using if statement.
                condition = y_i*(sum(self.w*x_i) + self.b)>= 1
                if condition:
                    # hint: update W using the Gradient Loss Function equation.
                    self.w -= self.lr*(2*self.lambda_param*self.w)
                else:
                    # hint: update W using the Gradient Loss Function equation.
                    self.w += self.lr*(y_i*x_i - 2*self.lambda_param*self.w) 
                    self.b -= self.lr * y_i

        return self.w, self.b


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
        y_pred = []
        approximation = np.matmul(x,self.w) - self.b
        for i in approximation:
            if i>=0: y_pred.append(1)
            else: y_pred.append(0)
        return y_pred


    def get_accuracy(self, y_true, y_pred):
        """
            Calcuate the accuracy using y_true and y_pred.
            Do not use sklearn's accuracy_score. Only use numpy.
        """
        answer_cnt = 0
        for label,pred in zip(y_true, y_pred):
            if (label==pred): answer_cnt+=1

        print("Accuracy: ", answer_cnt/len(y_true)*100, '%')

        plt.scatter(range(len(y_true)), y_true, c=y_true)
        plt.scatter(range(len(y_pred)), y_pred, c=y_pred, marker='x')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.title('SVM Classifier Results')
        plt.show()
        return 


class MulticlassSVM:
    def __init__(self, n_iters=1000, lr=0.0001, random_seed=3, lambda_param=0.01):
        self.n_iters = n_iters
        self.lr = lr
        self.lambda_param = lambda_param
        self.random_seed = random_seed
        np.random.seed(self.random_seed)

    def fit(self, x, y):
        self.classes = np.unique(y)
        self.num_classes = len(self.classes)
        self.classifiers = {}

        for i in range(self.num_classes):
            for j in range(i+1, self.num_classes):
                cls1 = self.classes[i]
                cls2 = self.classes[j]
                indices = np.logical_or(y == cls1, y == cls2)
                binary_y = np.where(y[indices] == cls1, 1., -1.)
                binary_x = x[indices]
                classifier = SVMClassifier(self.n_iters, self.lr, self.random_seed, self.lambda_param)
                classifier.fit(binary_x, binary_y)
                self.classifiers[(cls1, cls2)] = classifier
        return self.classifiers

    def predict(self, x):
        self.scoreboard = np.zeros((len(x),self.num_classes))
        for classes, classifier in self.classifiers.items():
            cls1, cls2 = classes
            binary_predictions = classifier.predict(x)
            for i in range(len(binary_predictions)):
                if list(binary_predictions)[i] == 1: 
                    self.scoreboard[i][int(cls1)] +=  1
                else: 
                    self.scoreboard[i][int(cls2)] += 1

        return self.scoreboard.argmax(axis=1)
    
    def get_accuracy(self, y_true, y_pred):
        """
            Calcuate the accuracy using y_true and y_pred.
            Do not use sklearn's accuracy_score. Only use numpy.
        """
        answer_cnt = 0
        for label,pred in zip(y_true, y_pred):
            if (label==pred): answer_cnt+=1

        accuracy =  answer_cnt/len(y_true)*100
        return accuracy
    




# class MulticlassSVM:
#     def __init__(self, n_iters=100, lr=0.0001, random_seed=3, lambda_param=0.01):
#         self.n_iters = n_iters
#         self.lr = lr
#         self.lambda_param = lambda_param
#         self.random_seed = random_seed
#         np.random.seed(self.random_seed)

#     #one to one
#     def vote(self, x, y):
#         self.classes = np.unique(y)     #0, 1, 2, 3
#         self.num_classes = len(self.classes)
#         self.scoreboard = np.zeros((self.x.shape[0],self.num_classes))
#         self.classifiers = {}

#         for i in range(self.num_classes):
#             for j in range(i+1, self.num_classes):
#                 x_tmp = 

#             for second_cls in 
#             binary_y = np.where(y == cls, 1, -1)
#             classifier = SVMClassifier(self.n_iters, self.lr, self.random_seed, self.lambda_param)
#             classifier.fit(x, binary_y)
#             self.classifiers[cls] = classifier

#     def predict(self, x):
#         predictions = np.zeros(len(x))
#         for cls, classifier in self.classifiers.items():
#             binary_predictions = classifier.predict(x)
#             predictions = np.where(binary_predictions == 1, cls, predictions)
#         return predictions.astype(int)
    

# class SVMClassifier:
#     def __init__(self, n_iters=100, lr=0.0001, random_seed=3, lambda_param=0.01):
#         self.n_iters = n_iters
#         self.lr = lr
#         self.lambda_param = lambda_param
#         self.random_seed = random_seed
#         np.random.seed(self.random_seed)

#     def fit(self, X, y):
#         n_samples, n_features = X.shape
#         self.w = np.random.rand(n_features)
#         self.b = 0

#         for _ in range(self.n_iters):
#             for i in range(n_samples):
#                 x_i = X[i]
#                 y_i = y[i]

#                 condition = y_i * (np.dot(self.w, x_i) + self.b) >= 1
#                 if condition:
#                     self.w -= self.lr * (2 * self.lambda_param * self.w)
#                 else:
#                     self.w += self.lr * (y_i * x_i - 2 * self.lambda_param * self.w)
#                     self.b -= self.lr * y_i

#     def predict(self, X):
#         approximations = np.dot(X, self.w) - self.b
#         return np.where(approximations >= 0, 1, -1)