import random
import time

from numpy import size

class MarkovGenerator:

    def __init__(self, totalGenerations, sizeTable, order, offset):
        self.sizeTables = sizeTable
        self.totalGenerations = totalGenerations
        self.order = order
        self.offset = offset
        if order == 1:
            self.probabilities = [[0 for i in range(sizeTable)] for j in range(sizeTable)]
        elif order == 2:
            self.probabilities = [[[0 for i in range(sizeTable)] for j in range(sizeTable)] for k in range(sizeTable)]

    def generateTable(self, l):
        first = 0
        second = 0
        for i in range(0, len(l) - 1):
            first = l[i]
            second = l[i + 1]
            self.probabilities[first - self.offset][second - self.offset] += 1
        for i in range(0, self.sizeTables):
            wTot = sum(self.probabilities[i])
            if wTot != 0:
                for l in range(0, self.sizeTables):
                    self.probabilities[i][l] /= wTot

    def generateTableSpans(self, l):
        first = 0
        second = 0
        for i in range(0, len(l) - 1):
            first = int(round(l[i], 2) * 100)
            second = int(round(l[i + 1], 2) * 100)
            self.probabilities[(first - self.offset)][second - self.offset] += 1
        for i in range(0, self.sizeTables):
            wTot = sum(self.probabilities[i])
            if wTot != 0:
                for l in range(0, self.sizeTables):
                    self.probabilities[i][l] /= wTot

    def generateTable3d(self, l):
        first = 0
        second = 0
        third = 0
        for i in range(1, len(l) - 2):
            first = l[i]
            second = l[i + 1]
            third = l [i + 2]
            self.probabilities[first - self.offset][second - self.offset][third - self.offset] += 1
        for i in range(0, self.sizeTables):
            wTot = sum(map(sum,self.probabilities[i]))
            if wTot != 0:
                for j in range(0, self.sizeTables):
                    for k in range(0, self.sizeTables):
                        self.probabilities[i][j][k] /= wTot
                    wTot2 = sum(self.probabilities[i][j])
                    if wTot2 != 0:
                        for k in range(0, self.sizeTables):
                            self.probabilities[i][j][k] /= wTot2

    def createComp(self, start):
        current = start - self.offset
        output = [current + self.offset]
        for i in range(0, self.totalGenerations):
            prob = random.random()
            scale = 0
            for j in range(len(self.probabilities[current])):
                scale += self.probabilities[current][j]
                if prob <= scale:
                    output.append(j + self.offset)
                    current = j
                    break
        return output

    def createComp3d(self, start):
        current = start
        output = [current]
        for i in range(0, self.totalGenerations):
            prob = random.random()
            scale = 0
            for j in range(len(self.probabilities[current])):
                scale += sum(self.probabilities[current][j])
                if prob <= scale:
                    output.append(j + 21)
                    prob2 = random.random()
                    scale2 = 0
                    if sum(self.probabilities[current][j]) != 0:
                        for k in range(len(self.probabilities[current][j])):
                                newProb = prob2 / sum(self.probabilities[current][j])
                                scale2 += self.probabilities[current][j][k]
                                if newProb <= scale2:
                                        output.append(k + self.offset)
                                        current = k
                                        break
        return output