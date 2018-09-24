import parse
import pandas as pd

def Sort(scores, data): 								# Sort entire dataset in increased order of probability
    # Append scores to dataset
    for i in range(len(data)):
        data[i].append(scores[i])

    sorted = QuickSort(data)
    return sorted

def QuickSort(data):                                    # Quick sort implementation O(nlogn)
    less = []
    equal = []
    greater = []

    if len(data) > 1:
        pivot = data[0][8]
        for x in data:
            if x[8] < pivot:
                less.append(x)
            if x[8] == pivot:
                equal.append(x)
            if x[8] > pivot:
                greater.append(x)
        return QuickSort(less)+equal+QuickSort(greater)

    else:
        return data

def File1(sorted):
    provider_info = parse.F1(sorted)					# Create file1
    df = pd.DataFrame(provider_info)
    df.to_csv("/home/agiachris/Desktop/file1.csv")

def File2(sorted):										# Create file2
    dict = {}
    for i in range(len(sorted)):						# Create dicitonary of providers and their top 100 anomolies
        if sorted[i][2] not in dict.keys():
            dict[sorted[i][2]] = []
            dict[sorted[i][2]].append(sorted[i])
        else:
            dict[sorted[i][2]].append(sorted[i])

    extracted = []										# Extract top 100 from each provider
    for key in dict.keys():
        for i in range(100):                            # or len(dict[key]) if decreased dataset
            extracted.append(dict[key][i])

    info = parse.F2(extracted)							# Parse for necessary columns
    df = pd.DataFrame(info)
    df.to_csv("/home/agiachris/Desktop/file2.csv")		