__author__ = 'easycui'

from problem2 import *
from problem3 import *
from problem4 import *
import numpy as np
import matplotlib.pyplot as plt


def train(data, tree, conti, title):
    """

    :param data: training data, it should be a np.array with shape(n*k+1), K is the attribute num, the last
                column is the label
    :return: return generated  decision tree
    """
    gen_mktree(data, title, tree, 0, "nil", conti)
    # tree2dot("3_c tree",tree)
def train_e(data, tree, conti, title, maxdepth):
    """

    :param data: training data, it should be a np.array with shape(n*k+1), K is the attribute num, the last
                column is the label
    :return: return generated  decision tree
    """
    e_gen_mktree(data, title, tree, 0, "nil", conti, 0, maxdepth)
    # tree2dot("3_c tree",tree)

def test(data, tree, conti, title):
    return cltree(data, tree, conti, title)


def plot(training_error, test_error):
    a = [2, 3, 4, 5]
    plt.plot(a, training_error)
    plt.plot(a, test_error)
    plt.show()


def main():
    data, title = parseCSV("./mpg_train.csv",'num')


    # 5.b

    tree = TreeNode("nil")
    conti = np.array([0, 1, 1, 1, 1,0])
    train(data, tree, conti, title)
    tree2dot("5_b tree", tree)
    # 5.c
    #training_error_rate = test(data, tree, conti, title)


    data, title = parseCSV("./mpg_test.csv",'num')
    test_error_rate = test(data, tree, conti, title)
    print("training error rate and test error rate are:")
    #print(training_error_rate, test_error_rate)
    #
    # # 5.d
    # data, title = parseCSV("./mpg_train.csv",'num')
    # conti = np.array([0, 1, 1, 1, 0, 0])
    # tree = TreeNode("nil")
    # train(data, tree, conti, title)
    # tree2dot("5_d tree", tree)
    # training_error_rate = test(data, tree, conti, title)
    # data, title = parseCSV("./mpg_test.csv",'num')
    #
    # test_error_rate = test(data, tree, conti, title)
    # print("5_d: training error rate and test error rate are:")
    # print(training_error_rate, test_error_rate)
    #
    # # 5.e
    # training_error=[]
    # test_error=[]
    #
    # for i in range(2,6):
    #     data, title = parseCSV("./mpg_train.csv",'num')
    #     conti = np.array([0, 1, 1, 1, 1,0])
    #     tree = TreeNode("nil")
    #     train_e(data, tree, conti, title, i)
    #     tree2dot("5_e tree_" + str(i), tree)
    #     # 5.c
    #     training_error_rate = test(data, tree, conti, title)
    #     data, title = parseCSV("./mpg_test.csv",'num')
    #     test_error_rate = test(data, tree, conti, title)
    #     training_error.append(training_error_rate)
    #     test_error.append(test_error_rate)
    # print(training_error,test_error)
    # plot(training_error, test_error)


if __name__=="__main__":
    main()