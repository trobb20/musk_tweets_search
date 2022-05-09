# Lets you search Elon tweets using regular expressions
# Teddy Robbins 2022

import pandas as pd
import argparse
import re
import matplotlib.pyplot as plt
from make_elon_csv import make_elon_csv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--regex', help='Regular expression to search for.', default=None)
    parser.add_argument('-c', '--case', help='Case sensitive: true or false', default=True)
    parser.add_argument('-u', '--use_existing', help='Use existing results?: true or false', default=False)
    args = parser.parse_args()

    criteria = args.regex
    case = args.case
    use_existing = args.use_existing

    dataframe = 'elon_db.csv'

    if use_existing == 'true':
        result = pd.read_csv('result.csv', index_col=0)
        print(str(len(result)) + ' results.')
    else:
        if case == 'false':
            flags = re.IGNORECASE
        else:
            flags = 0

        try:
            elon_db = pd.read_csv(dataframe, index_col=0)
        except FileNotFoundError:
            make_elon_csv(dataframe)
            elon_db = pd.read_csv(dataframe, index_col=0)

        if criteria is not None:
            result = elon_db[elon_db['Tweet'].str.contains(criteria, regex=True, flags=flags)]
        else:
            result = elon_db
        result = result.drop_duplicates(subset='Tweet', keep='first').reset_index(drop=True)

        print(str(len(result)) + ' results. Saving...')
        result.to_csv('result.csv')

    if input('Show datetime plot? y/n: ') == 'y':
        dates = pd.to_datetime(result['Date'])
        fig, ax = plt.subplots(1, 1)
        ax.hist(dates, bins=50)
        ax.set_title('%s regex on Elon tweets'%criteria)
        ax.set_ylabel('Count')
        ax.set_xlabel('Date')
        plt.show()

    if input('Show results? y/n: ') == 'y':
        print(result['Tweet'].values)


if __name__ == '__main__':
    main()
