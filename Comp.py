from cmath import exp
import time
from Markov_Algo import MarkovGenerator
from algo import expand, expand_rand, randPoisDistribution, expand2, revertMidC, setMidC
from Motif import Motif
from Note import Note
from NoteScale import NoteScale
from copy import copy
import random

class Notes_1:
    def __init__(self, num_expansions, sieve, spans, direction):
        self.modulus, self.shift = sieve
        self.motif = Motif([], [], [])
        start = direction[0]
        end = direction[1]
        if start > end:
            for i in range(start,end-1,-1):
                counter = 0
                while True:
                    modulo = self.modulus[counter]
                    base = self.shift[counter]
                    counter +=  1
                    if i % modulo == base:
                        self.motif.add(i, spans[counter - 1], 60)
                        i -= 1
                        break
                    if counter >= len(self.modulus):
                        i -= 1
                        break
        else:
            for i in range(start,end):
                counter = 0
                while True:
                    modulo = self.modulus[counter]
                    base = self.shift[counter]
                    counter +=  1
                    if i % modulo == base:
                        self.motif.add(i, spans[counter - 1], 60)
                        i += 1
                        break
                    if counter >= len(self.modulus):
                        i += 1
                        break
        self.motif.pitches = setMidC(self.motif.pitches)
        self.num_expansions = num_expansions
        self.rand = random.Random(101)
        self.size = len(self.motif.pitches)

    def markovify(self, order, start):
        pitches = self.motif.pitches
        gen = MarkovGenerator(len(pitches), 88, order, 0)
        gen.generateTable(pitches)
        self.motif.pitches = gen.createComp(start)

    
    def run(self):
        my_list = []
        my_list.append(Note(None, 0.25, 0, 0, span=1.0, root=81))
        for i in range(self.num_expansions):
            my_list = expand(my_list, self.motif, expPitch=True, expSpan=True, expVel=False, offset=-60)
        self.motif.pitches = revertMidC(self.motif.pitches)
        return my_list

class Comp_1:
    def __init__(self, num_expansions, scale, seed):
        self.motif = Motif([-1, 5, 8, -4, 2], [1.0, 0.01, 0.5, 1.0, 0.01], [1, 0.5, 0.5, 0.5, 0.5])
        self.num_expansions = num_expansions
        self.scale = scale
        self.rand = random.Random(seed)

    def run(self):
        my_list = [NoteScale(None, 2.0, 0, 60, chan=2, span=1.0, scale=(self.scale, 59))]
        my_list = expand(my_list, self.motif, expPitch=True, expSpan=True, expVel=True, offset=-60)
        my_list = expand(my_list, self.motif, expPitch=True, expSpan=True, expVel=True, offset=-60)
        my_list = expand(my_list, self.motif, expPitch=True, expSpan=True, expVel=True, offset=-60)
        # for i in range(self.num_expansions):
        #     my_list = expand_rand(my_list, self.motif, self.rand)
        return my_list

class Comp_4:
    def __init__(self, num_expansions, scale, seed):
        self.motif = Motif([1, 4, 3, -2, 7], [0.7, 0.5, 0.7, 0.6, 0.3], [3, -10, 3, 10, -10])
        self.num_expansions = num_expansions
        self.scale = scale
        self.rand = random.Random(seed)
    
    def run(self):
        my_list = [NoteScale(None, 2.0, 0, 60, chan=2, span=1.0, scale=(self.scale, 59))]
        my_list = expand(my_list, self.motif, expPitch=True, expSpan=True, expVel=True, offset=-60)
        my_list = expand(my_list, self.motif, expPitch=True, expSpan=True, expVel=True, offset=-60)
        my_list = expand(my_list, self.motif, expPitch=True, expSpan=True, expVel=True, offset=-60)
        # for i in range(self.num_expansions):
        #     my_list = expand_rand(my_list, self.motif, self.rand)
        return my_list

class Comp_8:
    def __init__(self, num_expansions, scale, seed):
        self.motif = Motif([-2, 5, -10, 6, -6, 9, -9, -1, -7], [0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.6], [0.5, 20, 0.5, 20, 0.1, 0.01, 0.5, 0.5, 0.5])
        self.num_expansions = num_expansions
        self.scale = scale
        self.rand = random.Random(seed)
    
    def run(self):
        my_list = [NoteScale(None, 0.1, 0, 40, span=1.0, scale=(self.scale, 64))]
        my_list = expand(my_list, self.motif, expPitch=True, expSpan=True, expVel=True, offset=-60)
        my_list = expand(my_list, self.motif, expPitch=True, expSpan=True, expVel=True, offset=-60)
        return my_list

class Comp_7:
    def __init__(self, num_expansions, scale, seed):
        self.motif = Motif([-2, 5, -4, -2, 8, 10], [0.5, 1.3, .75, .03, .5, .5], [1, 0.5, 0.5, 0.5, 0.5, 0.5])
        self.num_expansions = num_expansions
        self.scale = scale
        self.rand = random.Random(seed)
    
    def run(self):
        my_list = [NoteScale(None, 0.5, 0, 40, span=1.0, scale=(self.scale, 64))]
        my_list = expand(my_list, self.motif, expPitch=True, expSpan=True, expVel=True, offset=-60)
        my_list = expand(my_list, self.motif, expPitch=True, expSpan=True, expVel=True, offset=-60)
        my_list = expand(my_list, self.motif, expPitch=True, expSpan=True, expVel=True, offset=-60)
        return my_list