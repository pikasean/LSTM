#!/bin/sh
echo "Ensure you have install python3, jupyter notebook, pandas, numpy, ta and scipy [y/n]"

read confirm

confirm=$( echo $confirm | tr '[:upper:]' '[:lower:]' )
 
if [ $confirm != y ] && [ $confirm != yes ]   
then
    echo please install the dependencies first. quitting ...
    exit 1
fi

echo "enter the currency pair in the format (EURUSD): "
read currency

echo determining python3 path
which python3

if [ $? -eq 0 ]
then
    python3 ./DataPreparation.py $currency
else
    echo python3 not detected. using python instead
    python ./DataPreparation.py $currency
fi

if [ $? -eq 0 ] 
then
    echo "data successfully prepared,"
    echo "which model do you want to refer to? : [LSTM/Classifiers]"
    read ans
    ans=$(echo $ans | tr '[:upper:]' '[:lower:]')
    if [ ans == LSTM ]
    then
        echo "LSTM chosen, starting jupyter notebook"
        jupyter notebook ./Neural_Networks_Model/LSTM_Template.ipynb
    else
        echo "Classifiers chosen, starting jupyter notebook"
        jupyter notebook ./Classifiers_Model/Classifiers_GBPUSD.ipynb
    fi
else
    echo error handling data preparation
fi
