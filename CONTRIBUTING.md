# Contributing

This project is open to verification, correction and extension. Contributions are especially welcome in the following forms:

1. an independent implementation of the rupture and recovery definitions;
2. a correction supported by exact calculations and a reproducible example;
3. a larger catalogue supported by an explicit complete-search boundary;
4. alternative recovery measurements with clearly stated conventions;
5. comparisons with specified probabilistic prime-gap models;
6. matched-control analysis of rupture interiors;
7. negative or inconclusive results.

## Before opening a pull request

- Read the paper's definitions and limitations.
- Run `python3 analysis.py` and `python3 -m unittest -v test_analysis`.
- Add or update a regression test when changing numerical or classification logic.
- Use exact integers for endpoints, gaps, steps and ordering decisions.
- State the source, access date, coverage claim and checksum for new external data.
- Distinguish direct computation from reliance on a published exhaustive search.
- Treat missing recovery beyond a finite boundary as right-censored, not permanent.
- Update the data dictionary and changelog if fields or conventions change.

## Evidence standard

A pair of consecutive primes with a large gap is not automatically a record gap. A proposed new rupture must establish record priority relative to all earlier gaps, normally through a documented exhaustive computation or a reliable published catalogue with a declared complete boundary.

Likewise, a proposed recovery must be the first occurrence of the relevant skipped step, not merely a later occurrence.

## Tone and scope

Please avoid causal or physical language about the primes repairing, balancing or responding to a rupture. The project welcomes conjectures when they are clearly labelled and separated from proved statements and finite observations.

## Credit and AI assistance

Contributors retain credit for their work. Cite the repository version or DOI from which an extension begins. If generative AI materially assists a contribution, disclose the system and role and review every submitted claim, source and line of code.

