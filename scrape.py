import requests
import pandas as pd
from bs4 import BeautifulSoup


def getTable(URL):
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
    dat = data.split()
    for word in dat:
        try:
            int(word)
            return int(word)
        except:
            pass
