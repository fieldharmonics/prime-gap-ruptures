# Prime-Gap Ruptures: Skipped Levels in the Record Growth of Consecutive Prime Gaps

Riccardo Panza

Independent researcher | 14 September 2026

## 1 Abstract

For consecutive odd primes, write s=(q−p)/2 and let M be the largest earlier step. We define a prime-gap rupture by s>M+1: a record expansion that skips at least one intermediate integer half-gap level. Every rupture is necessarily a record prime gap. The first occurs at 113→127, where the previous record step 4 increases to 7 and skips levels 5 and 6. An independent segmented sieve through 100,000,000 reproduces the original thirteen events and extends direct verification to sixteen. Published exhaustive-search data through 10²⁰ support a catalogue of 68 ruptures, of which the first 66 have completely observed recovery. Every skipped level in those 66 events appears within that boundary. The maximum observed complete-recovery delay is eight subsequent ruptures. The remaining two events have right-censored recovery; a 69th listed candidate lies beyond the detection boundary. Universal recovery remains unproved and no predictive mechanism is claimed. The contribution is definitional, visual and computational: a record-transition classification, a centred prime-step tree and reproducible skipped-level recovery statistics. A rupture interior is also described as a prime desert and, through its composite factorisations, a prime-factor oasis; unusual factor richness is not established.

## 2 Introduction

Record prime gaps describe the successive largest separations between consecutive primes. This paper distinguishes records whose half-gap increases by one from records that bypass intermediate half-gap levels. The latter are called prime-gap ruptures. The bypassed values provide a finite set whose first later appearances can be recorded and compared.

The underlying prime gaps are established mathematical data. The proposed contribution is a classification of record-gap transitions according to whether intermediate half-gap levels are skipped, together with a visual representation and a recovery analysis of those skipped levels. Its potential utility lies in organising observations and formulating testable questions; a predictive application is not required or demonstrated.

Existing computational catalogues already record maximal gaps and first occurrences [1–4]. Half-gap first-occurrence order is explicitly represented by OEIS A014321, while differences between successive record gaps are OEIS A053695 [5–6]. Thus neither dividing gaps by two nor measuring record increments is new. The framework combines these objects with a centred block display and event-specific recovery sets. The combined terminology, visualisation and recovery framework appears distinctive within the literature examined; this is a limited literature assessment, not an absolute novelty claim.

## 3 Origin of the prime-step representation

The starting point is Panza's exploratory paper, originally titled “Violation Events in the Prime Sequence”, and its associated factor spreadsheet. The working term “violation event” is replaced by “prime-gap rupture” because no mathematical rule is broken. The original numerical catalogue survives the audit, while interpretations involving capacity or structural responses do not follow from its definition.

For each odd prime p, place p equal blocks in a centred row: one spine block and (p−1)/2 blocks on each side. A row containing 1 is a construction seed, not a prime; 2 is displayed separately as the exceptional even prime. The word tree refers to the shape of this display, not to a graph-theoretic branching rule. All odd-prime rows through 127 are shown in Figure 1.

![Figure 1. Complete prime-step tree. Dark outer blocks show additions from the preceding odd-prime row; the seven additions on each side at 127 are hatched. Vertical spacing follows row order, not numerical distance.](figures/01_prime_step_tree.png)

## 4 Prime gaps and traversal steps

Let p₁=2,p₂=3,… be the increasing sequence of primes. For n≥2 define gₙ=pₙ₊₁−pₙ and sₙ=gₙ/2. Both endpoints are odd, so sₙ is a positive integer. The exceptional gap 2→3 has size 1 and is excluded from the step history. Initialise that history with 3→5, step 1. For n≥3 put Mₙ=max{ sⱼ : 2≤j<n }.

A transition adds sₙ blocks to each side of the tree. Equivalently, it takes sₙ moves of length 2 to travel between the endpoints on the odd-number lattice. There are sₙ−1 odd integers strictly inside the gap, and 2sₙ−1 interior integers altogether. Steps are an exact rescaling of gaps: gₙ=2sₙ. The display changes presentation, not arithmetic information.

{{GLOSSARY}}

## 5 Record expansions

A record expansion satisfies sₙ>Mₙ. A sequential record expansion satisfies sₙ=Mₙ+1. The initial step 1 is the seed record; it is not compared with an undefined earlier maximum. Record growth is different from the sequence of all steps, which can rise and fall.

{{EARLY}}

![Figure 2. Early record-step progression. Levels 5 and 6 are bypassed when the record increases from 4 to 7.](figures/03_record_progression.png)

## 6 Definition of a prime-gap rupture

A prime-gap rupture is a transition satisfying sₙ>Mₙ+1. Its jump is Jₙ=sₙ−Mₙ, its skipped-step set is Kₙ={Mₙ+1,…,sₙ−1}, and its skipped-level count is |Kₙ|=Jₙ−1. Thus a rupture occurs precisely when Jₙ≥2. Every skipped value exceeds the earlier maximum and has therefore never occurred previously. Skipped sets from different ruptures are disjoint, since record values strictly increase.

Proposition. Every prime-gap rupture is necessarily a record prime gap.

Proof. If sₙ>Mₙ+1, then sₙ>Mₙ. Hence sₙ exceeds every earlier odd-prime step, and gₙ=2sₙ exceeds every earlier odd-prime gap. It also exceeds the exceptional initial gap 1. Therefore it is a record prime gap. Conversely, a record with Jₙ=1 is sequential and is not a rupture. ∎

The equivalent criterion in gap units is gₙ>Gprevious+2. A non-record gap cannot qualify, even if some smaller gap sizes remain unrealised. This corrects the contrary statements in Sections 4.1 and 10.1 of the original paper. “Rupture” denotes a numerical discontinuity in sequential record growth, without implying a physical event or causal mechanism.

## 7 The first rupture: 113→127

The early records are steps 1,2,3,4,7. The three increases to 2,3,4 are sequential. At 113→127 the record jumps directly from 4 to 7, bypassing 5 and 6. Independent prime enumeration verifies that no earlier transition satisfies the rupture condition.

{{FIRST}}

![Figure 3. Enlargement from 89 through 127, including every intervening prime. In particular, 97 and 113 are not consecutive primes. The first row is a baseline.](figures/02_enlargement.png)

![Figure 4. The first rupture as a change in the standing record. The skipped levels are step sizes, not missing integers in the interval.](figures/04_first_rupture.png)

The tree makes the final expansion conspicuous, but its visual prominence supplies no evidence of a deeper mechanism. The numerical definition establishes the event.

## 8 Rupture deserts and prime-factor oases

Every consecutive-prime interval is prime-free in its interior. A rupture desert is specifically the integer interior of a prime-gap rupture. Under this definition, (113,127) is the first rupture desert, consisting of the thirteen composite integers 114,…,126. It is not the first prime-free interval.

![Figure 5. The first rupture desert. Filled endpoint markers are primes; open interior markers are composites.](figures/05_rupture_desert.png)

Viewed additively, this interval is a prime desert. Viewed multiplicatively, its factorisations offer a complementary prime-factor oasis. “A prime-gap rupture creates a prime desert at the surface and reveals a prime-factor oasis beneath it” is a descriptive bridge; “creates” here denotes association with an interval, not a causal process.

![Figure 6. Verified factorisations of the first rupture interior. Repeated factors and prime powers are visible without an alphabetic factor language.](figures/06_factor_oasis.png)

The oasis description does not imply that rupture interiors contain statistically more factors than comparable ordinary prime gaps. All composite intervals admit factorisation. Whether rupture interiors have unusual factor structure after controlling for gap length and numerical location belongs to Paper Two. The source spreadsheet's missing 19 at 114 and missing 31 at 124 are corrected in this illustration; its full cell audit is supplied separately.

## 9 Skipped steps and recovery

For each skipped step t in Kₙ, let F(t) be the lower endpoint of the first consecutive-prime gap of size 2t. Its recovery pair is F(t)→F(t)+2t. This occurrence must be later than the rupture, because t exceeded every earlier step. Complete recovery is observed at the upper endpoint of the last such pair. We also report that pair's lower endpoint as complete_p. No recovery date is assigned until both endpoints lie within the observation boundary.

For 113→127, step 5 first appears at 139→149 and step 6 at 199→211. The recovery order is 5,6 and complete recovery is observed at 211, before any subsequent rupture. “Recovery” means first later occurrence only, not repair or balancing.

