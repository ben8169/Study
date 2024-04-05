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
            self.prior[i] = self.label_index[i].size/training_size      #by this, we can earn P(S), P(NS). It will still work although if there's more cases.
        return self.prior


    def get_likelihood(self):

        """
        This function calculates the likelihood.
        After this function is processed, calculate the likelihood for each word for each label and store it in self.likelihood as follows.
        """
        self.likelihood = {}           #We should make result like -> self.likelihood  = {0:[12,234,0,2,5,..], 1:[2,4,35,8,1,...]}'
        N = self.data.shape[1]


        for i in self.label_index:
            self.likelihood[i] = []
            SIZE = self.label_index[i].size         # at this case, S_SIZE = self.label_index[0].size / NS_SIZE = self.label_index[1].size
            denominator = N*(SIZE+1)
            for j in range(self.data.shape[1]):
                cnt = self.smoothing                #Laplace Smoothing ... Add 1 element at numerator
                for idx in self.label_index[i]:     #Count all the existing words and add to numerator
                    cnt += self.data[idx][j]
                self.likelihood[i].append(cnt)
            
            self.likelihood[i] = np.array(self.likelihood[i])
            self.likelihood[i] = self.likelihood[i]/(denominator+ N)  #Laplace Smoothing...just adding 1 can be possible, so I add 1
            print(self.likelihood[0][:3])

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
        self.posterior = []           #this should be [[p1,p2],[p3,p4],...], as Spam/Ham probabilities

        for testcase in x:
            tmp = []
            #case:spam(lbl_idx = 0) & case:ham(lbl_idx = 1)
            for lbl_idx in self.label_index:
                pst = np.log(self.prior[lbl_idx])       #log-scaled prior
                for idx in range(testcase.size):        #check all 500 words, and count the frequency of words
                    for _ in range(testcase[idx]):
                        pst+=(np.log(self.likelihood[lbl_idx][idx]))    #calculate log-scaled likelihood
                tmp.append(np.exp(pst))
                evidance = sum(tmp) + self.epsilon
                for i in range(len(tmp)):
                    tmp[i] = tmp[i]/evidance
            self.posterior.append(tmp)

        [print(i) for i in self.posterior]
        return self.posterior

    def predict(self, x):

        """
        This function doesn't need to be modified.
        It utilizes likelihood and prior to compute the posterior for actual data and convert it into probabilities.
        """
        posterior = self.get_posterior(x)
        return np.argmax(posterior, axis=1)