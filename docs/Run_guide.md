# Run guide

## Reading without programming

Open **output/Prime_Gap_Ruptures.pdf** to read the paper, or the Word file beside it to edit it. **output/Audit_and_corrections.md** explains what changed and why. The **output/figures** folder contains ten numbered figures in PDF and SVG for printing, plus PNG copies.

**output/ruptures.csv** has one row per event. Rows 1–68 are confirmed within the stated boundary; row 69 is provisional. **output/recoveries.csv** has one row per skipped step. Blank recovery endpoints mean censored or outside-boundary, as stated in the status column; they do not mean zero. The file includes partial recovery orders. All endpoints are exact decimal integers.

When opening CSV files in Excel or similar software, use its import command and set endpoint columns to **Text**. Simply double-clicking can round the large integers. Keep an untouched copy of the supplied CSV files.

## Repeating the calculation

1. Download or clone the repository. Keep its folder structure intact.
2. Use Python 3.12 or later. The numerical calculation needs only Python's standard library and works offline with the included source snapshots.
3. Open a terminal in that folder. On Windows, “Open in Terminal” is usually available from the folder's context menu. On macOS or Linux, open Terminal and change to that folder.
4. Run `python3 analysis.py` (or `py analysis.py` on Windows).
5. Run `python3 -m unittest -v test_analysis` (or `py -m unittest -v test_analysis`). The expected result is **30 tests, OK**.

The numerical calculation took about eight seconds in the research environment. A slower computer may take longer. It enumerates primes only through 100 million, then checks and analyses the supplied published records. It does not enumerate all primes through 10²⁰.

The expected headline output is 69 listed entries, 68 confirmed entries, 66 complete recoveries, first-thirteen maximum 3, expanded maximum 8, and maximum events 27 and 59. The scripts stop with an assertion error if a source cross-check disagrees. Do not ignore such an error or use partially refreshed outputs.

## Optional figures and Word rebuild

These tasks need additional Python packages: matplotlib for figures and python-docx for the editable paper. Install the exact versions in `requirements-optional.txt`, then run:

```text
python3 figures.py
python3 build_paper.py
```

The figures use vector PDF/SVG exports and 300 dpi PNGs. The Word builder reads manuscript_template.md and fills its tables from the datasets. Use Word or LibreOffice's PDF export to regenerate a PDF. The delivered PDF was produced with LibreOffice through the document renderer and visually reviewed. The exact pagination can vary with fonts and office software.

## Definitions used in the files

`p,q`: lower and upper endpoints. `previous`: earlier maximum step. `jump`: new step minus earlier maximum. `skipped_start,skipped_end`: inclusive range of skipped levels. `complete_p,complete_q`: last recovery pair. `delay_ruptures`: number of subsequent ruptures completed before complete recovery. `order`: a skipped level's position among observed recoveries for that event.

Gap-count and prime-index distance use the same index difference and are populated only when directly enumerated. Numerical distance uses lower primes; ratio and natural logarithmic ratio also use lower primes. The recovery timeline figure explicitly uses upper-prime ratios instead. These conventions must not be mixed when comparing results.

## Provenance and boundaries

The **sources** folder contains a compact snapshot of gap data through size 1854, the OEIS tables used for cross-checks and the published coverage page. The original exploratory PDF and workbook are privately retained rather than republished; their checksums remain in `output/provenance.csv`. The original full SQL download's checksum is also recorded although that larger file is omitted. The compact snapshot is sufficient to repeat every numerical result in the paper.

The declared exhaustive boundary is a claim of the published search project, not an independently rerun search at that scale. Beyond it, verified consecutive endpoints do not establish record priority. Updating the catalogue requires a fresh complete-coverage statement, new source cross-checks and a review of all censoring statuses. Do not simply increase the boundary constant.