For a rupture at gap index n and recovery at j, gap-count distance and prime-index distance both equal j−n: the immediately next gap has distance 1. Numerical distance uses lower endpoints F(t)−pₙ. The ratio is F(t)/pₙ and logarithmic distance is its natural logarithm. Record and rupture delays count later events completed by the recovery upper endpoint, excluding the originating rupture. Those counters can be zero despite positive numerical delay. Index fields are left blank beyond the direct sieve rather than estimated.

Missing recoveries within a complete observation range are right-censored. A censored event is retained, with its observed partial recovery order. An event beyond the rupture-detection boundary is a different case: even its place in the global record sequence is not established here.

## 10 Data and computational methods

The reproducible pipeline uses exact Python integers. A segmented sieve of Eratosthenes enumerates all primes through 10⁸ using blocks of 1,000,000 integers. It finds 5,761,455 primes, ending at 99,999,989, and sixteen ruptures. The original thirteen lie within 5,000,000; their complete recoveries require a larger range, ending at 13,626,407.

{{BOUNDARY}}

The expanded catalogue uses a frozen Prime Gap List Project snapshot [1]. Its reported exhaustive boundary is 10²⁰, attained on 8 May 2026 [2]. OEIS lower and upper record endpoints agree for all 85 listed entries [3]. First-occurrence lower endpoints agree with OEIS A000230 for steps 1–721, and chronological half-gap order agrees for all 747 terms available in A014321 [4–5]. These publications share underlying discoveries, so agreement is a publication cross-check rather than two independent exhaustive searches. All first occurrences inside the direct sieve also match the independently generated data.

Every listed record pair and every accepted skipped-step recovery pair is locally checked for consecutive primality. A bounded deterministic Miller–Rabin test uses the first thirteen prime bases, through 41, below 3,317,044,064,679,887,385,961,981, using the threshold of Sorenson and Webster [7]. Both endpoints pass and every interior integer is composite. These local tests establish consecutiveness, not global record priority or first-occurrence priority; the latter depend on exhaustive source computations above 10⁸.

{{RUNTIME}}

CSV endpoint fields are decimal integer strings and must be imported as text into spreadsheet software to avoid its fifteen-digit precision limit. Ratios and logarithms alone use floating-point arithmetic; they never determine ordering or status. Source snapshots, hashes, code, tests and a non-programmer run guide accompany the paper. No exhaustive computation to 10²⁰ was rerun locally.

## 11 Verified rupture catalogue

{{ORIGINAL}}

The first thirteen rows reproduce the original table exactly in their endpoint, step and previous-record fields. The expanded list contains 69 qualifying transitions among the first 85 listed record gaps, where that record numbering includes 2→3. However, only 84 record entries and 68 ruptures fall inside 10²⁰. Among the 82 odd-prime record transitions after initialisation, 68 are ruptures (82.9%) and 14 are sequential. This proportion describes that finite record catalogue, not all prime gaps.

![Figure 7. Rupture locations on a logarithmic number line. The open diamond is listed candidate 69; the dashed line is the exhaustive boundary.](figures/07_rupture_timeline.png)

Candidate 69 is 101,412,319,996,363,309,069→101,412,319,996,363,310,923. Its gap is 1854 and its step is 927. Relative to the listed previous record 862, it has jump 65 and skipped set {863,…,926}, comprising 64 levels. The endpoints and their consecutiveness are locally verified. Although the source list flags this entry as maximal and first-occurring, the separate exhaustive-coverage statement stops at 10²⁰. We therefore retain it provisionally outside the confirmed catalogue; intervening undiscovered records could change its classification or numbering. The appendix preserves all 69 entries with this distinction.

## 12 Recovery observations

{{RECOVERY13}}

All skipped levels of the first thirteen events recover within the direct sieve. Their maximum delay is three subsequent ruptures, attained by events 9 and 10. That finite maximum does not survive expansion: among the 66 completely recovered events within 10²⁰, the maximum is eight, attained by events 27 and 59. The requested first-59 checkpoint is confirmed and extended to the first 66; events 60–66 should not be labelled censored.

