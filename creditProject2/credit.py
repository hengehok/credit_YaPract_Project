# -*- coding: utf-8 -*-

import math
import constants


def modificator(sourceIncome, rate, expectedSum, goal):
    sourceIncomeMod = constants.INTEREST_RATE[sourceIncome]
    rateMod = constants.INTEREST_RATE[rate]
    goalMod = constants.INTEREST_RATE[goal]
    expectedSumMod = -math.log(expectedSum/1000000)
    mod = sourceIncomeMod + rateMod + goalMod + expectedSumMod

    return mod

class Credit:
    def __init__(self, line):
        self.error = '0'
        self.age = self.getAge(line)
        self.sex = self.getSex(line)
        self.sourceIncome = self.getSourceIncome(line)
        self.income = self.getIncome(line)
        self.rate = self.getRate(line)
        self.expectedSum = self.getExpectedSum(line)
        self.period = self.getPeriod(line)
        self.goal = self.getGoal(line)

    def processСlient(self):
        if self.isDataValid():
            #print('VALID')
            # result = credit.processСlient()
            return self.makeDecision(self.age, self.sex, self.sourceIncome, self.income, self.rate, self.expectedSum,
                                 self.period, self.goal)
        else:
            return self.getError()


    def getAge(self, line):
        age = int(line['age'])
        if (age < 0):
            self.error = 'Invalid Age'
        return age

    def getSex(self, line):
        sex = line['sex']
        if sex not in constants.SEX:
            self.error = 'Invalid sex value'
        return sex

    def getSourceIncome(self, line):
        sourceIncome = line['sourceIncome']
        if sourceIncome not in constants.SOURCE_INCOME:
            self.error = 'Invalid source income'
        return sourceIncome

    def getIncome(self, line):
        income = int(line['income'])
        return income

    def getRate(self, line):
        rate = line['rate']
        if rate not in constants.RATE:
            self.error = 'Invalid rate'
        return rate

    def getExpectedSum(self, line):
        expectedSum = float(line['expectedSum'])
        if expectedSum > 10000000 or expectedSum < 100000:
            self.error = 'Invalid Expected Sum'
        return expectedSum

    def getPeriod(self, line):
        period = int(line['period'])
        if period < 1 or period > 20:
            self.error = 'Invalid Period'
        return period

    def getGoal(self, line):
        goal = line['goal']
        if goal not in constants.GOAL:
            self.error = 'Invalid Goal'
        return goal

    def isDataValid(self):
        if len(self.error) > 1:
            return False
        else:
            return True

    def getError(self):
        return self.error

    def maxPossibleSum(self, sourceIncome, rate):
        if sourceIncome == 'passive' or rate == -1:
            max_possible_sum = 1000000
        elif sourceIncome == 'worker' or rate == 0:
            max_possible_sum = 5000000
        else:
            max_possible_sum = 10000000
        return max_possible_sum

    def creditSum(self, expectedSum, period, mod):
        base = 10
        annualSum = (expectedSum * (1 + period * (base + mod) / 100)) / period
        #print(annualSum, expectedSum, period)
        return annualSum

    def makeDecision(self, age, sex, sourceIncome, income, rate, expectedSum, period, goal):
        global mod
        if age >= 60 and sex == "F":
            return 'False, retirement woman age'
        elif age >= 65 and sex == 'M':
            return 'False, retirement man age'
        elif age < 18:
            return 'False, too young'
        elif expectedSum / period > income / 3:
            return 'False, expectedSum/period > income/3'
        elif rate == '-2':
            return 'False, low credit rate'
        elif sourceIncome == 'unemployed':
            return 'False, unemployed'

        if self.maxPossibleSum(sourceIncome, rate) < expectedSum:
            return 'False, too much money required'
        else:
            mod = modificator(sourceIncome, rate, expectedSum, goal)

        annualCreditSum = self.creditSum(self.expectedSum, self.period, mod)
        #print (annualCreditSum)

        if annualCreditSum > income * 0.5:
            return 'False, too much annual sum'
        else:
            return round(annualCreditSum, 3)


