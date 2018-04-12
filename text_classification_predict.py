#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from model.svm_model import SVMModel

class TextClassificationPredict(object):
    def __init__(self):
        self.test = None

    def get_train_data(self):
        train_data = []
        fr_train = open('generated_files/cleanDataTrainVi.txt')
        for line in iter(fr_train.readline, ''):
            string_feature = unicode(line.rstrip(),"utf-8")

            string_target = unicode(fr_train.readline().rstrip(),"utf-8)")
            train_data.append({"feature": string_feature, "target": string_target})
        df_train = pd.DataFrame(train_data)


        #test data
        test_data = []
        accuracy = []

        fr_test = open('generated_files/cleanDataTestVi.txt')
        for line in iter(fr_test.readline, ''):
            string_feature = unicode(line.rstrip(),"utf-8")
            string_target = unicode(fr_test.readline().rstrip(),"utf-8)")
            accuracy.append(string_target)
            test_data.append({"feature": string_feature, "target": string_target})
        df_test = pd.DataFrame(test_data)



        model = SVMModel()
        clf = model.clf.fit(df_train["feature"], df_train.target)
        predicted = clf.predict(df_test["feature"])
        # Print predicted result
        h = 0
        for i in range(1,len(accuracy)):
            if predicted[i-1] == accuracy[i-1]:
                h+=1
        print '%f' % (h/float(i))
        print clf.predict_proba(df_test["feature"])

        while True:
            raw = raw_input("nhap gi do:")
            decoded = raw.decode("utf-8")
            test = []
            test.append({"feature": decoded, "target": u'HOTEL'})
            test_df = pd.DataFrame(test)
            print(clf.predict(test_df["feature"]))

if __name__ == '__main__':
    tcp = TextClassificationPredict()
    tcp.get_train_data()