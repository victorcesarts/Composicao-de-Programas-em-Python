import pandas as pd

# Test 0
def numRows(games):
    return len(games.index)

# Test 1
def numColumns(games):
    return len(games.columns)

# Test 2
def numGoldTotal(games):
    totalGoldMedals = games['GoldS'].sum() + games['GoldW'].sum()
    return totalGoldMedals

# Test 3
def numSummerGoldCountry(games, country):
    def countMedals(line):
        if line['Country'] == country:
            return line['GoldS']
        else:
            return 0
    return int(games.apply(countMedals, axis = 1).sum())

# Test 4
def getCodeMaxSummerGold(games):
    idofMaxGold = games['GoldS'].idxmax()
    countryMostGolds = games.iloc[idofMaxGold]
    return countryMostGolds

# Test 5
def getNthBestSummerCountry(games, n):
    return games.sort_values(by=['GoldS', 'SilverS', 'BronzeS', 'Country'], ascending = False).iloc[n]['Country']
# Test 6

def numCountriesWithMoreThanNWinterMedals(games, n):
    def limitMedals(line):
        return line['TotalW'] > n
    return games.apply(limitMedals, axis = 1).sum()

# Test 7
def numWinterCountries(games):
    average = games['GoldW'].mean()
    def aboveAverage(line):
        return line['GoldW'] > average
    return games.apply(aboveAverage, axis = 1).sum()
    
# Test 8
def countGoldsWithLetter(games, c):
    def startsWith(line):
        if line['Country'][0] == c:
            return line['GoldS']
    numberOfMedals = int(games.apply(startsWith, axis = 1).sum())
    return numberOfMedals

# Test 9
def countHybernalCountries(games):
    def moreWmedals(line):
        return line['TotalW'] >= line['TotalS']
    return games.apply(moreWmedals, axis = 1).sum()