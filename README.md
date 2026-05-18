# FractMuse
---
## An algorithmic compositional tool for musicians

This project functions as another "tool" composers can use in their creative process. I introduce ways to iteratively expand motifs, sieve theory (from Xenakis), and markov chains.

https://drive.google.com/file/d/1sDyDam0oKtqYpLp__ofFcDvPNpnso7Sd/view?usp=sharing

## Getting started

Create an environment and install the package:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

Real-time MIDI playback needs the optional playback extra:

```bash
python -m pip install -e ".[playback]"
```

Invoke the unified command-line interface:

```bash
python -m fractmuse list
python -m fractmuse run legacy/main8 --output demo.mid
```

Use `--port` to target a specific MIDI output, `--no-play` to skip real-time playback, and `--midi-file` to override the source file for Markov-based pieces.

## Architecture

FractMuse is organized around a small package boundary:

- `fractmuse.core` contains notes, scale-aware notes, MIDI events, and motifs.
- `fractmuse.algorithms` contains pure transformations such as expansion, interpolation, sieves, and Markov generation.
- `fractmuse.io` contains MIDI file and playback adapters.
- `fractmuse.compositions` contains registered pieces and legacy composition ports.

Historical top-level modules such as `Note.py`, `Motif.py`, and `algorithms/algo.py` remain as compatibility wrappers for old scripts.

## Future Work
Detecting chord progressions
Allow users to create mappings of certain notes or chord progressions they like
