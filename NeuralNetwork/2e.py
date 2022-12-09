#!/usr/bin/env python
# coding: utf-8

# In[7]:


# import Library
import numpy as np
import os


# In[8]:


import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.preprocessing import normalize


# In[9]:


print( np.__version__)
print( tf.__version__)


# ## Import data

# In[133]:


raw_tr = np.loadtxt(os.path.join('./bank-note', 'train.csv'), delimiter=',')
raw_te = np.loadtxt(os.path.join('./bank-note', 'test.csv'), delimiter=',')

Xtr, ytr, Xte, yte = raw_tr[:,:-1], np.expand_dims(raw_tr[:,-1], axis=1), raw_te[:,:-1],np.expand_dims(raw_te[:,-1], axis=1)

print(Xtr.shape, ytr.shape, Xte.shape, yte.shape)        
        


# In[134]:


Xtr = normalize(Xtr, axis =0)
Xte = normalize(Xte, axis =0)


# ## Neural Network model

# In[135]:


def create_nn_model(curr_depth, curr_width, act_func):
    model = Sequential()
    if act_func == 'relu': initializer = keras.initializers.he_normal()
    else: initializer = keras.initializers.glorot_normal()
        
    # Add layers
    for _ in range(curr_depth-1):
        model.add(Dense(curr_width, activation=Activation(act_func), kernel_initializer=initializer))
    model.add(Dense(1, activation=Activation('sigmoid'), kernel_initializer=initializer))
    
    # Set loss and optimizer
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model


# ## Check For Best Model Depending Width/Height based on accuracy

# In[137]:


def is_smallest_width_model(curr_width, accuracy, highest_acc):
    return accuracy > highest_acc[-1]             or (accuracy == highest_acc[-1] and curr_width < highest_acc[1])

def is_smallest_depth_model(curr_depth, accuracy, highest_acc):
    return accuracy > highest_acc[-1]             or (accuracy == highest_acc[-1] and curr_depth < highest_acc[0])


# ## train, test and best model reurn

# In[139]:


def train_and_test_model(curr_depth, curr_width, act_func, highest_acc, smallest):
    model = create_nn_model(curr_depth, curr_width, act_func)
            
    # Train
    model.fit(Xtr, ytr, epochs=10, verbose=0)
    
    # Test
    evaluation = model.evaluate(Xte, yte, verbose=0)
    loss = evaluation[0]
    accuracy = evaluation[1]
    
    print("DEPTH", curr_depth, ", WIDTH", curr_width, ", Error", loss,", ACCURACY", accuracy)
    
    # Return the highest accuracy model with the smallest width/depth
    if smallest == 'width' and is_smallest_width_model(curr_width, accuracy, highest_acc):
        return [curr_depth, curr_width, accuracy]
    
    elif smallest == 'depth' and is_smallest_depth_model(curr_depth, accuracy, highest_acc):
        return [curr_depth, curr_width, accuracy]
    
    else:
        return highest_acc


# ## run for each depth and width

# In[140]:


def run_nn(act_func, lowest):
    best_model = [0., 0., 0.]
    
    for depth in [3,5,9]:
        print(".............................................................................")
        for width in [5, 10,25,50,100]:
            best_model = train_and_test_model(depth, width, act_func, best_model, lowest)
            
    return best_model


# ## pass activation and parameter

# In[142]:


print("=======================RELU=======DEPTH=============RELU========DEPTH================================================")
highest_acc = run_nn('relu', 'depth')
print("==================================================================================================")
print("HIGHEST:", highest_acc)
print("==================================================================================================")
print("==================================================================================================")
print("==================RELU============WIDTH===========RELU==========WIDTH================================================")
highest_acc = run_nn('relu', 'width')
print("==================================================================================================")
print("HIGHEST:", highest_acc)
print("==================================================================================================")
print("==================================================================================================")
print("=================TANH=============DEPTH=========TANH============DEPTH================================================")
highest_acc = run_nn('tanh', 'depth')
print("==================================================================================================")
print("HIGHEST:", highest_acc)
print("==================================================================================================")
print("==================================================================================================")
print("=================TANH=============WIDTH=========TANH============WIDTH================================================")
highest_acc = run_nn('tanh', 'width')
print("==================================================================================================")
print("HIGHEST:", highest_acc)


# In[ ]:




