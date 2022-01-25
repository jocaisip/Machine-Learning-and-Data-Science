## Overview and Description

This project involves building a neural network NLP model that reads statements containing the reason the person is happy and classifies them into categories such as 'leisure', 'affection', and 'achievement'.  

Text statements are cleaned by filtering unnecessary characters and using preprocessing techniques lemmatization and removing stopwords. 

TF-IDF is the feature extraction method used for tokenization and vectorization. With the features and labels extracted, the data is then split and trained on a Bidirectional LSTM model.

The dataset is courtesy of the [Happiness Type](https://www.kaggle.com/sourabhbaldwa/bonding) dataset from Kaggle. 

