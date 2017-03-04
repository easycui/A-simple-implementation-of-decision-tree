__author__ = 'easycui'

from  problem3 import *
from TreeNode import *


def cltree(data, tree, conti, title):
    """

    :param data: the data will be tested
    :param tree: the tree generated from
    :param conti: it is a np. array with shape(k+1), k is the number of attribute of data, it would be like
                  [0,1,1,0]. 1 means this attribute is continuous, for target, it should be 0
    :return: return the error rate of the testing
    """
    sample_num = data.shape[0]
    error_num = 0.0
    for i in range(sample_num):
        if sampletest(data[i, :], tree, conti,title) == 0:
            error_num += 1.0
            print(i)
        #print(error_num)
    error_rate = error_num / sample_num

    return error_rate


def sampletest(sample, tree, conti, title):
    """

    :param sample: it should be a
    :param tree:
    :param conti:
    :return:
    """
    #print(tree)
    #print(sample)
    cur = tree.get_children()[0]
    while cur.get_children():
        attr_index = title.index(cur.get_attr())
        if conti[attr_index] == 1:
            #print(cur.get_branches())
            #print(cur.get_branches()[0]['value'])
            if sample[attr_index] > cur.get_branches()[0]['value']:
                if cur.get_branches()[0]['type'] == 1:
                    cur = cur.get_children()[0]
                else:
                    cur = cur.get_children()[1]
            else:
                if cur.get_branches()[0]['type'] == -1:
                    cur = cur.get_children()[0]
                else:
                    cur = cur.get_children()[1]
        else:
            branch = dict()
            branch['type'] = 0
            branch['value'] = sample[attr_index]
            cur = cur.get_child(branch)
            if cur==0:
                return 0
    prediction = cur.get_attr()
    #print(prediction,sample[-1])
    if int(float(prediction)) == int(sample[-1]):
        return 1
    else:
        return 0


def main():
    data, title = parseCSV("./play_tennis.csv", "string")
    #print(data)
    tree = TreeNode("nil")
    mktree(data, title, tree, "nil")
    error=cltree(data, tree, np.array([0, 0, 0, 0, 0]), title)
    return error


if __name__ == "__main__":
    print(main())
