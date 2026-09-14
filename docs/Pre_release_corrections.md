# Pre-release corrections

Corrections authorised by Riccardo Panza on 14 September 2026 following
review of commit bd5c6ec92895d4ed429b28a2bfbfeddddcc52fb1.
No tag, GitHub release or Zenodo publication is authorised by this update.

## Changes and checks

- Rebuilt Markdown and Word from the same template and numerical summary,
  then exported the PDF from that Word file. All 16 PDF pages were visually
  inspected. The AI declaration is present, the recovery definition is
  legible, and the appendix has all 69 entries without the former blank page.
- Added a separate two-block prime-2 inset; changed the tree column heading
  to “Row value” because the seed 1 is not prime. The enlargement still shows
  all intervening primes from 89 through 127.
- Refreshed the frozen A000230 B-file through index 721 and recorded its
  actual access date, checksum and length. All 721 positive steps match the
  source-derived first-occurrence data. Added explicit index-coverage and
  source-integrity validation.
- Added six tests for source hashes, coverage, malformed index sequences,
  data-driven maximum delays and platform-specific memory units. All 36
  tests pass. Python optimisation mode is rejected because it disables
  required assertions. CI now also compares regenerated numerical CSVs.
- Corrected exact-integer import guidance and the shared record identifiers.
  Removed a hard-coded maximum-delay value from event selection.
- Replaced the copied boundary HTML in the current tree with an original
  factual note. Its historical checksum and earlier Git history remain.
  OEIS extracts are explicitly attributed and identified as CC BY-SA 4.0;
  mixed code/content/source licensing is explained in the Zenodo description.

## Numerical integrity

The numerical run completed in 4.183 seconds using Python 3.12.14 on Linux,
with approximately 13.375 MiB peak resident memory. The three numerical
outputs, records.csv, ruptures.csv and recoveries.csv, are byte-for-byte
identical to the reviewed commit. Runtime and memory are measurements of
this run, not reproducibility requirements.

The independent reviewer implementation was rerun separately. Its
non-segmented sieve again found 5,761,455 primes through 100,000,000 and
16 ruptures. It checked all 812 distinct listed record/recovered pairs and
reproduced 68 confirmed ruptures, 66 complete recoveries and maximum delay
eight at events 27 and 59. It took 8.96 seconds with approximately 319.36 MiB
peak memory. This is a targeted recheck, not a new exhaustive search to 10^20.

## Remaining qualifications

Publication is pending the author's final approval. The upstream Prime Gap
List numerical extract has no express licence identified in its source
repository. Its inclusion is explained as a limited extract of mathematical
facts, not a claim of permission or a legal warranty. The author should
review that documented basis before archival publication; no third party
has been contacted. See THIRD_PARTY_NOTICES.md.

The original private manuscript and workbook remain excluded. No new
credentials, recovery codes or private authentication files are included.
The public audit material remains as previously authorised.

With the author’s approval, private-source filenames and checksums have been
removed from the current public provenance. Earlier Git history has not been
rewritten; historical metadata remain in earlier commits.
