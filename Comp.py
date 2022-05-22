from algo import expand, expand_rand, randPoisDistribution
from Motif import Motif
from Note import Note
from Note2 import Note2
import random

class Comp_1:
    def __init__(self, num_expansions, scale):
        self.motif = Motif([6, 7, 4, -1], [0.7, 0.6, 0.9, 1.2], [0, 5, -4, 6])
        self.num_expansions = num_expansions
        self.scale = scale
    
    def run(self):
        my_list = [Note(None, 2.0, 0, 60, span=1.0, scale=(self.scale, 64))]
        for i in range(self.num_expansions):
            my_list = expand(my_list, self.motif)
        return my_list

class Notes_1:
    def __init__(self, num_expansions, sieve):
        self.modulus, self.shift = sieve
        self.motif = Motif([], [], [])
        for i in range(0, 88):
            self.motif.add(i, 0.5, 60)
        self.num_expansions = num_expansions
    
    def run(self):
        my_list = [Note2(None, 0.5, 0, 0, span=0.5, root=21, sieve=(self.modulus, self.shift))]
        for i in range(self.num_expansions):
            my_list = expand(my_list, self.motif)
        return my_list

class Comp_2:
    def __init__(self, num_expansions, scale):
        self.motif = Motif([-4, 0, 5, 3], [0.3, 0.3, 0.3, 0.3], [0.25, 1.0, 3, 10])
        self.num_expansions = num_expansions
        self.scale = scale
    
    def run(self):
        my_list = [Note(None, 2.0, 0, 60, span=1.0, scale=(self.scale, 64))]
        for i in range(self.num_expansions):
            my_list = expand(my_list, self.motif)
        return my_list

class Comp_3:
    def __init__(self, num_expansions, scale):
        self.motif = Motif([3, 2, 5, -6], [0.3, 0.8, 0.5, 0.7], [1, 1, 1, 1])
        self.num_expansions = num_expansions
        self.scale = scale
    
    def run(self):
        my_list = [Note(None, 2.0, 0, 60, span=1.0, scale=(self.scale, 59))]
        for i in range(self.num_expansions):
            my_list = expand(my_list, self.motif)
        return my_list

class Comp_4:
    def __init__(self, num_expansions, scale, seed):
        self.motif = Motif([1, 4, 3, -2, 7], [0.7, 0.5, 0.7, 0.6, 0.3], [3, -10, 3, 10, -10])
        self.num_expansions = num_expansions
        self.scale = scale
        self.rand = random.Random(seed)
    
    def run(self):
        my_list = [Note(None, 2.0, 0, 60, chan=2, span=1.0, scale=(self.scale, 59))]
        my_list = expand(my_list, self.motif)
        my_list = expand(my_list, self.motif)
        my_list = expand(my_list, self.motif)
        # for i in range(self.num_expansions):
        #     my_list = expand_rand(my_list, self.motif, self.rand)
        return my_list

class Comp_5:
    def __init__(self, num_expansions, scale, seed):
        self.motif = Motif([-8, 6, 0, 7, -2, -3, 3], [0.7, 0.5, 0.7, 0.6, 0.3, 0.5, 0.5], [1, -10, 3, 20, -10, .5, .5])
        self.num_expansions = num_expansions
        self.scale = scale
        self.rand = random.Random(seed)
    
    def run(self):
        my_list = [Note(None, 2.0, 0, 50, span=1.0, scale=(self.scale, 61))]
        my_list = expand(my_list, self.motif)
        my_list = expand(my_list, self.motif)
        my_list = expand(my_list, self.motif)
        # for i in range(self.num_expansions):
        #     my_list = expand_rand(my_list, self.motif, self.rand)
        return my_list

class Comp_6:
    def __init__(self, num_expansions, scale, seed):
        self.motif = Motif([-1, 5, 8, -4, 2], [1.0, 0.01, 0.5, 1.0, 0.01], [1, 0.5, 0.5, 0.5, 0.5])
        self.num_expansions = num_expansions
        self.scale = scale
        self.rand = random.Random(seed)
    
    def run(self):
        my_list = [Note(None, 2.0, 0, 40, span=1.0, scale=(self.scale, 61))]
        for i in range(self.num_expansions):
            my_list = expand(my_list, self.motif)
        return my_list

class Comp_7:
    def __init__(self, num_expansions, scale, seed):
        self.motif = Motif([-2, 5, -4, -2, 8, 10], [0.5, 1.3, .75, .03, .5, .5], [1, 0.5, 0.5, 0.5, 0.5, 0.5])
        self.num_expansions = num_expansions
        self.scale = scale
        self.rand = random.Random(seed)
    
    def run(self):
        my_list = [Note(None, 2.0, 0, 40, span=1.0, scale=(self.scale, 64))]
        for i in range(self.num_expansions):
            my_list = expand(my_list, self.motif)
        return my_list


class Comp_8:
    def __init__(self, num_expansions, scale, seed):
        self.motif = Motif([-2, 5, -10, 6, -6, 9, -9, -1, -7], [0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.6], [0.5, 20, 0.5, 20, 0.1, 0.01, 0.5, 0.5, 0.5])
        self.num_expansions = num_expansions
        self.scale = scale
        self.rand = random.Random(seed)
    
    def run(self):
        my_list = [Note(None, 0.1, 0, 40, span=1.0, scale=(self.scale, 64))]
        for i in range(self.num_expansions):
            my_list = expand(my_list, self.motif)
        return my_list

class Comp_9:
    def __init__(self, num_expansions, scale, seed):
        self.motif = Motif([-2, 5, -10, 6, -6, 9, -9, -1, -7], [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 1.0], [0.5, 20, 0.5, 20, 0.1, 0.01, 0.5, 0.5, 0.5])
        self.num_expansions = num_expansions
        self.scale = scale
        self.rand = random.Random(seed)
    
    def run(self):
        my_list = [Note(None, 0.1, 0, 40, span=1.0, scale=(self.scale, 64))]
        for i in range(self.num_expansions):
            my_list = expand(my_list, self.motif)
        return my_list