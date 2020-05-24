#!/bin/bash
read -p "Ensure you have install python3, jupyter notebook, pandas, numpy, ta and scipy [y/n]: " chk

chk=$( echo $chk | tr '[:upper:]' '[:lower:]' )
 
if [ $chk != y ] && [ $chk != yes ]   
then
    echo please install the dependencies first. quitting ...
    exit 1
fi

read -p "enter the currency pair in the format (EURUSD): " currency

for name in `find ./Dataframes -type f -exec basename {} \;`
    do
        basename=${name%%.*}
        if [[ df_$currency = $basename ]]
            then
            read -p "existing forex pair df detected, skip preparation?[y/n]:" skip
        fi
done

skip=$( echo $skip | tr '[:upper:]' '[:lower:]' )


prep() {
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
        then echo data successfully prepared
    else
        echo error handling data preparation
    fi
}

if [[ $skip != "yes" && $skip != "y" ]]
then  prep
fi

    read -p "which model do you want to refer to? [LSTM/Classifiers]: " ans
    ans=$(echo $ans | tr '[:upper:]' '[:lower:]')
    if [ $ans = 'lstm' ]
    then
        echo LSTM chosen, starting jupyter notebook
        jupyter notebook --no-browser --port 8888 ./Neural_Networks_Model/LSTM_Template.ipynb
    else
        echo Classifiers chosen, starting jupyter notebook
        jupyter notebook --no-browser --port 8888 ./Classifiers_Model/Classifiers_Template.ipynb
    fi

    if [ $? -eq 0 ]
       then echo successfully launed jupyter notebook\nnavigate to \
            localhost:8888 in browser to have a look 
    fi
