# Write your name and student ID
__author__ = "김지헌"
__id__ = "2022313356"

# Do not import and other Python libraries
import numpy as np


# Write your code following the instructions
class NaiveBayesClassifier:
    def __init__(self, smoothing=1):

        """
        This function doesn't need to be modified.
        """

        self.author = __author__
        self.id = __id__
        self.smoothing=smoothing
        self.epsilon = 1e-10


    def fit(self, x, y):

        """
        This function doesn't need to be modified.

        This is the part where actual training (probability calculation) takes place.
        A numpy matrix of size [number of documents x word feature size (500)] is stored in self.data,
        and labels for each document are stored in self.labels as a numpy matrix of shape [number of documents, ].

        After this function is called, the variable self.label_index is stored in the following dictionary format:
        self.label_index = {0: array([   1,    4,    5, ..., 3462, 3463, 3464]), 1: array([   0,    2,    3, ..., 3447, 3449, 3453])}
        Document IDs for label 0 are in numpy array format, and document IDs for label 1 are in numpy array format as shown above.

        Afterward, label_index, prior, and likelihood are calculated sequentially.
        The self.get_... functions called below are the calculation functions that you need to implement.
        """

        self.data = x           #counter vector
        self.labels = y

        self.label_index = dict()           
        self.label_name = set(self.labels)
        for lab in self.label_name:
            self.label_index[lab] = []          #the result will be -> self.label_index = {0: [], 1: []}

        for index, label in enumerate(self.labels):
            self.label_index[label].append(index)       #the result will be -> self.label_index = {0: [1,4,5,...], 1: [0,2,3,...]}
            
        for lab in self.label_name:
            self.label_index[lab] = np.array(self.label_index[lab])         #the result will be -> self.label_index = {0: array([1,4,5,...]), 1: array([0,2,3,...])}

        self.get_prior()
        self.get_likelihood()
        

    def get_prior(self):

        """
        This function calculates the prior.
        After this function is processed, ensure that the self.prior variable contains the label as the key and the prior for the label as the value.
        self.prior = {0: prior value for label 0, 1: prior value for label 1}

        However, in grading, if it works correctly only for cases with two labels, no points will be awarded.
        """ 


        self.prior = dict()
        training_size = self.data.shape[0]          #Get train size
        for i in self.label_index:
            self.prior[i] = self.label_index[i].size/training_size      #by this, we can earn P(S), P(NS). Also,
        return self.prior


    def get_likelihood(self):

        """
        This function calculates the likelihood.
        After this function is processed, calculate the likelihood for each word for each label and store it in self.likelihood as follows.
        """
        
        self.likelihood = {}
        for i in self.label_index:
            self.likelihood[i] = []      #{0:[], 1:[]}
        for i in self.label_index:
            total_size = self.label_index[i].size
            for j in self.label_index[i]:
                self.data[j][]
                self.likelihood[i+1] = cnt+self.smoothing /(self.data.shape[0]+self.smoothing)*self.data.shape[1]   #smoothing 1
        return self.likelihood


    def get_posterior(self, x):

        """
        This function calculates the posterior using self.likelihood and self.prior.
        Calculate the posterior for labels 0 and 1.

        Utilize log and exp to prevent overflow. Consider the following equation to compute the posterior:

        posterior 
        = prior * likelihood 
        = exp(log(prior * likelihood))  refer. log(ab) = log(a) + log(b)
        = exp(log(prior) + log(likelihood))

        Add self.epsilon to the denominator to prevent nan during probability calculation.
        """

        self.posterior = []
        sum = np.log(self.prior)
        for i in self.likelihood:

        # np.exp(np.log(self.prior) + np.log(self.))



        
        return self.posterior


    def predict(self, x):

        """
        This function doesn't need to be modified.
        It utilizes likelihood and prior to compute the posterior for actual data and convert it into probabilities.
        """

        posterior = self.get_posterior(x)
        return np.argmax(posterior, axis=1)



