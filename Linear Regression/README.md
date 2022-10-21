# Linear Regression
This is the Least Mean Squares algorithm. It is optimized by Stochastic Gradient Descent and Batch Gradient Descent.

## Least Mean Squares
### Cost Function
<img src="https://github.com/solosoren/CS5350-MachineLearning/blob/master/LinearRegression/Images/Cost.png" height="75">  

## Batch Gradient Descent
Uses the gradient of the Least Mean Squares loss function to minimize the cost. The algorithm is said to converge when ||new weight vector - prev weight vector|| is less than 10e-6. 
### How To Run
```
python3 LR.py bgd
```
###Results
included in PDF
## Stochastic Gradient Descent
Uses the gradient of the Least Mean Squares loss function to minimize the cost. The algorithm is said to converge when ||new weight vector - prev weight vector|| is less than 10e-10. 
### How To Run
```
python3 LinearRegression.py sgd
```
###Results
included in PDF

## Data
The dataset is from [UCI repository](https://archive.ics.uci.edu/ml/datasets/Concrete+Slump+Test). This dataset contains 7 concrete features and is used to calculate the SLUMP of the concrete. There are 53 training examples and 50 test examples.
#### Attributes and Labels
1. Cement
2. Slag
3. Fly ash
4. Water
5. SP
6. Coarse Aggr
7. Fine Aggr

