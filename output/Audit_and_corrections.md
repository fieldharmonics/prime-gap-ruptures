# Mathematical and spreadsheet audit

Riccardo Panza | Paper One | 13 September 2026

## Sources and coverage

The complete 23-page PDF **Violation Events in the Prime Sequence V2.0.pdf**, dated 11/02/2026, was extracted and read, including its front matter, Sections 1–11, Appendices A–B and six references. Page renderings were reviewed to check the extracted structure. The original workbook **Prime Factor to Violation#1.xlsx** contains one worksheet, `Sheet 1 - REGION 1 VIOLATION #1`, with a used range A1:EZ46. Every non-empty cell was inspected, including row labels, prime labels, incidence marks and power annotations. There are no formulas or comments. The workbook is an exploratory display, not an executable factorisation algorithm.

Earlier generated research files were located during source discovery but were not used as evidence for the results in this revision. The new calculation uses a fresh source snapshot and independently written code.

## Mathematical correction log

| ID | Location in original | Finding and correction |
|---|---|---|
| M01 | Abstract; Sections 1, 3–7, 9–11 | Remove claims of capacity, structural failure, feasibility, stress, influence and response. The definition establishes a record classification, not those mechanisms. |
| M02 | Section 1.1 | The assertion that listed structured prime configurations are known to occur infinitely often is unsupported and includes unresolved problems. Remove it. |
| M03 | Section 2.2 | Prime gaps are integer quantities in classical number theory. Gap descriptions do not implicitly treat them as continuous. |
| M04 | Section 2.3 | A step s counts unit moves on the odd-number lattice, not interior odd integers. There are s−1 interior odd integers and 2s−1 interior integers. |
| M05 | Sections 2.3, 10 | Half-gap normalisation is an invertible rescaling g=2s. It adds visual convenience, not numerical information absent from the gaps. |
| M06 | Sections 2–4 | Exclude 2→3 from the integer-step history. Initialise with 3→5, s=1; the earlier maximum is undefined for this seed. |
| M07 | Sections 3.2, 4.1 | A previous maximum imposes no requirement that intermediate levels must occur first. Replace “support” or “feasibility” with observed historical maximum. |
| M08 | Sections 4.1 and 10.1 | The assertion that a violation may be non-record contradicts s>M+1. Every rupture is a record gap. Add the short proof. |
| M09 | Appendix A note | “Not equivalent to record gaps” is valid only as a proper-subclass distinction. Explain that sequential records are excluded, but non-records cannot qualify. |
| M10 | Section 4.3 | Retain 113→127, gap 14, step 7, previous maximum 4. Add jump 3 and skipped set {5,6}. |
| M11 | Sections 4.2–4.3 | The first rupture desert is not the first prime-free interval. Define the integer interior explicitly. |
| M12 | Section 5.1 | Regions starting at 2 do not tile all positive integers: 1 is omitted. The final tail also needs a convention in a finite catalogue; infinite coverage cannot be assumed from the finite table. Remove regions from Paper One. |
| M13 | Sections 5.3–7.4 | No computation supports claims that ruptures constrain Cunningham chains, twin primes or 2p+k forms. Remove these interpretations. The parity observation for 2p+k is correct but outside scope. |
| M14 | Section 8 | Odd composites start 9,15,21,25,27,…; their initial step is already 3 and their steps never exceed 3, since multiples of 3 among odd integers are six apart. Record growth is bounded rather than smoothly increasing. This is not a matched control and does not establish prime-specificity. |
| M15 | Section 9 | A previously unrealised step has a first occurrence, not a reappearance. Define individual and complete recovery, an observation boundary and censoring. Remove resilience terminology. |
| M16 | Appendix A | All 13 lower primes, upper primes, steps and previous maxima reproduce exactly. All 26 listed region endpoints agree with the stated finite construction. No numerical edits are needed in Table A1. |
| M17 | Appendix B.1 | Events 14–16 start at 17,051,707; 20,831,323; 47,326,693. Events 15 and 16 are much earlier than the suggested ranges. The second successive event interval shrinks, so monotone region expansion is not supported. |
| M18 | Appendix B.2 | Gap 246 has step 123 but is not a record gap: gap 248 appears earlier. No rupture can be assigned solely from gap size. Remove heuristic placement. |
| M19 | References 1–2 | The exact Cunningham and Caldwell bibliographic entries were not established by the focused search. Do not reproduce them as verified references. This is not a claim that the authors or related works do not exist. |
| M20 | Front matter | math.GM is General Mathematics, not the subject label “Experimental Mathematics”. Use number theory and computational number theory descriptively. |
| M21 | New brief | The enlargement 89→97→113→127 omits 101,103,107,109. Include these rows; 97→113 is not a consecutive-prime transition. |
| M22 | New brief | Row 1 is a geometric seed and is not prime. “Tree” names a display, not a newly specified graph-theoretic tree. |
| M23 | New brief | Number of later gaps and prime-index distance are the same quantity j−n under the selected convention, not independent metrics. |
| M24 | Expanded checkpoint | There are 69 selected jumps among 85 listed record entries, including the exceptional gap 1. The confirmed catalogue within 10^20 contains 68 ruptures among 84 total record entries. Entry 69 is retained separately as outside-boundary candidate. |
| M25 | Recovery checkpoint | The current boundary supports complete recovery of events 1–66, not merely 1–59. Events 60–66 must not be censored when their recoveries are available. |
| M26 | Recovery checkpoint | The maximum completed delay remains eight later ruptures, attained by 27 and 59. It is a finite maximum, not a bound. |
| M27 | Novelty | OEIS A014321 already records first occurrences of half-gaps; A053695 already records differences of record gaps. Do not claim either primitive is new. |

