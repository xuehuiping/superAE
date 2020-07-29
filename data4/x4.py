# -*- coding: utf-8 -*-
# author: huihui
# date: 2020/7/29 6:28 下午 

'''切分训练集和验证集'''

from sklearn.model_selection import train_test_split

X = open('article.txt').readlines()
y = open('summary.txt').readlines()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

with open('train.src', 'w') as f:
    f.writelines(X_train)

with open('train.tgt', 'w') as f:
    f.writelines(y_train)

with open('valid.src', 'w') as f:
    f.writelines(X_test)

with open('valid.tgt', 'w') as f:
    f.writelines(y_test)