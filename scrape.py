import requests
import pandas as pd
from bs4 import BeautifulSoup


def getTable(URL):
    '''given a URL this function returns a cleaned dataframe with all the
    creatures of the type in the url, the df matches the table on the given url'''
    page = requests.get(URL).text
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('tbody').findNext('tbody')
    tableList = []
    for tr in table.find_all('tr'):
        row = {}
        for i, cell in enumerate(tr.find_all('td')):
            row[i] = cell.text
        tableList.append(row)
    df = pd.DataFrame(tableList)
    df = df[[0, 1, 2, 3, 4]]
    df.columns = ['Name', 'Summary', 'Abilities', 'Size', 'Speed']
    df.dropna(inplace=True)
    return df


def cleanSpeed(data):
    '''a .apply function to extract the base speed'''
    dat = data.split()
    for word in dat:
        try:
            int(word)
            return int(word)
        except:
            pass
