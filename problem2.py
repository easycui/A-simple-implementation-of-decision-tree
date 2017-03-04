__author__ = 'easycui'

import numpy as np
import csv


def parseCSV(filename,type):
    """

    :param filename: the filename of CSV file
    :return: data: the data is the content since the second row, it is a (n*m) np.array, n is the number of records
                   m is the number of attributes+1
             title: the content in the first row, it is a list
    """
    if type=="num":
        title = []
        data = []
        with open(filename, 'rU') as csvfile:
            content = csv.reader(csvfile, delimiter=',')
            row_num = 1
            for row in content:
                if row_num == 1:
                    title = row
                    data = np.zeros((1, len(row)))
                else:
                    sample = np.array([])
                    for d in row:
                        sample = np.append(sample, [float(d)], axis=0)
                    sample = sample.reshape(1, len(row))
                    data = np.append(data, sample, axis=0)
                row_num += 1
        return data[1:,:], title
    else:
        title = []
        data = []
        colume=[]
        with open(filename, 'rU') as csvfile:
            content = csv.reader(csvfile, delimiter=',')
            row_num = 1
            for row in content:
                if row_num == 1:
                    title = row
                else:
                    data.append(row)
                row_num += 1
            trans_data=np.zeros((row_num-2,len(title)))
            for j in range(len(data[0])):
                for i in range(len(data)):
                    colume.append(data[i][j])
                uniq=set(colume)
                d=dict()
                num=0
                for k in uniq:
                    d[k]=num
                    num+=1
                for m in range(len(colume)):
                    trans_data[m,j]=float(d[colume[m]])
                colume=[]
        return trans_data, title


def parse_state(data):
    """

    :param data: data should be a np.array, shape is (n,)
    :return: states is np.array, shape is (1,K), K is the amount of different states, state[1] means the probability of state 1
    """
    d = uniqueValue(data)
    states = np.zeros(len(d))
    i = 0
    for x in d:
        states[i] = float(d[x]) / data.shape[0]
        i += 1
    #print(states)
    return states


def entropy(data):
    """
    :param data: it should be a np.array, shape is (n,)
    :return: the entropy of this data
    """
    prob = parse_state(data)
    H = -np.sum(prob * np.log2(prob))
    return H


def uniqueValue(data):
    d = dict()
    for x in data:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    return d


def infogain(data):
    """
    :param data: it should be a matrix of size N*(|A|+1)
    :return: return the information gain IG(S,A_{c}) of each categorical attribute, it should be a np.array, shape is
            (|A|,)
    """
    width = data.shape[1]
    H_S = entropy(data[:, width - 1])
    #print(H_S)
    IG = np.zeros(width - 1) + H_S

    for i in range(width - 1):
        con_entropy = condentropy(data, data[:, i])
        IG[i] -= con_entropy
    return IG


def condentropy(data, data_A):
    """

    :param data: it should be a matrix of size N*(|A|+1)
    :param attr:  it should indicate the index of the known attribute
    :return: the conditional entropy
    """
    con_entropy = 0
    d = uniqueValue(data_A)
    for x in d:
        index = np.where(data_A == x)
        con_entropy += float(index[0].shape[0]) / data.shape[0] * entropy(data[:, -1][index])
    return con_entropy


def gainratio(data):
    """

    :param data: it should be a matrix of size N*(|A|+1)
    :return: return the gain ratio of each categorical attribute, it should be a np.array, shape is
            (|A|,)
    """
    return infogain(data) / splitinfo(data[:,:-1])


def splitinfo(data):
    """

    :param data: it should be a matrix of size N*(|A|)
    :return: return the split information of each categorical attribute, it should be a np.array, shape is
            (|A|,)
    """
    SI = np.zeros(data.shape[1] - 2)
    for i in range(data.shape[1] - 2):
        SI[i] = entropy(data[:, i])
    return SI


def t_infogain(data, data_A):
    """
    :param data: it should be a np.array, shape is (n,),

    It will finds the value of a threshold t that converts this to a binary attribute and maximizes its information gain
    IG(S,A_{r};t)

    :return: IG*(S,A_{r})= argmax_{t} IG(S_{r},A_{r}:t)
    """

    H_S = entropy(data[:, -1])
    min_A=H_S
    threshold=0
    #print(data_A)
    for i in range(data.shape[0]):
        data_copy = np.copy(data_A)
        data_copy[np.where(data_A > data_A[i])] = 0
        data_copy[np.where(data_A <= data_A[i])] = 1
        con_entropy = condentropy(data, data_copy)
        if con_entropy < min_A:
            min_A = con_entropy
            #print(data_A[i])
            threshold=data_A[i]
            #print(threshold)
    return H_S-min_A, threshold


def main():
    data, title = parseCSV("./dataset_infoth.csv","num")
    print("The information gain of attr [A1,A2,A3] is")
    print(infogain(data[:,np.array([0,1,2,4])]))
    print("The information gain of attr A4 and the threshold is")
    print(t_infogain(data, data[:,-2]))
    print("The gainratio of attr[A1,A2,A3] is")
    print(gainratio(data[:,np.array([0,1,2,4])]))

if __name__ == "__main__":
    main()
