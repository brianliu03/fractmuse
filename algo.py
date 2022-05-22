import math
from Note import Note
import random
from copy import copy

# snote: a Note that has a span but not a time
   


def snotes_to_notes(snotes):
    '''Input arguments:
    snotes: list of Note with span
    Output: list of Note with time
    '''
    time = 0
    output = []
    for n in snotes:
        note = copy(n)
        note.time = time
        time += n.span
        output.append(note)
    return output

def snotes_to_notes_sieve(snotes, modulus):
    time = 0
    output = []
    i = 0
    for n in snotes:
        if i % modulus == 0:
            note = copy(n)
            note.time = time
            time += n.span
            output.append(note)
        i += 1
    return output

# s-note: has a span but not a time
#   A(1.0)  B(0.5) C(1.1) D(2)
#   A_n (t = 0.0), B_n(t = 1.0), C_n(t = 1.5)
#
#   A  B  C  D   E   F ..
# [A, C, E, G, I, ...] <- move this one up tritone
# [B, D, F, H, J, ...] <- translate pitch an tritone down

def snotes_to_notes_2(snotes):
    time_top = 0
    time_bot = 0
    output_top = []
    output_bot = []
    for i in range(len(snotes)):
        n = snotes[i]
        if i % 2 == 0:
            note = copy(n)
            note.time = time_top
            note.pitch += 6
            note.chan = 1
            # note = Note(time_top, n.dur, n.pitch + 6, n.vel, span=n.span, scale=n.scale)
            time_top += n.span
            output_top.append(note)
        else:
            note = copy(n)
            note.time = time_bot
            note.pitch -= 6
            note.chan = 2
            time_bot += n.span
            output_bot.append(note)
    final_out = output_top + output_bot
    return final_out
    

def expand(snotes, motif):
    pitches = motif.pitches
    spans = motif.spans
    vels = motif.vels
    output = []
    for n in snotes:
        for i in range(len(pitches)):
            n1 = copy(n)
            n1.pitch += pitches[i]
            n1.vel += vels[i]
            n1.span *= spans[i]
            output.append(n1)
    return output

def expand_rand(snotes, motif, rand):
    pitches = motif.pitches
    spans = motif.spans
    vels = motif.vels
    output = []
    for n in snotes:
        r = rand.random()
        if r < 0.7:
            for i in range(len(pitches)):
                n1 = copy(n)
                n1.pitch += pitches[i]
                n1.vel += vels[i]
                n1.span *= spans[i]
                output.append(n1)
        else:
            output.append(n)
    return output

def randPoisDistribution(snotes, motif):
    # uses random k values
    pitches = motif.pitches
    spans = motif.spans
    vels = motif.vels
    output = []
    # i = 0
    for n in snotes:
        for j in range(len(pitches)):
            k = random.randrange(0, 100)
            r = random.random()
            poisson = 5 * ((30 ** k) / math.factorial(k)) * (2.71828 ** (-30))
            if poisson >= r:
                n1 = copy(n)
                n1.pitch += pitches[j]
                n1.vel = vels[j]
                n1.span *= spans[j]
                output.append(n1)
            # i = i + 1
    return output
