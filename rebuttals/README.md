
# REBUTTAL

We are delighted that the topic of the paper is “super relevant” (R5), which is
acknowledged by R1 and R4, and that R3 likes “the general direction and the
topic of the submission”. R4 notes that the “motivation for the work is clear”,
and the goal is to “shift the focus from specific actions or events to a focus
on how activity might change over time.” This is, indeed, our goal.  Thus, we
were disappointed that R3 says “from the title, I expected some automatic
classification” because this would position the work in the ‘specific actions or
events’ paradigm, which is not what we intend. Clearly we need our revision to
make this distinction clearer, and elaborate on this in the next two
sections. We also recognise that the reviewers were concerned with the
presentation of the data collection and analysis, and these issues are responded
to later.  

## VARIANCE AND VARIABILITY 
The crux of our argument is the distinction
between variance (in signals) and variability (in human activity). On
reflection, this distinction is (we feel) clear in the text, but confused by the
inclusion of figure 1.  We will remove this figure and, in its place, provide a
critical discussion of the techniques reviewed in the Khan et al paper
(recommended by R4 and R3) and the recent papers of Ploetz (recommended by R3)
with techniques applied to analysing dexterity (from the biomechanics
literature) that we use.  Signal processing techniques typically seek to ensure
that variance in the data is sufficiently constrained for classifications to be
statistically meaningful.  For, say, walking and running, this would be
important.  Khan et al treat ‘skill’ in a similar manner. We note that R3
defines Dynamic Time Warping as time-series analysis; in this approach,
‘landmarks’ in the signal are used to align corresponding points. These
techniques share the goal of reducing variance and consequently process out
variability.  


## SKILL AND DEXTERITY 
We take pains to distinguish between skill and
dexterity in our paper (R3 does not engage with this distinction, so we assume
that, for this reviewer, the terms are synonymous).  For us, ‘skill’ could be
discretised (and the approach proposed by Khan et al makes perfect sense) but we
do not believe that ‘dexterity’ is similarly discrete.  Following Bernstein,
dexterity involves the balance between stability of movement (to ensure
consistency and repeatability) and variability (to allow adaptation to
situational demands). Conceptually, classification techniques focus on stability
and ignore (or process out) variability.  We want to find techniques which do
not reject variability.  To this end, the paper is, as R2 notes, a “welcome
renewal of the characterisation of dexterity”.  

## REPORTING OF EXPERIMENTS 
We accept that we have been lax in our description of the data collection. In the
first study, we need to indicate the number of participants (N = 16) and provide
more detail on the method of data collection.  We will remove the discussion of
1/f scaling – this was intended to provide an alternative approach to exploring
human motor control but we think that it confuses this paper. Also, this
analysis is in [17], presented at an international conference in October ([17]
has no mention of time-series analysis).  Incidentally, we were confused by the
requirement of R2 to upload our papers because we couldn’t see how this could
maintain anonymous reviewing.  

## REPORTING OF ANALYSIS 
A key problem with the
paper was the reporting of the results.  First, we have analysed the data from
all 13 ‘non-dancers’, but did not include them in the paper (we kept with 1 of
each type of ‘skill’ because we had only 1 ‘expert’).  With hindsight, this was
a silly choice and the revision will include all of the data.  Providing these
data would allow statistical comparison; a set with 1 instance per category can
only be analysed ‘by eye’ (and asking the reader to accept that a figure looks
like it shows a difference, leads to the result either being obvious or to be
taken on trust, and this problem was raised by R2 and R3).  

## COMPARISON WITH OTHER APPROACHES 
We have applied PCA to the raw data from study two (using the
technique described by Hammerla et al) and could provide this analysis in the
paper.  The problem is that this does not easily provide a like-with-like
comparison; the approaches make different assumptions about the underlying human
activity from which data originates. As R2 points out “finding reliable ways to
analyse behaviour and characterise how it can vary over long time periods is a
challenge...” Such activity cannot solely be considered in discrete terms but
requires us to think of new approaches that can take variability into account.
That is what we seek in this paper, which is, as R2 concludes “a step in the
right direction”.

We believe that this submission raises critical questions for CHI concerning the
analysis of human activity and that the paper could provoke an interesting
debate at conference.

