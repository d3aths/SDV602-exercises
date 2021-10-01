import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def display_csv_pandas():
    df = pd.read_csv('nz-convictions (copy).csv')
    print(df)

def transpose(table_csv, skip_if_empty = True):
    transposed_tmp = []
    transposed = []
    transposed_tmp = list(zip(*table_csv))
    
    # change each row to a list
    for row_tuple in transposed_tmp:
        transposed += [list(row_tuple)]
    
    return transposed

def multiple_plots(**kwargs):
    """
    Plot more than one on a single graph
    Args 
          **kwargs lets you pass arguments into this function
    """
    years = []
    convictions_f = []
    convictions_m = []

    with open('nz-convictions (copy).csv') as f:
        reader = csv.reader(f, delimiter=',')
        transposed = transpose(reader)

        for row in transposed:
            years.append(int(row[0])),
            convictions_f.append(int(row[3])),
            convictions_m.append(int(row[4]))


    fig, ax = plt.subplots()

    ax.set(xlabel='Year',
        ylabel='Convictions by sex',
        title='New Zealand Conviction Data')

    ax.plot(years, convictions_f)
    ax.plot(years, convictions_f, "oy")
    ax.plot(years, convictions_m)
    ax.plot(years, convictions_m, "or")

    # return plt.gcf()

    plt.show()

# runs code
if __name__ == '__main__':
   multiple_plots()