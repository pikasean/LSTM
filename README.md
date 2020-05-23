# NUS-Invest
This repository contains resources used for the research project under NUS-Invest.

## Using this repo
### test using your own dataset
- Ensure you have installed python (preferably python 3) and jupyter notebook
- Ensure you have also installed pandas, numpy, ta and scipy
- Add the data of the forex pair you want to use inside FX_Data.
Or if your data is present in the current repo, there is no need to add again.
- execute `launch.sh` by `sudo ./launch.sh`
- specify the currency pair and the model you want to use.
- the bash file will help you prepare the dataframes and direct you to jupyter notebook.
### see result for existing datasets
- navigate to `Classifiers_Model` or `Neural_Networks_Model` to see all results we have.

## Using LSTM for Forex Trading
- Using keras for machine learning and scikit-learn for data crunching
- The main code is in /Neural Networks/LSTM.jpynb. You would need Jupyter Notebook to edit the code after cloning it to your local machine.
- The `sharpe ratio` calculated is `1.29` (which is fairly good). The `maximum drawdown` is at 2400, which is quite small as compared to the 
total profit under our trading strategy designed based on the prediction model.

## Using classifiers to analysis Forex
- We created a meta-classifier by combining Random Forest, Xg-boost and SVM through logistic regression. 

- The next step would be to train models on the the features and carry out feature selection.

## Link to Research Paper
- Follow this [link](https://docs.google.com/document/d/1pXo8aAMOx-z-drCUTaYkVPKRNU2WE8aZyOjxHjqPfz8/edit#heading=h.u6qfjxirpk2l)

## Contributors:
```
Zhou Zijian
Sean Gee
Joe Teddy
Huang Linhang
Cao Yuchen
```
