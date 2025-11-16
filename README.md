# FractMuse
---
## An algorithmic compositional tool for musicians

This project functions as another "tool" composers can use in their creative process. I introduce ways to iteratively expand motifs, sieve theory (from Xenakis), and markov chains.

https://drive.google.com/file/d/1sDyDam0oKtqYpLp__ofFcDvPNpnso7Sd/view?usp=sharing

## Getting started

Install the Python dependencies listed in `requirements.txt` (or your preferred environment) and invoke the unified command-line interface:

```bash
python -m fractmuse list
python -m fractmuse run legacy/main8 --output demo.mid
```

Use `--port` to target a specific MIDI output, `--no-play` to skip real-time playback, and `--midi-file` to override the source file for Markov-based pieces.

## Future Work
### I am currently working on a Swift application for musicians to view their improvisations from audio -> midi -> sheet music.
Detecting chord progressions
Allow users to create mappings of certain notes or chord progressions they like
