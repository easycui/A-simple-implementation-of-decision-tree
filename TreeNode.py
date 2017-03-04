__author__ = 'easycui'


class TreeNode:
    def __init__(self, attr):
        self.attr = attr
        self.children = []
        self.branches = []

    # def insert_child(self, branch, TreeNode):
    #     """
    #
    #     :param branch:  branch is a dictionary, it should be a dictionary,like {
    #     type: could be -1,0,1, -1 means less than the value, 0 means equal to value
    #           1 means larger than the value
    #     value : the value to discredited the attribute
    #
    #     }
    #     :param TreeNode: another TreeNode object
    #     :return:
    #     """
    #     self.children.append(TreeNode)
    #     self.branches.append(branch)

    def insert_child(self, type, value, TreeNode):
        """

        :param
        type: could be -1,0,1, -1 means less than the value, 0 means equal to value
              1 means larger than the value
        value : the value to discredited the attribute


        :param TreeNode: another TreeNode object
        :return:
        """
        branch=dict()
        branch['type']=type
        branch['value']=value
        self.children.append(TreeNode)
        self.branches.append(branch)

    def get_child(self, branch):
        try:
            index = self.branches.index(branch)
            return self.children[index]
        except:
            return 0

    def get_children(self):
        return self.children

    def get_attr(self):
        return self.attr

    def get_branches(self):
        return self.branches
