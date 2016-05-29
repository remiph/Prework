import os
os.chdir('C:\Users\Remi\Desktop\Datascience\Titanic')

import pandas as pd
import numpy as np
import csv as csv

from sklearn.linear_model import LogisticRegression

# Load the train / test data file
train_data = pd.read_csv('data/train.csv', header=0)
test_data = pd.read_csv('data/test.csv', header=0)

train_data.head(n=10)
test_data.head(n=10)

train_data = train_data.set_index('PassengerId')
test_data = test_data.set_index('PassengerId')

train_data.head(n=10)
train_data.describe()

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


# Test model with quantitative variables
train_data_2 = train_data.copy()
X_train, y_train = train_data_2[['SibSp', 'Parch', 'Fare']], train_data_2['Survived']

# First shot with a simple model
logit_model = LogisticRegression()
logit_model.fit(X_train, y_train)
print logit_model.coef_

# Prediction with the test and Kaggle dashboard
test_data_2 = test_data.copy()
print len(test_data_2['SibSp'][ test_data_2['SibSp'].isnull()] )
print len(test_data_2['Parch'][ test_data_2['Parch'].isnull()] )
print len(test_data_2['Fare'][ test_data_2['Fare'].isnull()] )
test_data_2['Fare'] = test_data_2['Fare'].fillna(test_data_2['Fare'].median())

output_predicted = logit_model.predict(test_data_2[['SibSp', 'Parch', 'Fare']]).astype(int)
test_data_2['Predict'] = output_predicted

test_file = open("data/test_pred.csv", "wb")
open_file_object = csv.writer(test_file)
open_file_object.writerow(["PassengerId", "Survived"])
open_file_object.writerows(zip(test_data_2.index.values, output_predicted))
test_file.close()





