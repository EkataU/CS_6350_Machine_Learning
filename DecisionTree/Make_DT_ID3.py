#Author: Ekata Mitra
# =============================================================================
# CS 5350/6350: Machine Learining Fall 2022:
# HW1: Section 2
# Question 1
# =============================================================================

# =============================================================================
# Decision Tree implementation using ID3 Algorithm
# Step 1: Load Dataset
# Step 2: Prediction error: Entropy, Gini Index and Majority Error
# Step 3: feature Index: Information Gain
# The max tree depth is also varied. 

# =============================================================================

import sys
import math
import Dataloader # module to get data and pre-processed data

# =============================================================================
# # Decision Tree class: Define tree structure
# _init_ function:
# input:
#     :param: depth : path to import sample data (s)
#           : feature : type of dataset
# _set_root function:
#             :param: node list
# =============================================================================


class Tree:
    def __init__(self, feature="ig", depth=0):
        self.feature = feature
        self.depth = depth
        self.root = None

    def set_root(self, node):
        self.root = node

# =============================================================================
# # Decision Tree class: Define tree structure
# _init_ function:
# input:
#     :param: depth : path to import sample data (s)
#           : feature : type of dataset
# _set_root function:
#             :param: node list
# =============================================================================
               
class Node:
    def __init__(self, s, parent, is_leaf):
        self.s = s
        self.parent = parent
        self.is_leaf = is_leaf
        self.branches = {}
        self.attribute = -1
        self.label = None

    def set_attribute(self, attribute):
        self.attribute = attribute

    def set_label(self, label):
        self.label = label

    def add_branch(self, value, node):
        self.branches[value] = node
# =============================================================================
# 
# #ID3 Ref: Gain(S,A) = Feature(S)- ratio* Feature(S_V)
# Feature: Entropy/ME/GI
# ratio : Sum_v<A((S_v/S))
# 
# =============================================================================

def _recursive_ID3(s, parent, a, feature, level, depth):
    if s[-1].count(s[-1][0]) == len(s[-1]):
        node = Node(s, parent, True)
        node.set_label(s[-1][0])
        return node

    elif len(a) == 0 or level == depth+1:
        node = Node(s, parent, True)
        node.set_label(_select_MajLabel(s[-1]))
        return node

    else:
        node = Node(s, parent, False)
        _split_on_gain(feature, node, a)

        for value in node.attribute:
            s_v = _find_s_v(node, node.attribute, value)

            if len(s_v[-1]) == 0:
                label = _select_MajLabel(s[-1])
                child = Node({}, node, True)
                child.set_label(label)
                node.add_branch(value, child)

            else:
                copy = a.copy()
                copy.remove(node.attribute)
                child = _recursive_ID3(s_v, node, copy, feature, level + 1, depth)
                node.add_branch(value, child)

        return node

# =============================================================================
# # Function: This function computes gain for given sample and attribute
# input:
#     :param: node: split on that node 
#           : attribute : attribute at that split one
#           : feature : Entropy/ME/GI
# output:   :return: Gain(S,A) for particular feature
# =============================================================================        
def _calculate_gain(node, attribute, feature):
    gain = 0.0
    gain += _select_feature(node.s, feature)
    for value in attribute:
        s_v = _find_s_v(node, attribute, value)

        if len(s_v[-1]) != 0:
            ratio = len(s_v[-1]) / len(node.s[-1])
            feat_s_v = _select_feature(s_v, feature)

            if feat_s_v != 0:
                gain -= ratio * feat_s_v

    return gain
# =============================================================================
# #Helper Function to compute gain on specific feature
# input:
#     :param: s: sample list
#           : feature : Entropy/ME/GI
# output:   :return: Calculate feature value on selection for input feature
# ============================================================================= 

def _select_feature(s, feature):
    if   feature == "me": return _calculate_ME(s)
    elif feature == "gi": return _calculate_GI(s)
    else: return _calculate_H_s(s)
# =============================================================================
# #Helper Function to compute gain on specific feature
# input:
#     :param: s: sample list
# output:   :return: Calculate Entropy if "ig" selected
# ============================================================================= 

def _calculate_H_s(s):
    h_s = 0.0
    for label in labels:
        num_of_s_l = _get_s_l(s, label)
        if num_of_s_l != 0:
            probability_of_label = num_of_s_l / len(s[-1])
            h_s -= probability_of_label * math.log(probability_of_label, 2)
    return h_s
# =============================================================================
# #Helper Function to compute gain on specific feature
# input:
#     :param: s: sample list
# output:   :return: Calculate Majority Error if "me" selected
# ============================================================================= 

def _calculate_ME(s):
    Maj_l = _select_MajLabel(s[-1])
    me = 1 - _get_s_l(s, Maj_l) / len(s[-1])
    return me

# =============================================================================
# #Helper Function to compute gain on specific feature
# input:
#     :param: s: sample list
# output:   :return: Calculate Gini Index if "gi" selected
# ============================================================================= 

def _calculate_GI(s):
    gi = 1.0
    for label in labels:
        num_s_l = _get_s_l(s, label)
        if num_s_l != 0:
            p_l = num_s_l / len(s[-1])
            gi -= p_l**2
    return gi

# =============================================================================
# #Helper Function to compute s_v sample to specific value
# input:
#     :param: node: node list
#     :param: attribute: attribute
#     :param: value: attribute value
# output:   :return: Calculate s_v
# ============================================================================= 