## Spreadsheet correction log

Column number equals the represented integer: for example DJ represents 114. Rows 33 upwards represent primes 2,3,5,7,11,13,17,19,23,…, using A,B,C,… as labels. Under this inferred incidence convention, a cell is occupied when that row's prime is a proper divisor of the column integer. This interpretation is supported by the repeating multiples and prime key in row 34.

| ID | Cell or cells | Original | Correction | Reason |
|---|---|---|---|---|
| S01 | P31 → O31 | C at 16 | Move C to 15 | 5 divides 15, not 16. |
| S02 | BQ26 → BQ25 | I in the 19-row at 69 | Move I to the 23-row | 69=3×23. |
| S03 | BX26 | Blank | H | 76=4×19. |
| S04 | CQ26 | Blank | H | 95=5×19. |
| S05 | DJ26 | Blank | H | 114=2×3×19. |
| S06 | DT23 | Blank | K | 124=4×31. |

These are eight cell differences, representing six underlying correction issues. All remaining divisor-incidence cells within columns 2–127 agree with the inferred convention. The prime labels through 127, base row values and existing power annotations agree with exact arithmetic. The power rows are selective: for example 121=11² has no dedicated 11-power row. That is incomplete annotation rather than a false assertion. Prime squares are represented by incidence once, so incidence alone does not encode multiplicity.

Labels AA, AB and so forth are not self-delimiting as concatenated factor words; a later factor-language paper needs an explicit grammar. Paper One avoids that ambiguity by using ordinary factorisations. The input workbook is preserved unchanged; this log supplies the cell corrections, and the figure/table use corrected arithmetic.

## First rupture interior

114=2×3×19; 115=5×23; 116=2²×29; 117=3²×13; 118=2×59; 119=7×17; 120=2³×3×5; 121=11²; 122=2×61; 123=3×41; 124=2²×31; 125=5³; 126=2×3²×7.

## Checkpoint reconciliation

| Requested checkpoint | Audit result |
|---|---|
| First 13 below original bound | Exactly 13 with both endpoints ≤5,000,000. |
| Every original numerical table entry | Confirmed, including derived region endpoints. |
| First 13 all recover | Yes, using a larger recovery boundary; final completion is at 13,626,407. |
| First 13 delay at most three ruptures | Confirmed, maximum attained by events 9 and 10. |
| 69 ruptures in first 85 records | Numerically confirmed for the listed sequence; only 68 inside declared exhaustive boundary. |
| First 59 assessable and recovered | Confirmed, and extended to first 66. |
| Maximum eight; events 27 and 59 | Confirmed among all 66 completed events. |
| Entry 69 endpoints and arithmetic | Consecutiveness verified; gap 1854, step 927, listed predecessor 862, jump 65, skipped 863–926 (64 levels). Global priority beyond 10^20 is not established here. |

## Negative and inconclusive results

1. The first-13 maximum of three is not stable under expansion: it becomes eight.
2. Factor-richness is untested, not demonstrated. No matched-control experiment was performed in Paper One.
3. No universal recovery, delay bound, predictive model or new mechanism is established.
4. The 69th entry cannot be included in a complete verified catalogue at the declared boundary, despite favourable database flags and locally verified endpoints.
5. Claims of prime-specificity from the original odd-composite control fail to follow.
6. A precise precedent for the entire combined display and recovery framework was not established; the search is insufficient for an absolute novelty claim. Half-gap order and record differences have clear precedents.

## Literature search scope and limitations

Search date: 13 September 2026. Sources examined include the Prime Gap List Project, OEIS A002386/A000101/A005250/A014321/A053695/A014320, author-hosted literature, arXiv author manuscripts and Chris Caldwell's PrimePages gap exposition. Queries included “prime-gap rupture”, “prime-step tree”, “prime gaps skipped record values recovery”, “prime record gaps skipped”, and titles of computational and modelling papers. Some exact-term searches returned irrelevant or generic pages; these are not evidence of absence. No comprehensive MathSciNet or zbMATH review was conducted.

The closest numerical precedents are A014321 (first appearances of half-gaps, including 1,2,3,4,7,5,6) and A053695 (record-gap differences). The proposed rupture condition filters the latter at differences greater than 2. Recovery joins that filtered history to first-occurrence data. A centred block display and the desert/oasis vocabulary are descriptive additions. The combined terminology, visualisation and recovery framework appears distinctive within the literature examined, but no priority claim is justified.

## Publication recommendation

The best initial format is a short computational research note or carefully documented preprint with machine-readable supplements and a prominent explanatory figure. A venue interested in integer sequences, experimental mathematics, or mathematical exposition is more appropriate than a theorem-led specialist journal at this stage. An educational version could focus on the tree and the distinction between finite evidence and proof. Editorial acceptance is uncertain: renaming existing data alone is not sufficient, so the reproducible recovery statistics and clear provenance should carry the contribution.
