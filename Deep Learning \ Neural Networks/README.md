## Overview and Description

### Happiness Classifier

This project involves building a NLP neural network model that reads statements containing the reason the person is happy and classifies them into categories such as 'leisure', 'affection', and 'achievement'.  

Text statements are cleaned by filtering unnecessary characters and using preprocessing techniques lemmatization and removing stopwords. 

TF-IDF is the feature extraction method used for tokenization and vectorization. With the features and labels extracted, the data is then split and trained on a Bidirectional LSTM model.

The dataset is courtesy of the [Happiness Type](https://www.kaggle.com/sourabhbaldwa/bonding) dataset from Kaggle.




### Audio Language and Gender Recognition

Audio is classified in three language categories - Spanish, English, and German, and two gender categories - Male and Female, for a total of six possible classifications. 

Features extraction methods include the commonly used Mel spectrogram and MFCC features, the combined MFCC (MFCC + delta-delta MFCC) feature was selected as input features. 
Labels are first encoded with Label Encoder to transform labels into integers and then encoded with One Hot Encoder for the final input labels.

Convolutional neural networks (CNN) are very effective on computer vision and image modeling. Since MFCC are image representations of audio, the CNN model architecture was selected in building the deep learning model. Results for this model show an impressive 99% for train and validation accuracy, but the test accuracy of 83% could be further improved.

LSTM (Long short term memory), which is a recurrent neural network (RNN) is the second model architecture used in training this model. This model had produced a high loss rate and  only achieved a test accuracy of 28%. Further steps to improve the accuracy can be through training on other audio features and increasing the dataset size, as well as optimizing the model.

Dataset is courtesy of the [spoken language dataset](https://www.kaggle.com/toponowicz/spoken-language-identification) by [tomasz-oponowicz](https://github.com/tomasz-oponowicz).
