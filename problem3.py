__author__ = 'easycui'
import numpy as np
from  problem2 import *
from tree_contruction import *
from TreeNode import *


def mktree(data, title, tree, value):
    """

    :param data: it is the train data to generate, it is a np array with shape(n*(k+1))
           title : it is the list of attributes including the target
           tree : the root of tree
           value : the value of the branch connected to the tree
    :return: return a tree, the structure of the tree is : for example: {1:{1:2,2:3}}
    """

    ""
    if np.unique(data[:, -1]).shape[0] == 1:
        tree.insert_child(0, value, TreeNode(str(data[0, -1])))

    elif inputissame(data[:, :-1]):
        #print("haha")
        d = uniqueValue(data[:, -1])
        maxnum = 0
        for x in d:
            if maxnum < d[x]:
                maj = x
                maxnum = d[x]
        tree.insert_child(0, value, TreeNode(str(maj)))
    else:
        #print(data)
        info_gain = infogain(data)
        attr_index = np.argmax(info_gain)
        max_attr = title[attr_index]
        node = TreeNode(str(max_attr))
        tree.insert_child(0, value, node)

        for x in np.unique(data[:, attr_index]):
            index = np.where(data[:, attr_index] == x)[0]
            #print(data[index,:])
            mktree(data[index, :], title, node, x)
    return 0


def inputissame(data):
    for i in range(data.shape[1]):
        #print(data[:, i])
        if not np.unique(data[:, i]).shape[0] == 1:
            return False
    return True


def gen_mktree(data, title, tree, type, value, conti):
    """

    :param data: data is a np array with shape(n*(k+1)), n is the number of samples, k is the number of attributes
    :param title: the title is the list of attributes
    :param tree: the tree is the root node of the tree
    :param type: type is the type of the branch, it could be a
    :param value: value is the value of the branch
    :param conti: this is a np array with shape(k+1,), it should be like [0,1,0,1] 1 means this attribute is
                continuous, 0 means it is discrete, for target it should be 0
    :return:
    """

    conti_idx = np.extract(conti, np.arange(len(title)))
    disc_idx = np.extract(1 - conti, np.arange(len(title)))
    if np.unique(data[:, -1]).shape[0] == 1:
        tree.insert_child(type, value, TreeNode(str(data[0, -1])))

    elif inputissame(data[:, :-1]):
        d = uniqueValue(data[:, -1])
        maxnum = 0
        for x in d:
            if maxnum < d[x]:
                maj = x
                maxnum = d[x]
        tree.insert_child(type, value, TreeNode(str(maj)))
    else:
        #print(disc_idx, disc_idx[0])
        #print(data)
        #print(data[:,disc_idx])
        info_gain = infogain(data[:, disc_idx])

        max_info = np.max(info_gain)
        attr_index = disc_idx[np.argmax(info_gain)]
        isdisc = 1
        for i in conti_idx:
            info, threshold = t_infogain(data, data[:, i])
            if max_info < info:
                max_info = info
                attr_index = i
                th = threshold
                isdisc = 0

        max_attr = title[attr_index]
        node = TreeNode(str(max_attr))
        #print(max_attr)
        #print(data)
        tree.insert_child(type, value, node)

        if isdisc == 1:
            #print(np.unique(data[:, attr_index]))
            for x in np.unique(data[:, attr_index]):
                index = np.where(data[:, attr_index] == x)[0]
                #print(index)
                gen_mktree(data[index, :], title, node, 0, x, conti)
        else:

            index = np.where(data[:, attr_index] <= th)[0]
            subdata=np.copy(data[index, :])
            subdata[:,attr_index]=th
            gen_mktree(subdata, title, node, -1, th, conti)
            index = np.where(data[:, attr_index] > th)[0]
            subdata=np.copy(data[index,:])
            subdata[:,attr_index]=th+1

            gen_mktree(subdata, title, node, 1, th, conti)
    return 0
    # tree
def e_gen_mktree(data, title, tree, type, value, conti,depth,max_depth):
    """

    :param data: data is a np array with shape(n*(k+1)), n is the number of samples, k is the number of attributes
    :param title: the title is the list of attributes
    :param tree: the tree is the root node of the tree
    :param type: type is the type of the branch, it could be a
    :param value: value is the value of the branch
    :param conti: this is a np array with shape(k+1,), it should be like [0,1,0,1] 1 means this attribute is
                continuous, 0 means it is discrete, for target it should be 0
    :return:
    """

    conti_idx = np.extract(conti, np.arange(len(title)))
    disc_idx = np.extract(1 - conti, np.arange(len(title)))
    if np.unique(data[:, -1]).shape[0] == 1:
        tree.insert_child(type, value, TreeNode(str(data[0, -1])))

    elif inputissame(data[:, :-1]) or depth==max_depth:
        d = uniqueValue(data[:, -1])
        maxnum = 0
        for x in d:
            if maxnum < d[x]:
                maj = x
                maxnum = d[x]
        tree.insert_child(type, value, TreeNode(str(maj)))
    else:
        #print(disc_idx, disc_idx[0])
        #print(data)
        #print(data[:,disc_idx])
        info_gain = infogain(data[:, disc_idx])

        max_info = np.max(info_gain)
        attr_index = disc_idx[np.argmax(info_gain)]
        isdisc = 1
        for i in conti_idx:
            info, threshold = t_infogain(data, data[:, i])
            if max_info < info:
                max_info = info
                attr_index = i
                th = threshold
                isdisc = 0

        max_attr = title[attr_index]
        node = TreeNode(str(max_attr))
        #print(max_attr)
        #print(data)
        tree.insert_child(type, value, node)

        if isdisc == 1:
            #print(np.unique(data[:, attr_index]))
            for x in np.unique(data[:, attr_index]):
                index = np.where(data[:, attr_index] == x)[0]
                #print(index)
                e_gen_mktree(data[index, :], title, node, 0, x, conti,depth+1,max_depth)
        else:

            index = np.where(data[:, attr_index] <= th)[0]
            subdata=np.copy(data[index, :])
            subdata[:,attr_index]=th
            e_gen_mktree(subdata, title, node, -1, th, conti,depth+1,max_depth)
            index = np.where(data[:, attr_index] > th)[0]
            subdata=np.copy(data[index,:])
            subdata[:,attr_index]=th+1

            e_gen_mktree(subdata, title, node, 1, th, conti,depth+1,max_depth)
    return 0

def main():
    data, title = parseCSV("./play_tennis.csv","string")
    #print(data)
    tree = TreeNode("nil")
    mktree(data, title, tree, "nil")
    tree2dot("3_b tree", tree)
    # tree=TreeNode("nil")
    # gen_mktree(data,title,tree,0,"nil",np.array[0,1,1,1,1,0])
    # tree2dot("3_c tree",tree)


if __name__ == "__main__":
    main()
