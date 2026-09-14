# Prime-Gap Ruptures

**Skipped Levels in the Record Growth of Consecutive Prime Gaps**

Riccardo Panza · independent researcher · release candidate 1.0.0 · 14 September 2026

This repository accompanies the observational paper *Prime-Gap Ruptures: Skipped Levels in the Record Growth of Consecutive Prime Gaps*. It is intended as an open, reproducible research object that other researchers can inspect, challenge, correct and extend.

![The centred prime-step tree through 127](output/figures/01_prime_step_tree.png)

## Core definition

For consecutive odd primes \(p_n<p_{n+1}\), define

\[
s_n=\frac{p_{n+1}-p_n}{2}
\]

and let \(M_n\) be the largest earlier step. A **prime-gap rupture** occurs when

\[
s_n>M_n+1.
\]

It is therefore a record gap whose half-gap jumps over at least one previously unrealised integer level. The first rupture is \(113\to127\): the record step jumps from 4 to 7 and skips 5 and 6.

## Verified release findings

- The original 13 rupture events are reproduced by independent prime enumeration.
- A direct segmented sieve through \(10^8\) finds 16 ruptures.
- Published exhaustive-search data through \(10^{20}\) support 68 confirmed ruptures.
- Complete recovery is observed for events 1–66; events 67–68 are right-censored at the boundary.
- The greatest complete-recovery delay observed is eight subsequent ruptures, attained by events 27 and 59.
- A 69th listed pair lies above \(10^{20}\) and is retained only as an outside-boundary candidate.

These are finite computational results. The project does not claim a prime-prediction method, universal recovery, a physical mechanism, or a proof of an established conjecture.

## Start here

- [Paper (PDF)](output/Prime_Gap_Ruptures.pdf)
- [Editable paper (Word)](output/Prime_Gap_Ruptures.docx)
- [Plain-language summary](output/Plain_language_summary.md)
- [Mathematical audit and correction log](output/Audit_and_corrections.md)
- [Non-programmer run guide](docs/Run_guide.md)
- [Data dictionary](DATA_DICTIONARY.md)
- [Research roadmap](ROADMAP.md)

## Reproduce the numerical results

Python 3.12 or later is recommended. The core calculation uses only the Python standard library and the included source snapshots.

```bash
python3 analysis.py
python3 -m unittest -v test_analysis
```

Expected result: **36 tests, OK**. The direct sieve through \(10^8\) usually takes several seconds. It does not attempt to enumerate primes through \(10^{20}\); record priority above \(10^8\) is checked against the cited published data.

Optional figure and document rebuilding uses the versions listed in `requirements-optional.txt`.

## Repository map

| Path | Contents |
|---|---|
| `analysis.py` | Exact rupture and recovery analysis |
| `test_analysis.py` | Thirty regression and definition tests |
| `output/ruptures.csv` | One row per rupture or outside-boundary candidate |
| `output/recoveries.csv` | One row per skipped step |
| `output/records.csv` | Record-gap sequence used by the classification |
| `output/figures/` | Ten figures in PDF, SVG and PNG |
| `sources/` | Frozen computational source extracts and provenance notes |
| `output/Audit_and_corrections.md` | Full audit, discrepancies and negative results |

Large endpoint columns in the CSV files must be imported into spreadsheet software as **text**, otherwise values beyond 15 digits may be rounded.

## Contributing

Independent implementations, enlarged catalogues, corrections, negative results and model comparisons are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md). In particular, any proposed boundary extension must establish complete search coverage; verifying a prime pair alone does not establish that its gap is a record.

## Citation

Citation metadata are supplied in [`CITATION.cff`](CITATION.cff). The file will be updated with the Zenodo DOI after publication.

## Licences and provenance

Original prose, figures and author-produced datasets are released under **CC BY 4.0**. Project code is released under the **MIT Licence**. Included third-party source extracts retain their original terms and are not relicensed here. See [LICENSE.md](LICENSE.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## AI assistance

The originating concept, visual representation, source manuscript, spreadsheet and research direction are Riccardo Panza's. OpenAI Codex in ChatGPT Work assisted under his direction with restructuring, mathematical and computational auditing, code, testing, literature discovery, tables and figures. The author reviewed the work and accepts responsibility for it. See [AI_ASSISTANCE.md](AI_ASSISTANCE.md).
