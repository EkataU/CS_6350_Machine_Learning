# Decision Tree
This is an ID3 Decision Tree learning algorithm for two evaluation tasks. There are three types of purity used: Entropy, Majority Error, and Gini Index.

## Car
The dataset is from the [UCI repository]. In this task, we have 6 car attributes, and the label is the evaluation of the car. There are 1000 training examples and 728 test examples.

Attributes and Labels
Buying - Very High, High, Medium, Low
Maintenance - Very High, High, Medium, Low
Number of Doors - 2, 3, 4, 5+
Persons - 2, 4, More than 4
Lug Boot - Big, Medium, Small
Safety - High, Medium, Small
Label - Unacceptable, Acceptable, Good, Very Good
How To Run
python3 ID3.py car ig
To change the purity, replace ig with any of the following:

Information Gain: ig
Majority Error: me
Gini Index: gi
If you would like to add a depth constraint to the tree, add the depth to the end of the line.
Ex: python3 ID3.py car ig 2

## Bank
The dataset is from UCI repository. This dataset contains 16 bank attributes for a given customer, including both numerical and categorical ones. The numerical attributes were altered to be equal to or under the median value, or above the median. Any unknown attributes were altered to be the majority attribute. The label is whether the client subscribed to a term deposit. There are 5000 training examples and 5000 test examples.

Attributes and Labels
Age - (numeric)
Job - admin., unknown, unemployed, management, housemaid, entrepreneur, student, blue-collar, self-employed, retired, technician, services
Marital - married, divorced, single
Education - unknown, secondary, primary, tertiary
Default - yes, no
Balance - (numeric)
Housing - yes, no
Loan - yes, no
Contact - unknown, telephone, cellular
Day - (numeric)
Month - jan, feb, mar, ..., nov, dec
Duration - (numeric)
Campaign - (numeric)
Pdays - (numeric) -1 means client was not previously contacted
Previous - (numeric)
Poutcome - unknown, other, failure, success
Label - yes, no
How To Run
python3 ID3.py bank ig
As above, to change the purity, replace ig with any of the following:

Information Gain: ig
Majority Error: me
Gini Index: gi
If you would like to add a depth constraint to the tree, add the depth to the end of the line.
Ex: python3 ID3.py bank ig 2

Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Sta
