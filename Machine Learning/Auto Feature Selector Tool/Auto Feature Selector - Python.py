get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as ss
from collections import Counter
import math
from scipy import stats


# load sample dataset

player_df = pd.read_csv("fifa19.csv")
numcols = ['Overall', 'Crossing','Finishing',  'ShortPassing',  'Dribbling','LongPassing', 'BallControl', 'Acceleration','SprintSpeed', 
           'Agility', 'Stamina','Volleys','FKAccuracy','Reactions','Balance','ShotPower','Strength','LongShots',
           'Aggression','Interceptions']
catcols = ['Preferred Foot','Position','Body Type','Nationality','Weak Foot']
player_df = player_df[numcols+catcols]

traindf = pd.concat([player_df[numcols], pd.get_dummies(player_df[catcols])],axis=1)
features = traindf.columns
traindf = traindf.dropna()
traindf = pd.DataFrame(traindf,columns=features)


# define X and y

y = traindf['Overall']>=87
X = traindf.copy()
del X['Overall']
X.head()
len(X.columns)

feature_name = list(X.columns)
num_feats=30


# feature selection algorithms

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import RFE
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from lightgbm import LGBMClassifier

from sklearn.preprocessing import MinMaxScaler


# Pearson correlation
def cor_selector(X, y,num_feats):
    cor_list = []
    for i in feature_name:
        cor = np.corrcoef(X[i], y)[0, 1]
        cor_list.append(cor)
        
    cor_list = [0 if np.isnan(i) else i for i in cor_list]
    cor_feature = X.iloc[:,np.argsort(np.abs(cor_list))[-num_feats:]].columns.tolist()
    cor_support = [True if i in cor_feature else False for i in feature_name]
    return cor_support, cor_feature


# Chi-squared
def chi_squared_selector(X, y, num_feats):
    X1= MinMaxScaler().fit_transform(X)
    chi_model = SelectKBest(score_func=chi2, k=num_feats)
    chi = chi_model.fit(X1,y)
    
    chi_support = chi.get_support()
    chi_feature = X.loc[:,chi_support].columns.tolist()
    return chi_support, chi_feature


# Recursive Feature Elimination
def rfe_selector(X, y, num_feats):
    X1= MinMaxScaler().fit_transform(X)
    lr = LogisticRegression(solver='lbfgs')
    rfe_model = RFE(estimator=lr, n_features_to_select=num_feats)
    rfe = rfe_model.fit(X1,y)
        
    rfe_support = rfe.get_support()
    rfe_feature = X.loc[:,rfe_support].columns.tolist()
    return rfe_support, rfe_feature


# Embedded Selection: Lasso
def embedded_log_reg_selector(X, y, num_feats):
    lr = LogisticRegression(penalty='l2', solver="lbfgs")
    embedded_log_reg_model = SelectFromModel(estimator=lr, max_features=num_feats)
    embedded_log_reg= embedded_log_reg_model.fit(X, y)
    
    embedded_lr_support = embedded_log_reg.get_support()
    embedded_lr_feature = X.loc[:,embedded_lr_support].columns.tolist()
    return embedded_lr_support, embedded_lr_feature


# Random Forest Classifier
def embedded_rf_selector(X, y, num_feats):
    rf = RandomForestClassifier(n_estimators=100)
    embedded_rf_model = SelectFromModel(rf, max_features=num_feats)
    embedded_rf = embedded_rf_model.fit(X, y)
        
    embedded_rf_support = embedded_rf.get_support()
    embedded_rf_feature = X.loc[:,embedded_rf_support].columns.tolist()
    return embedded_rf_support, embedded_rf_feature


# LightGBM
def embedded_lgbm_selector(X, y, num_feats):
    lgbm = LGBMClassifier(n_estimators=500, learning_rate=0.2)
    lgbm_model = SelectFromModel(lgbm, max_features=num_feats)
    lgbmclassifier = lgbm_model.fit(X, y)    
    
    embedded_lgbm_support = lgbmclassifier.get_support()
    embedded_lgbm_feature = X.loc[:, embedded_lgbm_support].columns.tolist()
    return embedded_lgbm_support, embedded_lgbm_feature



def preprocess_dataset(dataset_path):
    y = traindf['Overall']>=87
    X = traindf.copy()
    del X['Overall']
    num_feats=30
    return X, y, num_feats


def autoFeatureSelector(dataset_path, methods=[]):
 
    X, y, num_feats = preprocess_dataset(dataset_path)
    if 'pearson' in methods:
        cor_support, cor_feature = cor_selector(X, y,num_feats)
    if 'chi-square' in methods:
        chi_support, chi_feature = chi_squared_selector(X, y,num_feats)
    if 'rfe' in methods:
        rfe_support, rfe_feature = rfe_selector(X, y,num_feats)
    if 'log-reg' in methods:
        embedded_lr_support, embedded_lr_feature = embedded_log_reg_selector(X, y, num_feats)
    if 'rf' in methods:
        embedded_rf_support, embedded_rf_feature = embedded_rf_selector(X, y, num_feats)
    if 'lgbm' in methods:
        embedded_lgbm_support, embedded_lgbm_feature = embedded_lgbm_selector(X, y, num_feats)
    
  
    feature_selection_df = pd.DataFrame({'Feature':feature_name, 'Pearson':cor_support, 'Chi-2':chi_support, 'RFE':rfe_support,
                                         'Logistics':embedded_lr_support, 'RandomForest':embedded_rf_support,
                                         'LightGBM':embedded_lgbm_support})
    feature_selection_df['Total'] = np.sum(feature_selection_df, axis=1)
    feature_selection_df = feature_selection_df.sort_values(['Total','Feature'] , ascending=False)
    feature_selection_df.index = range(1, len(feature_selection_df)+1)
    
    best_features = feature_selection_df['Feature'][:5].values.tolist()
    
    
    return best_features

best_features = autoFeatureSelector(dataset_path="data/fifa19.csv", methods=['pearson', 'chi-square', 'rfe', 'log-reg', 'rf', 'lgbm'])
print(best_features)

