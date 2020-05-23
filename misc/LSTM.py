#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created for the NUS Investment Club 2020 Project

@author: Zhou Zijian
@author: Sean Gee
"""

# import all libraries
import numpy as np
import pandas as pd
import matplotlib.pyploy as plt
import os
from sklearn.preprocessing import MinMaxScaler
from keras.layers import Dense, LSTM
from keras.models import Sequential, load_model

# initialize by specifying the file path
class LSMTClassifier:
    def __init__(self, file):
        self.batch_size = 512
        self.epoch = 10
        self.lookback = 50
        self.test_size = 0
        self.df = None
        self.model = None
        self.X = None
        self.y = None
        self.X_test = None
        self.file = file
        self.sc = MinMaxScaler(feature_range = (-1, 1))
    
    def getDataFrameFromFilePath(self):
        self.df = pd.read_csv(self.file)
    
    def getTrainingSets(self):
        
        data = self.df
        input_features = data.iloc[:, [2,3]].values
        input_data = input_features
        
        sc = MinMaxScaler(feature_range = (-1, 1))
        
        # normalize data
        input_data[:,0:2] = sc.fit_transform(input_features[:,:])
        
        X = []
        y = []
        for i in range(len(data) - self.lookback - 1):
            t = []
            for j in range(0, self.lookback):
                t.append(input_data[[(i + j)], :])
            X.append(t)
            y.append(input_data[i + self.lookback, 1])
            
        self.X, self.y = np.array(X), np.array(y)
        self.X_test = X[ : self.test_size + self.lookback]
        self.X = self.X.reshape(X.shape[0], self.lookback, 2)
        self.X_test = self.X_test.reshape(self.X_test.shape[0], self.lookback, 2)
        
        
    
    def getModelFromFilePath(self):
        # get training set for data first
        self.getTrainingSets(self)
        
        # use existed model or create from scratch
        if os.path.exists(self.file):
            	self.model = load_model(self.file)
        else:
            self.model = Sequential()
            self.model.add(LSTM(units=30, return_sequences= True, input_shape=(self.X.shape[1],2)))
            self.model.add(LSTM(units=30, return_sequences=True))
            self.model.add(LSTM(units=30))
            self.model.add(Dense(units=1))
            self.model.compile(optimizer='adam', loss='mean_squared_error')
            self.model.fit(self.X, self.y, epochs=self.epoch, batch_size=self.batch_size)
            self.model.save(self.file)
        
    
    def getPredictedPriceNormalized(self):
        # get model first
        self.getModelFromFilePath(self, self.file)
        input_features = self.df.iloc[:, [2,3]].values
        input_data = input_features
        
        predicted_value= self.model.predict(self.X_test)
        plt.figure(figsize=(100,40))
        plt.plot(predicted_value, color= 'red')
        plt.plot(input_data[self.lookback : self.test_size + (2 * self.lookback), 1], color='green')
        plt.title("Opening price of stocks sold")
        plt.xlabel("Time (latest-> oldest)")
        plt.ylabel("Stock Opening Price")
        plt.show()
        
        self.sc.inverse_transform(input_features[self.lookback : self.test_size + (2 * self.lookback)])
        return predicted_value
    
    # calculate sharpe ratio
    def getSharpeRatio(self): 
        predicted_value = self.getPredictedPriceNormalized(self, self.file)
        test = self.df[['open']][self.lookback : self.test_size + (2 * self.lookback)]
        test['next'] = test['open'].shift(1)
        test['diff'] = test['next'] - test['open']
        diff = test['diff'].to_numpy()
        diff[0] = 0
        diff = diff.reshape(diff.shape[0],1)
    
        profit = []
        for i in range(diff.shape[0]):
            profit.append(diff[i][0] * predicted_value[i][0])
    
        profit = np.array(profit)
        sharpe = np.sqrt(252) * profit.mean() / profit.std()
        return sharpe
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    