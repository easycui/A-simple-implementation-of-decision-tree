import pydot
from TreeNode import *


# this is a helper function to convert the tree data structure into a dot file
def convert2dot(filename, tree, ctr):
    if tree.get_attr() == "nil":
        convert2dot(filename, tree.get_children()[0], ctr)
        return 0

    ctr1 = ctr + 1;
    f = open(filename + ".dot", "a")

    # print current node,print the attribute, if it doesn't have children, that is it is leaf,
    # print the label in a box
    if tree.get_branches():
        f.write("\n" + str(ctr) + " [label = \"" + str(tree.get_attr()) + "\"];")
    else:
        f.write("\n" + str(ctr) + " [shape=box label = \"" + str(tree.get_attr()) + "\"];")
    f.close()

    # visit the children of tree, print the branches
    for i in range(len(tree.get_children())):
        f = open(filename + ".dot", "a")
        if tree.get_branches()[i]['type'] == 0:
            f.write("\n" + str(ctr) + " -> " + str(ctr1) + "[label=\"" + str(tree.get_branches()[i]['value']) + "\"];")

        elif tree.get_branches()[i]['type'] == -1:
            f.write(
                "\n" + str(ctr) + " -> " + str(ctr1) + "[label=\" <=" + str(tree.get_branches()[i]['value']) + "\"];")
        else:
            f.write(
                "\n" + str(ctr) + " -> " + str(ctr1) + "[label=\" >" + str(tree.get_branches()[i]['value']) + "\"];")

        f.close()

        ctr1 = convert2dot(filename, tree.get_children()[i], ctr1)
    return ctr1


# this is the main function for generating a dot file
# and a pdf file with given the tree data structure
def tree2dot(filename, tree):
    # generate dot file
    f = open(filename + ".dot", "w")
    f.write("digraph G{ \ncenter = 1; \nsize=\"250,210\";")
    f.close()
    convert2dot(filename, tree, 0)
    f = open(filename + ".dot", "a")
    f.write("\n}")
    f.close()

    # generate pdf file
    graph = pydot.graph_from_dot_file(filename + ".dot")
    graph.write_pdf(filename + ".pdf")


# .dot files can be visualize using Graphviz (www.graphviz.org)


