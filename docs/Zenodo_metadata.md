# Zenodo release metadata

This project is designed for two linked Zenodo records.

## Record A — paper

**Upload type:** Publication → Preprint

**Title:** Prime-Gap Ruptures: Skipped Levels in the Record Growth of Consecutive Prime Gaps

**Creator:** Riccardo Panza

**Publication date:** 2026-09-14

**Version:** 1.0.0

**Language:** English

**Licence:** Creative Commons Attribution 4.0 International

**Files:**

- `Prime_Gap_Ruptures.pdf` — primary file
- `Prime_Gap_Ruptures.docx` — editable version

**Description:**

For consecutive odd primes, let the step be half their difference and let the previous maximum be the largest earlier step. This paper defines a prime-gap rupture as a record expansion that exceeds the previous maximum by more than one step level, thereby skipping at least one previously unrealised intermediate level. Every rupture is necessarily a record prime gap. The first is 113→127, where the record step rises from 4 to 7 and skips 5 and 6. A direct sieve through 10^8 reproduces the original events. Published exhaustive-search data through 10^20 support 68 confirmed ruptures, with complete recovery observed for the first 66 and right-censoring for the remaining two. No universal recovery or predictive mechanism is claimed. The contribution is definitional, visual and computational.

**Keywords:** prime gaps; maximal prime gaps; record gaps; half-gaps; first occurrences; computational number theory; mathematical visualisation; reproducible research

**Related identifiers to add after Record B exists:**

- Record B DOI — relation: *is supplemented by*
- GitHub repository URL — relation: *is supplemented by*

## Record B — reproducibility package

**Upload type:** Software

**Title:** Prime-Gap Ruptures: Reproducibility Package

**Creator:** Riccardo Panza

**Publication date:** 2026-09-14

**Version:** 1.0.0

**Licence:** MIT for code; the archive's separate licence files govern paper, figures, derived data and third-party extracts.

**Description:**

Reproducibility package for *Prime-Gap Ruptures: Skipped Levels in the Record Growth of Consecutive Prime Gaps*. The release contains exact CSV catalogues, source provenance, Python analysis code, 36 automated tests, ten figures, the mathematical audit and documentation for verification and extension. It distinguishes 68 confirmed ruptures within the declared 10^20 boundary from a 69th outside-boundary candidate and records complete or censored recovery status for every skipped step.

**Related identifiers to add after Record A exists:**

- Record A DOI — relation: *is supplement to*
- GitHub repository URL — relation: *is source of* or *is alternate identifier*

## DOI update checklist

After Zenodo reserves or issues the DOIs:

1. add the paper DOI to `CITATION.cff` under `preferred-citation`;
2. add the software DOI at the top level of `CITATION.cff`;
3. replace the pending citation text in `README.md`;
4. add reciprocal related identifiers in both Zenodo records;
5. tag the exact GitHub commit as `v1.0.0`;
6. do not alter that tag after publication; use a new version for corrections.
