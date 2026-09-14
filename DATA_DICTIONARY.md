# Data dictionary

All prime endpoints and exact integer distances (including `numerical_distance`) are stored as decimal integer strings in CSV files. Import these columns as **text** in spreadsheet software to prevent rounding beyond 15 digits. Empty fields mean unavailable or not applicable under the stated status; they do not mean zero.

## `output/records.csv`

This file contains 84 odd-prime rows with record identifiers 2–85. Identifier 1 is the exceptional gap 2→3 and is omitted, but its place in the source numbering is retained. Identifier 85 corresponds to candidate event 69 and lies outside the confirmed boundary; identifiers are not physical CSV row numbers.

| Field | Meaning |
|---|---|
| `record` | Position in the supplied record-gap list, including the exceptional initial gap \(2\to3\) |
| `p`, `q` | Lower and upper consecutive-prime endpoints |
| `gap` | \(q-p\) |
| `step` | `gap/2` for odd-prime endpoints |
| `previous` | Largest earlier odd-prime step; blank for initialisation |
| `kind` | `initial`, `sequential` or `rupture` |

## `output/ruptures.csv`

| Field | Meaning |
|---|---|
| `event` | Rupture number in chronological order |
| `record` | Shared `record` identifier in `records.csv`, not the physical row number |
| `p`, `q`, `gap`, `step` | Event endpoints and exact gap/step values |
| `previous` | Earlier maximum step \(M\) |
| `jump` | `step - previous` |
| `skipped_start`, `skipped_end` | Inclusive skipped-step range |
| `skipped_count` | Number of integers in that range, equal to `jump - 1` |
| `status` | `confirmed` or `outside_boundary_candidate` |
| `recovered_count` | Skipped steps whose first occurrence is observed within the recovery boundary |
| `recovery_status` | `complete`, `right_censored` or `outside_detection_boundary` |
| `complete_p`, `complete_q` | First-occurrence pair of the last recovered step when recovery is complete |
| `last_step` | Step whose first occurrence completes recovery |
| `delay_ruptures` | Subsequent ruptures completed by the recovery endpoint, excluding the originating event |
| `recovery_order` | Semicolon-separated steps ordered by their observed first-occurrence lower endpoint |

## `output/recoveries.csv`

| Field | Meaning |
|---|---|
| `event` | Parent rupture number |
| `step`, `gap` | Skipped step and corresponding even gap |
| `p`, `q` | First-occurrence endpoints when observed |
| `status` | `recovered`, `right_censored` or `outside_detection_boundary` |
| `order` | Recovery order within the parent event |
| `gap_count_distance` | Number of later consecutive-prime gaps; populated only inside the direct sieve |
| `prime_index_distance` | Same index difference under the chosen convention |
| `numerical_distance` | Recovery lower endpoint minus rupture lower endpoint |
| `ratio` | Ratio of recovery and rupture lower endpoints |
| `log_ratio` | Natural logarithm of `ratio` |
| `later_records` | Later record gaps completed by the recovery upper endpoint |
| `later_ruptures` | Later ruptures completed by the recovery upper endpoint |

## Audit and provenance files

- `corrections.csv`: concise correction log with `id`, `location` and `correction`.
- `spreadsheet_cell_audit.csv`: audited workbook differences with cell, represented integer, prime, original value and expected value.
- `spreadsheet_inventory.csv`: non-empty cells from the privately retained source workbook; it contains values and coordinates, not formulas.
- `provenance.csv`: source, access date, SHA-256 checksum and byte length.
- `summary.json`: headline boundary, count, runtime and environment fields from the latest calculation.
