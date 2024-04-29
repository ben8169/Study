# Write your name and student ID
__author__ = "김지헌"
__id__ = "2022313356"

# Do not import and other Python libraries
import numpy as np


class my_evaluation_metrics:
    
    def __init__(self):
        self.author = __author__
        self.id = __id__

    def my_confusion_matrix(self, y_true, y_pred, pos_label=1):
        """
        Print confusion matrix using variable pos_label.
        You MUST use the variable pos_label.
    
        pos_label: positive label (usually 1 in binary classification)
        Output type is numpy array.
        """

        cm_result = [[0, 0], [0, 0]]

        # Q1. Complete the function my_confusion_matrix() [3 points]
        for true, pred in zip(y_true,y_pred):
            if true != pos_label:
                if pred != pos_label:
                    cm_result[0][0] += 1
                else:
                    cm_result[0][1] += 1
            else:
                if pred != pos_label:
                    cm_result[1][0] += 1
                else:
                    cm_result[1][1] += 1    
        return np.array(cm_result)


    def my_tf_idf(self, documents):
        """
        Print TF-IDF of the function.
        Reference the lecture materials to compute values for the variable tf_idf.
        The shape of tf_idf is (len(documents), len(word_list)).
        """

        # Word list from documents
        word_list = [] 
        for doc in documents:
            splited = doc.split(' ')
            for word in splited:
                if word not in word_list:
                    word_list.append(word)

        # Initialize numpy array to calculate TF-IDF.


        tf_idf = np.zeros((len(documents), len(word_list)))

        # #Q2. Complete the function my_tf_idf() [5 points]
        tf = np.zeros_like(tf_idf)
        for i in range(len(documents)):
            docu = documents[i]
            for word in word_list:
                idx = word_list.index(word)
                if word in docu:
                    tf[i][idx]+=docu.count(word)

        df = [0]*len(word_list)
        for word in word_list:
            idx = word_list.index(word)
            for doc in documents:
                if word in doc:
                    df[idx] += 1
        idf = []    
        for i in df:
            idf.append(np.log(len(documents)/(1+i)))
        idf = np.array(idf)

        tf_idf = tf*idf

        return tf_idf