![Figure 8. Individual recovery timelines for the first thirteen events. A black square marks each event's final recovered level; the full pairs and recovery order are in recoveries.csv.](figures/08_first13_recovery.png)

{{CENSORING}}

The 68 confirmed events skip 779 distinct levels. Of these, 728 recover within the boundary and 51 remain unresolved. Events 1–66 account for 705 skipped levels, all recovered; event 67 has 22 of 51 recovered and event 68 has 1 of 23. Completed-event delays have median 3 and mean 3.30 subsequent ruptures. Counts for delays 0 through 8 are respectively 4,8,12,16,10,5,6,3,2. These completed-case summaries exclude censored events and should not be interpreted as unbiased estimates of eventual delay.

![Figure 9. Complete-recovery summary. Open triangles show the elapsed rupture counts for the two censored events, not completed delays. Candidate 69 is excluded.](figures/09_recovery_summary.png)

![Figure 10. Record-step jump and skipped-set size by numerical location. These plots differ by exactly one unit because |K|=J−1; they are not independent discoveries. The open diamond is candidate 69.](figures/10_jump_sizes.png)

The prime sequence is deterministic. Counts, proportions, quantiles and plots here summarise a specified finite catalogue. No sampling population, independent observations, p-values or confidence intervals are assumed. Comparisons with explicitly defined random models would concern model behaviour, not randomness asserted of the primes.

## 13 Potential utility for future research

The classification may help organise maximal-gap catalogues into sequential and skipped-level expansions. Joining these records to first-occurrence tables supplies reproducible recovery orders, completion points and several distance measures. A larger study could compare how these statistics change across numerical scales while preserving the observation boundary and incomplete cases.

Probabilistic models offer a separate comparative setting. Cramér-type models and their refinements do not automatically describe every feature of actual prime gaps; Granville discusses important limitations [8], and Banks, Ford and Tao develop a model incorporating sieving [9]. Kourbatov studies maximal-gap distributions in Cramér's model, and Kourbatov and Wolf examine record-gap trends [10–11]. Applying the same rupture and recovery definitions to specified models may reveal useful agreements or discrepancies. No such model experiment is claimed in this paper.

Paper Two could test factorisation patterns, prime powers, parity, sieve depth, factor covers, midpoint symmetry and primorial relationships in rupture interiors, against matched gaps of similar length and location. The oasis hypothesis could prove to be merely a memorable description of compositeness; that negative result would still clarify the framework. Alphabetic factor language, predictive modelling, twin-prime centres and composite-index grids remain outside Paper One. The tree also offers an accessible teaching representation of record growth and the difference between computation and proof.

## 14 Limitations

The global large-number results rely on published exhaustive searches rather than a new exhaustive sieve. The source database flags and its stated coverage differ for candidate 69; this paper adopts the conservative boundary. First-occurrence endpoint cross-checks against a second publication cover steps through 721, not every later recovery. Shared provenance limits independence. Local primality verification cannot resolve unseen earlier occurrences. Prime-index distances are available only inside the direct sieve.

The literature search is focused rather than exhaustive. Existing half-gap and record-difference sequences limit novelty claims. The main tree is a chosen representation and the oasis is descriptive. No matched-control factor-richness result, universal recovery theorem, universal delay bound, fractal structure or predictive mechanism is established. The original odd-composite comparison does not establish prime-specificity.

Negative and inconclusive findings are substantive: the maximum delay rises from three to eight on extension; the final confirmed events remain unresolved; candidate 69 lacks coverage at the adopted boundary; and proposed structural or causal interpretations are unsupported. The original numerical observation remains useful without those interpretations.

## 15 Open questions

1. How do recovery order and complete-recovery delay change as exhaustive coverage grows, with the same censoring and event-count conventions?
2. Which explicitly specified prime-gap models reproduce the joint behaviour of rupture frequency, jump size and recovery delay?
3. After accounting for numerical scale and skipped-set size, what descriptive variation remains in the last recovered level and completion distance?
4. Do matched ordinary gaps explain all apparent factor structure in rupture interiors, or does any robust difference remain?
5. Can the centred tree measurably improve understanding of record gaps and finite computational evidence in a teaching study?

Polignac's conjecture asserts infinitely many consecutive-prime gaps of each positive even size. It would imply recovery of every skipped level. Recovery needs only a first occurrence of each skipped size and is not proved by existing bounded-gap results [5,12]. No new conjecture is advanced here.

## 16 Conclusion

Prime-gap ruptures distinguish sequential record-gap growth from record jumps that bypass intermediate half-gap levels. The first event, 113→127, and its recovery are exact and readily visualised. The declared exhaustive boundary supports 68 ruptures and complete recovery for 66; two remain censored and one further listed candidate is retained separately. Skipped sets and their recovery provide reproducible objects for future computational study. Their potential utility is sufficient to motivate this observational framework without a claim of prediction or a universal law.

{{CLASSIFICATION}}

## Declaration of generative AI and AI-assisted technologies

During preparation of this work, the author used OpenAI Codex in ChatGPT Work (GPT-5, accessed 13–14 September 2026), under his direction, to assist with manuscript restructuring, mathematical and computational auditing, Python code development and testing, literature discovery, tabulation and figure generation. The originating concept, prime-step representation, source manuscript, spreadsheet and research direction were supplied by the author. All numerical claims used in the paper were checked using the documented code and cited source data; the computational record is released for independent inspection. The author reviewed and approved the manuscript and accepts responsibility for its claims and interpretation. The AI system is not an author.

## 17 References

[1] Prime Gap List Project. Prime Gap Records, allgaps.sql snapshot and data-field documentation. Accessed 13 September 2026. https://github.com/primegap-list-project/prime-gap-list ; https://primegap-list-project.github.io/prime-gap-record-data-fields/

[2] Prime Gap List Project. Exhaustively analyzed gaps. Accessed 13 September 2026. https://primegap-list-project.github.io/fully-analyzed/

[3] OEIS Foundation. A002386, record-gap lower primes; A000101, upper primes; A005250, record-gap values. B-files accessed 13 September 2026. https://oeis.org/A002386 ; https://oeis.org/A000101 ; https://oeis.org/A005250

[4] OEIS Foundation. A000230, smallest lower prime for each even gap. B-file through step 721, accessed 13 September 2026. https://oeis.org/A000230

[5] H. Mlcousek and OEIS contributors. A014321, first-occurrence half-gap order; B-file by Brian Kehrig, with earlier terms by Ferenc Adorjan. Accessed 13 September 2026. https://oeis.org/A014321

[6] J. Burch and OEIS contributors. A053695, differences between record prime gaps. Entry originated 23 March 2000. Accessed 13 September 2026. https://oeis.org/A053695

[7] J. P. Sorenson and J. Webster. Strong pseudoprimes to twelve prime bases. Mathematics of Computation 86 (2017), 985–1003. https://doi.org/10.1090/mcom/3134

[8] A. Granville. Harald Cramér and the distribution of prime numbers. Scandinavian Actuarial Journal 1995, 12–28. https://www.dms.umontreal.ca/~andrew/PDF/cramer.pdf

[9] W. Banks, K. Ford and T. Tao. Large prime gaps and probabilistic models. Inventiones Mathematicae 233 (2023), 1471–1518; corrected author version 2025. https://arxiv.org/abs/1908.08613

[10] A. Kourbatov. The distribution of maximal prime gaps in Cramér's probabilistic model of primes. International Journal of Statistics and Probability 3(2) (2014), 18–29. https://arxiv.org/abs/1401.6959

[11] A. Kourbatov and M. Wolf. Predicting maximal gaps in sets of primes. Mathematics 7(5) (2019), 400. https://arxiv.org/abs/1901.03785

[12] J. Maynard. Small gaps between primes. Annals of Mathematics 181 (2015), 383–413. https://arxiv.org/abs/1311.4600

[13] C. Caldwell. The Gaps Between Primes. PrimePages. Accessed 13 September 2026. Uses the alternative convention counting interior composites. https://t5k.org/notes/gaps.html

## 18 Computational appendix

The following complete catalogue includes confirmed events 1–68 and the clearly separated candidate 69. Upper endpoints are obtained exactly as q=p+g. The accompanying CSV gives both endpoints, skipped sets, status, completion points and recovery order. The separate recovery dataset has one row per skipped level, including censored and outside-boundary rows. A separate audit supplies all corrections to the original text and spreadsheet.

{{CATALOGUE}}

{{PROVENANCE}}

The analysis stops on any mismatch between source records, local sieve, first-occurrence cross-checks or consecutiveness tests. The automated suite covers the exceptional initial gap, initialisation, records, sequential expansions, ruptures, skipped sets, recovery, censoring, the original thirteen rows and expanded checkpoints. Tests check implementation and finite data; they do not establish any universal recovery proposition.