def _find_s_v(node, attribute, value):
    attr_idx = attributes.index(attribute)
    indices = [i for i, x in enumerate(node.s[attr_idx]) if x == value]
    s_v = node.s.copy()

    for i in range(len(node.s)):
        new_feature_list = []

        for index in indices:
            new_feature_list.append(node.s[i][index])
        s_v[i] = new_feature_list

    return s_v



# =============================================================================
# #Helper Function to compute feature value
# input:
#     :param: s: sample list
#     :param: label: target attribute s[-1]
# output:   :return: Calculate lenth of sample on specific label
# ============================================================================= 
def _get_s_l(s, label):
    return len([i for i, x in enumerate(s[-1]) if x == label])

# =============================================================================
# #Helper Function to compute feature value
# input:
#     :param: s: sample list
#     :param: label: target attribute s[-1]
# output:   :return: Calculate lenth of sample on specific label
# ============================================================================= 
def _split_on_gain(feature, node, a):
    G = []
    for i in range(len(a)):
        G.append(_calculate_gain(node, a[i], feature))
    max_index = G.index(max(G))

    node.set_attribute(a[max_index])
# =============================================================================
# #Helper Function to compute feature value
# input:
#     :param: s_l: sample list 
#     
# output:   :return: majority label
# ============================================================================= 
def _select_MajLabel(s_l):
    count = [0 for _ in range(len(labels))]
    for label in s_l:
        for i in range(len(labels)):
            if label == labels[i]:
                count[i] += 1
                break

    index = count.index(max(count))
    return labels[index]

# =============================================================================
# #Function to implement recursive check tree
# input:
#     :param: node: root node list
#     :param: attr: attribute list
#     :param: branches: branch list
#     :param: level: depth
# output:   :check tree and prints out attributes, branches, it took to get to a label
# ============================================================================= 

def _check_tree(node, attr=[], branches=[], level=0):

    if node.is_leaf:
        pr_attr = ""
        pr_brnch = ""
        for i in attr:
            pr_attr += str(i) + ", "
        for b in branches:
            pr_brnch += b + ", "
        print("ATTRIBUTES: ", pr_attr, "BRANCHES: ", pr_brnch, "LABEL: ", node.label, "LEVEL: ", level)

    else:
        attr.append(node.attribute)
        for branch, child in node.branches.items():
            copy = branches.copy()
            copy.append(branch)
            _check_tree(child, attr.copy(), copy, level+1)

# =============================================================================
# #Function to train a decision tree with the given data, the ID3 algorithm, and the type of feature function given
# input:
#     :param: s: data list
#     :param: feature: feature list :"ig" for information gain. "me" for Majority Error. "gi" for Gini Index.
#     :param: depth: depth of tree
# output:   :return tree 
# ============================================================================= 
            
def _train_data(s, feature, depth=-1):
    tree = Tree(feature, depth)
    tree.set_root(_recursive_ID3(s, None, attributes.copy(), feature, 1, depth))
    return tree
# =============================================================================
# #Function to train a decision tree with the given data, the ID3 algorithm, and the type of feature function given
# input:
#     :param: s: data list
#     :param: root: root node
# output:   :return pred error 
# ============================================================================= 

def _predict(s, root):

    corr = 0
    for index in range(len(s[-1])):
        temp = []
        for l in s:
            temp.append(l[index])
        corr += _predict_example(temp, root)

    return corr/len(s[-1])

# =============================================================================
# #Function to predicts the given sample recursively
# input:
#     :param: ex1 : A single example from the data.
#     :param node: The current node to either split on or predict with.
# output:   :return 0 - correct. 1 - incorrect
# ============================================================================= 


def _predict_example(ex1, node):

    if not node.is_leaf:
        attr_idx = attributes.index(node.attribute)
        child = node.branches[ex1[attr_idx]]
        return _predict_example(ex1, child)
    else:
        if node.label == ex1[-1]: return 0
        else: return 1


# =============================================================================
# #Helper Function to help __main_
# =============================================================================
def _run():
    print("TRAIN:", _predict(train_data, tree.root))
    print("TEST: ", _predict(test_data, tree.root))

# =============================================================================
# #Main function
# 
# output:   :call several helper finctio to build tree using ID3
# =============================================================================     
if __name__ == '__main__':
    DL_select = sys.argv[1]
    feature_select = sys.argv[2]
    
    if len(sys.argv) > 3:
        depth = int(sys.argv[3])
    else:
        depth = -1
        
    attributes = []
    if DL_select == "car" and depth<7:
        attributes = Dataloader.car_attributes
        labels = Dataloader.car_labels
        train_data = Dataloader._load_data(DL_select, True)
        #train_data = Dataloader._car_data()

        test_data = Dataloader._load_data(DL_select, False)
        
        tree = _train_data(train_data, feature=feature_select, depth=depth)
        #print(train_data)

       # _check_tree(tree.root, [], [], 0)
        _run()

        
    elif DL_select == "bank" and depth<17:
        attributes = Dataloader.bank_attributes
        labels = Dataloader.bank_labels
        train_data = Dataloader._load_data(DL_select, True)
        #train_data = Dataloader._car_data()

        test_data = Dataloader._load_data(DL_select, False)
        
        tree = _train_data(train_data, feature=feature_select, depth=depth)
        #print(train_data)

       # _check_tree(tree.root, [], [], 0)
        _run()
    else: 
        print("depth not accepted")

    

    


    





    

    

