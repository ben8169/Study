# Write your name and student ID
__author__ = "김지헌"
__id__ = "2022313356"

# Do not import and other Python libraries
import numpy as np


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
        """

        self.data = x
        self.labels = y

        self.label_index = dict()
        self.label_name = set(self.labels)
        for lab in self.label_name:
            self.label_index[lab] = []

        for index, label in enumerate(self.labels):
            self.label_index[label].append(index)
            
        for lab in self.label_name:
            self.label_index[lab] = np.array(self.label_index[lab])

        self.get_prior()
        self.get_likelihood()
        

    def get_prior(self):
        """
        This function doesn't need to be modified.
        This function calculates the prior.
        After this function is processed, self.prior variable contains the label as the key and the prior for the label as the value.
        self.prior = {0: prior value for label 0, 1: prior value for label 1}
        """

        self.prior = dict()
        total=self.data.shape[0]

        for label in self.label_name:
            self.prior[label]=len(self.label_index[label])/total
        
        
        return self.prior


    def get_likelihood(self):
        """
        This function doesn't need to be modified.
        This function calculates the likelihood.
        """
        
        self.likelihood = {}

        word_num=self.data.shape[1]

        for label in self.label_name:
            total_appear=0 
            each_appear=[] 

            for idx in self.label_index[label]:
                idx_row=self.data[idx] 
                total_appear+=idx_row.sum()
                each_appear.append(idx_row)
                
            each_appear=np.array(each_appear).sum(axis=0)
            self.likelihood[label]=(each_appear+self.smoothing)/(total_appear+word_num)

   
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

        # Q1. Complete the function get_posterior() [5 points]
        self.posterior = []
        for label in self.label_name:
            for i in range(len(self.data.shape[0])):
                p = self.prior[label][i]
                l = self.likelihood[label][i]
                self.posterior.append(np.exp(np.log(p)+np.log(l)+self.epsilon))
        
        return self.posterior


    def predict(self, x):
        """
        This function doesn't need to be modified.
        It utilizes likelihood and prior to compute the posterior for actual data and convert it into probabilities.
        """

        posterior = self.get_posterior(x)
        return np.argmax(posterior, axis=1)



