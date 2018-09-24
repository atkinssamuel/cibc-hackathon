import csv
import numpy as np

def Normalize(dataPath):
    with open(dataPath+'/claims_final.csv') as dataSetFile:
        dataSet = csv.reader(dataSetFile, delimiter=',')
        dataMatrix = []
        dataDictionary = {}
        counter = 0
        for entry in dataSet:
            dataMatrix.append(entry)
            if str(dataMatrix[counter][4]) not in dataDictionary.keys():
                dataDictionary[str(dataMatrix[counter][4])] = list([dataMatrix[counter]])
            else:
                dataDictionary[str(dataMatrix[counter][4])].append(dataMatrix[counter])
            counter += 1
        countryMax = -1
        countryMin = -1
        for value in dataDictionary.values():
            for row in value:
                if countryMin == -1:
                    countryMin = float(row[7])
                if float(row[7]) < countryMin:
                    countryMin = float(row[7])
                if countryMax == -1:
                    countryMax = float(row[7])
                if float(row[7]) > countryMax:
                    countryMax = float(row[7])
            for row in value:
                row[7] = float(float(row[7]) - countryMin)/(countryMax - countryMin)
    return dataDictionary

def Extract(data):
    extData = []
    for i in range(len(data)):
        extData.append([])
        extData[i].append(data[i][0])
        extData[i].append(data[i][2])
        extData[i].append(data[i][3])
        extData[i].append(data[i][5])
        extData[i].append(data[i][6])
        extData[i].append(data[i][7])
    ext = np.r_[extData]
    return ext

def F1(data):
    extData = []
    for i in range(len(data)):
        extData.append([])
        extData[i].append(data[i][2])
        extData[i].append(i+1)
    ext = np.r_[extData]
    return ext

def F2(data):
    extData = []
    for i in range(len(data)):
        extData.append([])
        extData[i].append(data[i][0])
        extData[i].append(data[i][1])
        extData[i].append(data[i][2])
        extData[i].append(data[i][5])
        extData[i].append(data[i][3])
        extData[i].append(i+1)
    ext = np.r_[extData]
    return ext
