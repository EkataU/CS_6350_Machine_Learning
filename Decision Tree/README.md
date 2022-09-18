# Decision Tree
This is an ID3 Decision Tree learning algorithm for two evaluation tasks. There are three types of purity used: Entropy, Majority Error, and Gini Index.

## Car
The dataset is from the [UCI repository](https://archive.ics.uci.edu/ml/datasets/car+evaluation). 

**Data Set Characteristics**:  Multivariate

**Number of Instances**:1728

**Out of 1728:**
Test Instances: 728 Train Instances: 1000



#### Attributes and Labels:
- Buying - Very High, High, Medium, Low
- Maintenance - Very High, High, Medium, Low
- Number of Doors - 2, 3, 4, 5+
- Persons - 2, 4, More than 4
- Lug Boot - Big, Medium, Small
- Safety - High, Medium, Small
- Label - Unacceptable, Acceptable, Good, Very Good
### How To Run
`python3 ID3.py car ig`

To change the purity, replace ig with any of the following:

Information Gain: ig
Majority Error: me
Gini Index: gi
If you would like to add a depth constraint to the tree, add the depth to the end of the line.
Ex: `python3 ID3.py car ig 2`

## Bank
The dataset is from [UCI repository](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing). This dataset contains 16 bank attributes for a given customer, including both numerical and categorical ones. 
**Data-Description:** 
- The numerical attributes set to be equal to or under the median value, or above the median. 
- Any missing attributes set to be the majority attribute. 
- The label is whether the client subscribed to a term deposit. 

**Data Set Characteristics: ** Multivariate

**Number of Instances:** 10,000
**Out of 10,000:**
Test Instances: 5,000 Train Instances: 5,000

#### Attributes and Labels
- Age - (numeric)
- Job - admin., unknown, unemployed, management, housemaid, entrepreneur, student, blue-collar, self-employed, retired, technician, services
- Marital - married, divorced, single
- Education - unknown, secondary, primary, tertiary
- Default - yes, no
- Balance - (numeric)
- Housing - yes, no
- Loan - yes, no
- Contact - unknown, telephone, cellular
- Day - (numeric)
- Month - jan, feb, mar, ..., nov, dec
- Duration - (numeric)
- Campaign - (numeric)
- Pdays - (numeric) -1 means client was not previously contacted
- Previous - (numeric)
- Poutcome - unknown, other, failure, success
- Label - yes, no
#### How To Run
`python3 ID3.py bank ig`

As above, to change the purity, replace ig with any of the following:

Information Gain: ig
Majority Error: me
Gini Index: gi
If you would like to add a depth constraint to the tree, add the depth to the end of the line.
Ex: `python3 ID3.py car ig 2`

Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Sta
