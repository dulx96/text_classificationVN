# -*- coding: utf8 -*-

def generateCleanDataTrain(train_filename):

    fr  = open(train_filename,'r')
    fw  = open('../generated_files/cleanDataTrainVi.txt','w+')
    fr.readline()
    i = 0
    for line in iter(fr.readline, ''):
        if i%4 == 0:
            fw.write(line)
        elif i%4 == 1:
            fw.write(line.split('#')[0].split('{')[1]+'\n')

        i+= 1

def generateCleanDataTest(train_filename):
    fr  = open(train_filename,'r')
    fw  = open('../generated_files/cleanDataTestVi.txt','w+')
    fr.readline()
    i = 0
    for line in iter(fr.readline, ''):
        if i%4 == 0:
            fw.write(line)
        elif i%4 == 1:
            fw.write(line.split('#')[0].split('{')[1]+'\n')

        i+= 1

generateCleanDataTrain('../data/1-VLSP2018-SA-hotel-train (4-3-2018).txt')
generateCleanDataTest('../data/2-VLSP2018-SA-hotel-dev (4-3-2018).txt')