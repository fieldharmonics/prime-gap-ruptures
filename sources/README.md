# Source snapshots

These frozen files support reproducibility and provenance:

- `gap_snapshot.csv`: compact numerical extract of gap sizes up to 1854, including the exceptional gap 1 from the Prime Gap List Project data;
- `oeis_lower.txt`: record-gap lower endpoints from OEIS A002386;
- `oeis_upper.txt`: record-gap upper endpoints from OEIS A000101;
- `oeis_first.txt`: first-occurrence lower endpoints from OEIS A000230, indices 0–721 (positive steps 1–721);
- `oeis_order.txt`: chronological order of first-occurring half-gaps from OEIS A014321;
- `boundary.md`: author-written factual summary of the published exhaustive-search boundary.

The former `boundary.html` webpage copy is omitted from the corrected package. Its historical checksum remains in the provenance table; earlier Git history is unchanged.

The full `allgaps.sql` file is deliberately omitted from the public release because it is large and unnecessary for rerunning `analysis.py`. Its URL, access date, checksum and byte length are retained in `output/provenance.csv`. `prepare_snapshot.py` can rebuild the compact extract after a user independently obtains the full SQL file and places it at `sources/allgaps.sql`.

The exploratory manuscript and factor workbook are also deliberately omitted from the public repository. Their filenames and checksums are omitted from the public provenance. The authorised derived audit records every Paper One correction. They are privately retained by the author.

See `THIRD_PARTY_NOTICES.md` for attribution and licensing scope.
