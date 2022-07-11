import math
import random
from copy import copy
import queue


def snotes_to_notes(snotes):
    time = 0
    output = []
    for n in snotes:
        note = copy(n)
        note.time = time
        time += n.span
        output.append(note)
    return output

def interpolate(snotes, order):
    d = { }
    for i in range(0, len(snotes)):
        d["q{0}".format(i)] = queueify(snotes[i])
    output = []
    for num in order:
        note = copy(d["q{0}".format(num)].get())
        output.append(note)
    return output

def queueify(snotes):
    q = queue.Queue()
    for n in snotes:
        q.put(n)
    return q

def addDistribution(snotes, modulus, shift, ascending, inverted):
    output = []
    i = 0
    if not ascending:
        i = 87
    for n in snotes:
        counter = 0
        while True:
            modulo = modulus[counter]
            base = shift[counter]
            counter +=  1
            if i % modulo == base:
                if not ascending:
                    i -= 1
                else:
                    i += 1
                note = copy(n)
                output.append(note)
                break
            if counter >= len(modulus):
                probability = (math.factorial(88) / (math.factorial(88-i) * math.factorial(i))) * (.5 ** i) * (0.5 ** (88 - i)) * 10
                num = random.random()
                if not inverted and num <= probability:
                    note = copy(n)
                    output.append(note)
                elif inverted and num >= probability:
                    note = copy(n)
                    output.append(note)
                if not ascending:
                    i -= 1
                else:
                    i += 1
                break
    return output

def snotes_to_notes_tritones(snotes):
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

def expand(snotes, motif, expPitch, expSpan, expVel, offset):
    pitches = motif.pitches
    spans = motif.spans
    vels = motif.vels
    output = []
    for n in snotes:
        for i in range(len(pitches)):
            n1 = copy(n)
            if expPitch:
                n1.pitch += pitches[i]
            else:
                n1.pitch = pitches[i]
            if expSpan:
                n1.span *= spans[i]
            else:
                n1.span = spans[i]
            if expVel:
                n1.vel += vels[i]
            else:
                n1.vel = vels[i]
            if n1.pitch >= 0 + offset and n1.pitch <= 87 + offset:
                output.append(n1)
    return output

# what is this for???
def expand2(snotes, motif, expPitch, expSpan, expVel):
    pitches = motif.pitches
    spans = motif.spans
    vels = motif.vels
    output = []
    avg = sum(pitches) // len(pitches)
    for n in snotes:
        for i in range(len(pitches)):
            n1 = copy(n)
            if expPitch:
                n1.pitch += pitches[i] - avg
            else:
                n1.pitch = pitches[i]
            if expSpan:
                n1.span *= spans[i]
            else:
                n1.span = spans[i]
            if expVel:
                n1.vel += vels[i]
            else:
                n1.vel = vels[i]
            if n1.pitch >= 0 and n1.pitch <= 87:
                output.append(n1)
    return output

def expand_rand(snotes, motif, expPitch, expSpan, expVel, rand):
    pitches = motif.pitches
    spans = motif.spans
    vels = motif.vels
    output = []
    for n in snotes:
        r = rand.random()
        if r < 0.7:
            for i in range(len(pitches)):
                n1 = copy(n)
                if expPitch:
                    n1.pitch += pitches[i]
                else:
                    n1.pitch = pitches[i]
                if expSpan:
                    n1.span *= spans[i]
                else:
                    n1.span = spans[i]
                if expVel:
                    n1.vel += vels[i]
                else:
                    n1.vel = vels[i]
                if n1.pitch >= 0 and n1.pitch <= 87:
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
