import os
os.chdir('C:\Users\Remi\Desktop\Datascience\Titanic')

import pandas as pd
import numpy as np
import csv as csv
import pylab as plt

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot

# Load the train data file
train_data = pd.read_csv('data/train.csv', header=0)
train_data.head(n=10)
train_data = train_data.set_index('PassengerId')
train_data.head(n=10)
train_data.describe()

# Load the test data file
test_data = pd.read_csv('data/test.csv', header=0)
test_data.head(n=10)
test_data = test_data.set_index('PassengerId')

# Size of the sample: 891 rows 
# Variables: 
#   - PassengerId: id of the passenger (key)
#   - Survived: target, 0 or 1
#
#   - Name: name of the passenger (text)
#   - Cabin: cabin number of the passenger (text)   
#   - Ticket: ticket reference contains info on Embarked (text). Examples: 
#       * when starts with C or W or STON or SOTON  then Embarked at S
#       * when contains PARIS                       then Embarked at C
#       * when contains S.O.*                       then Embarked at S
#       * when starts with PC                       then Embarked at S
#       * when contains A/*                         then Embarked at S
#
#   - Sex: sex of the passenger, male of female (discrete)
#   - Embarked: where the passenger embarked, Cherbourg, Queenstown or Southampton (discrete, 2 missing)
#   - Pclass: class of the passenger, 1: high, 2: medium, 3: low (discrete ordered)
# 
#   - Age: age of the passenger (quantitative 177 missing values, ~20%)
#   - SibSp: number of siblings and spouse (quantitative)
#   - Parch: number of parents and childs (quantitative)
#   - Fare: price of the ticket (quantitative)

# Age
pyplot.hist(train_data['Age'], bins=np.linspace(0, 100, 100), color='green', alpha=0.5)

# Pclass
print train_data['Pclass'].value_counts()
print len(train_data['Pclass'][ train_data['Pclass'].isnull()] )

# Sex
print train_data['Sex'].value_counts()
print len(train_data['Sex'][ train_data['Sex'].isnull()] )

# Embarked, 2 missing values
print train_data['Embarked'].value_counts()
print len(train_data['Embarked'][ train_data['Embarked'].isnull()] )

# Cabin
print train_data['Cabin'].value_counts()
print len(train_data['Cabin'][ train_data['Cabin'].isnull()] )


# Plot histogram depending on the survival
def plot_histogram(data, variable, bins=20):
    survived = data[data.Survived == 1]
    dead = data[data.Survived == 0]
    
    x1 = dead[variable].dropna()
    x2 = survived[variable].dropna()
    plt.hist( [x1,x2], label=['Dead','Survived'], color=['red','blue'], bins=bins)
    plt.legend(loc='upper left')
    plt.show()


plot_histogram(data=train_data, variable='Pclass')
plot_histogram(data=train_data[train_data['Sex']=='male'], variable='Pclass')
plot_histogram(data=train_data[train_data['Sex']=='female'], variable='Pclass')

plot_histogram(data=train_data, variable='Age')
plot_histogram(data=train_data[train_data['Sex']=='male'], variable='Age')
plot_histogram(data=train_data[train_data['Sex']=='female'], variable='Age')

plot_histogram(data=train_data, variable='Fare')
plot_histogram(data=train_data[train_data['Sex']=='male'], variable='Fare')
plot_histogram(data=train_data[train_data['Sex']=='female'], variable='Fare')

# Main comments
# * PClass
#       Overall: 
#           High probability of survival for PClass 1, 
#           High probability of death PClass 3
#       Drilldown by sex:
#           Male: have a higher survival rate for PClass 1
#           Female: have a high proba of survival, except for PClass 3
# * Age
#       Overall: Young and old ages have a high probability of survival
#       Drilldown by sex:
#           Male: have a higher survival rate only for young ages
#           Female: have consistently a high survival rate for all ages


# Adding other variables
train_data_2 = train_data.copy()
test_data_2 = test_data.copy()

def create_features (X):
  
    X['Age'] = X['Age'].fillna(X['Age'].median())
    X['Fare'] = X['Fare'].fillna(X['Fare'].median())
    X['Embarked'] = X['Embarked'].fillna('S')
    
    X['Nickname']       = X['Name'].map( lambda x: x.find('(') > -1 or x.find('"') > -1 )

    X['Name_len']       = X['Name'].map( lambda x: len(x) )
    X['FamSize']        = X['Parch'] + X['SibSp']
    
    
    dummy_variables = ['Pclass', 'Sex', 'Embarked', 'Nickname']
    for variable in dummy_variables:
        dummy_cols = pd.get_dummies(X[variable], prefix=variable)
        X = X.join(dummy_cols)
        del X[variable]
       
    deleted_variables = ['Name', 'Cabin', 'Ticket']
    for variable in deleted_variables:
        del X[variable]

    return X


y_train = train_data_2['Survived']
del train_data_2['Survived']
X_train = create_features(train_data_2.copy())
# X_train.head(10)

# Logit model and random forest
logit_model = LogisticRegression()
logit_model.fit(X_train, y_train)

rf_model = RandomForestClassifier(n_estimators=300, criterion='gini', n_jobs=-1)
rf_model.fit(X_train, y_train)

# Cross validation to assess the model (20 cross validations)
score_logit = cross_val_score(logit_model, X_train, y_train, cv=4)
score_rf = cross_val_score(rf_model, X_train, y_train, cv=4)
print '[Score] Logit: \t\t' + str( round(np.mean(score_logit)*100, 2) ) + ' %'
print '[Score] Random Forest: \t' + str( round(np.mean(score_rf)*100, 2) ) + ' %'

# Random forest is better


# Prediction with the test and Kaggle dashboard
test_data_2.head(10)

X_test = create_features(test_data_2)
X_test.head(10)

# Prediction with the random forest
output_predicted = rf_model.predict(X_test).astype(int)

test_file = open("data/test_pred.csv", "wb")
open_file_object = csv.writer(test_file)
open_file_object.writerow(["PassengerId", "Survived"])
open_file_object.writerows(zip(test_data_2.index.values, output_predicted))
test_file.close()





