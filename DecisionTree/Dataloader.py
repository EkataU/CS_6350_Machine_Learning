#Author: Ekata Mitra
# =============================================================================
# CS 5350/6350: Machine Learining Fall 2022:
# HW1: Section 2
# Question 2 and 3
# =============================================================================

# =============================================================================
# Step 1: Visualize Dataset (car, bank)
# Step 2: Several Helper Function 

# =============================================================================

import statistics

# =============================================================================
# Step 1: Visualize Dataset (car, bank)

# Car dataset
# =============================================================================
# list of attributes
car_attributes = [
    ["vhigh", "high", "med", "low"],
    ["vhigh", "high", "med", "low", "."],
    ["2", "3", "4", "5more"],
    ["2", "4", "more"],
    ["small", "med", "big"],
    ["low", "med", "high"]
]

# list of target attributes
car_labels = ["unacc", "acc", "good", "vgood"]

# Bank dataset
# list of attributes
bank_attributes = [
    ["numeric", "leq", "over"],
    ["admin.", "unknown", "unemployed", "management", "housemaid", "entrepreneur", "student",
        "blue-collar", "self-employed", "retired", "technician", "services"],
    ["married", "divorced", "single"],
    ["unknown", "secondary", "primary", "tertiary"],
    ["yes", "no"],
    ["numeric", "leq", "over"],
    ["yes", "no"],
    ["yes", "no"],
    ["unknown", "telephone", "cellular"],
    ["numeric", "leq", "over"],
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"],
    ["numeric", "leq", "over"],
    ["numeric", "leq", "over"],
    ["numeric", "leq", "over"],
    ["numeric", "leq", "over"],
    ["unknown", "other", "failure", "success"]
]

# list of target attributes
bank_labels = ["yes", "no"]
maj_atr = []
# =============================================================================
# # Step 2: Several Helper Functions
# =============================================================================

# =============================================================================
# # Function: This function imports the data from a csv file as list
# input:
#     :param: dir_loc: dir_loc to import sample data (s)
#           : train : type of dataset
# output:   :return: the data as a list of lists that contain all the example values
#                    for an attribute or label (at s[-1]).
# =============================================================================
def _load_data(dir_loc, train):
    s =[] 
    if train:
        CSVfile = "../DecisionTree/" + dir_loc + "/train.csv"
    else:
        CSVfile = "../DecisionTree/" + dir_loc + "/test.csv"
        
    with open(CSVfile, 'r') as f:
        
        num_tot_attribute = 0
        for line in f:
            terms = line.strip().split(',')
            num_tot_attribute = len(terms)
            break

        s = [[] for _ in range(num_tot_attribute)]

        for line in f:
            terms = line.strip().split(',')
            for i in range(num_tot_attribute):
                s[i].append(terms[i])
                
    if dir_loc == "bank":
        attributes = bank_attributes
        temp = _change_NumAttr_to_BinAttr(s, attributes)
        s = _change_MissAttr_to_MajAttr(temp, attributes, train)
    return s

# =============================================================================
# # Function: - Check all numeric attributes
#             - Compute the median
#             - Update the attributes to contain the median
#             - Update all example to "leq", for equal to or less 
#             - Update "over" for the numeric attributes.
# input:
#     :param: s: the entire dataset
#     :param attributes: all attributes     
# output:    
#           return: the updated dataset
# =============================================================================

def _change_NumAttr_to_BinAttr(s, attributes):
    for i in range(len(attributes)):

        if attributes[i][0] == "numeric":
            median = _get_median(s[i]) # Compute the median
            attributes[i][0] = str(median)
            s[i] = _update_NumAttr(s[i], attributes[i]) #Update all example to "leq", for equal to or less

        elif _is_NumAttr(attributes[i]):
            s[i] = _update_NumAttr(s[i], attributes[i]) # Update "over" for the numeric attributes.
    return s

# =============================================================================
# # Helper Function to  _change_NumAttr_to_BinAttr for Bank dataset:
#             - Check bank_attributes is numeric or not
#
# input:
#     :param: attribute: the attrbute list
#         
# output:    
#           return: boolean "True" or "False"
# =============================================================================
def _is_NumAttr(attribute):
    try:
        int(attribute[0])
        return True
    except ValueError:
        return False

# =============================================================================
# # Helper Function to  _change_NumAttr_to_BinAttr for Bank dataset:
#             - Compute the median of the set
#
# input:
#     :param: val_a : value at a numeric attribute
#         
# output:    
#           return: median 
# =============================================================================

def _get_median(val_a):
    int_val = list(map(int, val_a))  # str to num
    median = statistics.median(int_val)
    return median

# =============================================================================
# # Helper Function to  _change_NumAttr_to_BinAttr for Bank dataset:
#             - Update all example to "leq", for equal to or less 
#             - Update "over" for the numeric attributes.
# input:
#     :param: val_a : value at a numeric attribute
#     :param: attribute: the attrbute list    
# output:    
#           return: binary attribute 
# =============================================================================

def _update_NumAttr(val_a, attribute):
    for i in range(len(val_a)):
        if int(val_a[i]) > int(attribute[0]): val_a[i] = "over"
        else: val_a[i] = "leq"
    return val_a

# =============================================================================
# # Function: - Check all missing attributes["unknown"]
#             - Compute the majority
#             - Update the missing attributes to majority attribute
# input:
#     :param: s: the entire dataset
#     :param: attributes: all attributes
#     :param: data_type: train only
# output:    
#           return: the updated dataset
# =============================================================================

def _change_MissAttr_to_MajAttr(s, attributes, train):
    
    for i in range(len(attributes)):

        if train:
            maj_atr.append("")
            if "unknown" in attributes[i]:
                MajAttr = _find_MajAttr(s[i], attributes[i])
                maj_atr[i] = MajAttr

                for j in range(len(s[i])):
                    if s[i][j] == "unknown":
                        s[i][j] = MajAttr

        elif "unknown" in attributes[i]:
            for j in range(len(s[i])):
                if s[i][j] == "unknown":
                    s[i][j] = maj_atr[i]

    return s

# =============================================================================
# # Helper Function: 
#             - Compute the majority
# input:
#     :param: val_a : value at a numeric attribute
#     :param: attribute: the attrbute list 
# output:    
#           return: majority attribute value
# =============================================================================

def _find_MajAttr(val_a, attribute):
    
    cnt = [0 for _ in range(len(attribute))]

    for val in val_a:
        for i in range(len(attribute)):

            if val == attribute[i] and attribute[i] != "unknown":
                cnt[i] += 1
                break

    inx = cnt.index(max(cnt))
    return attribute[inx]

# visualize car example 
def _car_data():

    return [
        ["low", "med"],
        ["high", "high"],
        ["5more", "5more"],
        ["4", "4"],
        ["med", "med"],
        ["high", "high"],
        ["vgood", "good"]
    ] # 2 examples

# visualize bank example

def _bank_data():
    s = [
        ["48","48"],
        ["services","blue-collar"],
        ["married", "married"],
        ["secondary", "secondary"],
        ["no", "no"],
        ["0", "0"],
        ["yes", "yes"],
        ["no", "no"],
        ["unknown", "unknown"],
        ["5", "5"],
        ["may", "may"],
        ["114", "114"],
        ["2", "2"],
        ["-1", "-1"],
        ["0", "0"],
        ["unknown", "unknown"],
        ["no", "no"],
    ] # 2 examples
    s = _change_NumAttr_to_BinAttr(s)
    return s