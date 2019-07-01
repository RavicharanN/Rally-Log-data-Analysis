import pandas
import pickle
import csv 
import numpy

csv_reader = pandas.read_csv('string_study.csv', delimiter=',', header=None)

final_arr = csv_reader.values

print(final_arr)


