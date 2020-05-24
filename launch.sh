#!/bin/bash

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

toLowerCase() {
   echo $( echo $1 | tr '[:upper:]' '[:lower:]' )
}

read -p "Ensure you have install python3, jupyter notebook, pandas, numpy, ta and scipy [y/n]: " chk

chk=$(toLowerCase $chk)

if [ $chk != y ] && [ $chk != yes ]   
then
    echo please install the dependencies first. quitting ...
    exit 1
fi

read -p "enter the currency pair in the format (eg. EURUSD): " currency

for name in `find ./Dataframes -type f -exec basename {} \;`
    do
        basename=${name%%.*}
        if [[ df_$currency = $basename ]]
            then
            read -p "existing forex pair df detected, skip preparation?[y/n]: " skip
        fi
done

skip=$(toLowerCase $skip)


if [[ $skip != "yes" && $skip != "y" ]]
then  prep
fi

read -p "which model do you want to refer to? [LSTM/Classifiers]: " ans
ans=$(toLowerCase $ans)
if [ $ans = 'lstm' ]
then
    echo LSTM chosen, starting jupyter notebook
    cd ./Neural_Networks_Model
    jupyter notebook --no-browser --port 8888 
else
    echo Classifiers chosen, starting jupyter notebook
    cd ./Classifiers_Model
    jupyter notebook --no-browser --port 8888 
fi

if [ $? -eq 0 ]
    then echo successfully launed jupyter notebook\nnavigate to \
        localhost:8888 in browser to have a look 
fi
