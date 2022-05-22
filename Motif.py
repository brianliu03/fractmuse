class Motif:

    def __init__(self, pitches, spans, vels):
        self.pitches = pitches
        self.spans = spans
        self.vels = vels
    
    def add(self, pitch, span, vel):
        self.pitches.append(pitch)
        self.spans.append(span)
        self.vels.append(vel)