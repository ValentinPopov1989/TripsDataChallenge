import os
import pandas as pd
import csv
from sqlalchemy import create_engine


def getDelimiter(filename, encoding):
    with open(filename, encoding=encoding) as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=None)
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        return dialect.delimiter


def readFiles(path, connOut, encoding='utf-8'):
    files = os.listdir(path)

    for file in files:
        filename = os.path.join(path, file)
        separator = getDelimiter(filename, encoding)
        tablename = file.split(".")[0]
        print("filename:{0} separator={1} tablename={2}".format(filename, separator, tablename))

        df = pd.read_csv(os.path.join(path, file), sep=separator, encoding=encoding)
        print(df.shape)

        df.to_sql(tablename, con=connOut, if_exists='replace', chunksize=1000, index=False)