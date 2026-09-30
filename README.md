# The Unofficial Guide

Name: Igor Polidva | Corpus: advice_threads

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. --> I picked up advice_threads because information is very concise and even has a relevanse score (numbers of votes). It's looks like reddit with 1 question and 3 answers per topic. All corpus is about life on campus for example what meal plan to choose, where to study, etc.
     

## Chunking Strategy

**Chunk size:** 300
**Overlap:** 100

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. --> I just tried couple random numbers based on the goal that ideal output, that should include 1 most relevant response (most voted). And this particular combination return the longest shortes chunk as 28 and 300 is enough to capture the longest most voted response.

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `thread_bike_commute.txt` — produced by: `chunker.py::split_documents`

```
THREAD: Is a bike worth it for a 20 minute walk commute?

--- reply 1 (14 votes) ---
Yeah. Cuts an 18 minute walk to about 6. The thing nobody mentions is storage — covered bike parking exists at three buildings and is full by 9am at all three.
```

**Chunk 2** — source: `thread_commuting.txt` — produced by: `chunker.py::split_documents`

```
--- reply 4 (17 votes) ---
I commuted for two years. The thing that made it work was treating the train as study time rather than dead time.
```

**Chunk 3** — source: `thread_laptop_specs.txt` — produced by: `chunker.py::split_documents`

```
THREAD: How much laptop do I actually need for CS courses?

--- reply 1 (31 votes) ---
Less than the recommended spec page says. 16GB of RAM is the one number worth paying for; everything else you'll never notice.
```

**Chunk 4** — source: `thread_office_hours_etiquette.txt` — produced by: `chunker.py::split_documents`

```
THREAD: Is it weird to go to office hours with no specific question?

--- reply 1 (44 votes) ---
No, and this is the single most common thing first years get wrong. 'I'm following the lectures but I don't feel like I understand the shape of it' is a completely normal thing to say.
```

**Chunk 5** — source: `thread_professor_email.txt` — produced by: `chunker.py::split_documents`

```
--- reply 3 (15 votes) ---
Empty office hours is the biggest unused resource here and I say that having wasted a year not going.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
What clothes do students recommend for the winter?

**Answer:**

```
(best distance 0.513, cutoff 0.6)
Students recommend wearing layers rather than a big coat, as well as boots with actual tread. (Source: thread_winter_advice.txt)
```

**My relevance cutoff:**
0.6


<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| What do students say about parking availability? | Yes | 0.530 |
| What clothes do students recommend for the winter? | Yes | 0.513 |
| Which meal plan tier is right? | Yes | 0.232 |
| What are best study spots that aren't the library? | Yes | 0.391 |
| What laptop do I need for CS classes? | Yes | 0.296 |
| What is the capital of Mongolia?	| No | 0.904 |
| How do I change the oil in a diesel engine? | No | 0.898 |
| Who won the 1994 World Cup? | No | 0.859 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.760 |
| How do I write a for loop in Rust? | No | 0.823

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->
     


**1.**
"I asked Gemini what aproaches existed for chunking. It introduced me to langchain_text_splitters, aproach using Splitting by double newlines (\n\n) and chunking with Overlap. I choosed the langchain_text_splitters, because it looks like the most flexible"

**2.**
AI helped me debugged my code. Remind me to install langchain_text_splitters (completely forgot that) and remind me that overlap cannot be more or equal chunk size.


<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks have "!" or "." in the end | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. All chunks have complete thoughts with no cut off at the start or at the end | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->
### Criterion Output Samples
**File & Function:** 
[Question] ──> store.py::search ──> gate.py::check ──(Pass)──> generate.py::answer_from_chunks ──> [Final Answer]
                                         │
                                      (Refuse)
                                         │
                                         └──> gate.REFUSAL ("OUT_OF_SCOPE")

**Criterion 1: Retrieved chunk contains the answer**
* **Raw Output:**
What clothes do students recommend for the winter? — run 1

- Best distance: 0.5130 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_laundry_timing.txt, thread_winter_advice.txt

```
Students recommend wearing layers rather than a big coat, as well as boots with actual tread. (Source: thread_winter_advice.txt)
```


**Criterion 2: Every answer names a source**
* **Raw Output:**
What do students say about parking availability? — run 1

- Best distance: 0.5300 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_parking.txt

```
Students say that west lots sell out in about three days in August, while the east lot never sells out (though it is a 12-minute walk). Additionally, street parking on Verrill is legal, free, and unmarked, which is why half the upper years use it. 

Source: thread_parking.txt
```

**Criterion 3: Gate stops out-of-corpus questions**
* **Raw Output:**
python app.py ask "What is the capital of Mongolia?" 
  (best distance 0.904, cutoff 0.6)

I don't have enough information about that.

0 model calls this session

**Criterion 4: Chunks have "!" or "." in the end**
* **Raw Output:**
What are best study spots that aren't the library? — run 1

- Best distance: 0.3912 (passed the gate)
- Sources retrieved: thread_study_spots.txt

```
Based on the provided documents, the best study spots that aren't the library are:
- Ridgeway Café before 10am, which is empty, quiet, and has good coffee (thread_study_spots.txt).
- The open lounges on floors 2 through 5 of the science building, which are unlocked and almost always empty (thread_study_spots.txt).
```

**Criterion 5: Answer has exact citation of the source**
* **Raw Output:**
What clothes do students recommend for the winter? — run 1

- Best distance: 0.5130 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_laundry_timing.txt, thread_winter_advice.txt

```
Students recommend wearing layers rather than a big coat, as well as boots with actual tread. (Source: thread_winter_advice.txt)
```


## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | Each run returned the answer 5/5 > 4/5 |
| 2 | Every answer names a source | MET | Each run contained the correct file name 5/5 |
| 3 | Gate stops out-of-corpus questions | MET | Each run with out-of-scope question lead to refusal 5/5 > 4/5 |
| 4 | Chunks have "!" or "." in the end | MET | Each chunk has "!" or "." 5/5, i designed the chunker function keeping it in mind, so I'm glad that's work|
| 5 | All chunks have complete thoughts with no cut off at the start or at the end| MET | Complete though that is easy to understand without any context and it complete |

## Diagnoses

Nothing is missed chuunker function was developed after Criteria "Chunks have "!" or "." in the end" so it meeting it, by design. But if documents does not have clear definition of ending of the sentence, things can still go wrong, so it does not mean that the same criteria pass during the test phase for other corpus

Criteria 5 the same, corpus itself very well structured and each chunk has complete thought, for other corpus without clear sructure this criteria fail.

# Chunker overview
My chunker use RecursiveCharacterTextSplitter that create chunks based on Hierarchical Separators. 1 "\n\n" for paragraphs, 2 based on new line "\n", 3 spaces " ", 4 empty string "" splitting by character if maximum chunk size is smaller than 1 word. 
After splits trying to merge small chunks into bigger onece within the maximum size limit.
<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:** Criteria 4 is so easy with existing chunking function, which making chunks based on "." and "!".


<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
