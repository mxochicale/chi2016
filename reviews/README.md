CHI 2016 Papers and Notes

Reviews of submission #2133: "Dancing in Time:  applying time-series
analysis to human activity"

------------------------ Submission 2133, Review 4 ------------------------

Reviewer:           primary

Your Assessment of this Paper's Contribution to HCI

   The paper presents an interesting approach to detect user dexterity using
   a time-series algorithm applied to sensor data. This topic is relevant to
   the CHI community and could potentially unlock new interaction
   approaches.

Overall Rating

   3.0 - Neutral: Overall I would not argue for accepting or rejecting this paper. 

Expertise

   2  (Passing Knowledge)

The Review


The Meta-Review

   The paper presents a super relevant topic for the CHI community. All
   reviewers agreed that this is an incredibly important area of research
   and encourage the authors to continue exploring these approaches as they
   could potentially unlock new forms of interactions for the design of
   computing systems.

   Reviewer 3 drafted a pretty honest review of the work, highlighting its
   merits and its limitations. I encourage the authors to pay special
   attention to this review in their rebuttal.

   I concur with R3 in many of the points. Particularly, the current
   presentation of the approach lack very important information in the paper
   that impede the readers from understanding exactly the method being used
   and the actual contributions of the presented work. Without specific
   information on the apparatus being used, the approach to data collection,
   and detailed information about the sample used in the study, it would be
   difficult or impossible for other researchers to reproduce the study. R1
   also raised questions on the sampling and others related to the
   methodology.

   Also, the authors need to be more specific with regard to what differs in
   the proposed approach compared to the existing methods. Was time-series
   never applied before to dexterity recognition? How does this study differ
   from the previous literature? In this regard, R3 provides an amazing
   review of previous work that has not been included in the current version
   of the paper. It would be important for the authors to review these works
   and explain exactly how their proposed approach differs from these.

Publicity Headline



------------------------ Submission 2133, Review 5 ------------------------

Reviewer:           secondary

Your Assessment of this Paper's Contribution to HCI


Overall Rating

   2.0 - Possibly Reject: The submission is weak and probably shouldn't be
   accepted, but there is some chance it should get in.

Expertise

   3  (Knowledgeable)

The Review

   The paper aims to extend activity recognition from simply recognizing
   activities to an assessment of the quality of performing an activity. The
   overall motivation of the work is clear. Instead of simply recognizing
   that an activity has been performed, there are a number of situations in
   which it would be more relevant to recognize how the activity has been
   performed. While previous work investigated how specific activities have
   been performed, this paper aims towards a general process to determine
   the quality of an activity. However, the authors’ motivation is not
   clear and not specific. The contribution of the paper is not made
   explicit. The paper misses a dedicated related work section and lacks a
   detailed discussion of previous work. I'm not an expert in this
   particular field but the recent UbiComp paper by Khan et al. [1] comes to
   mind. Khan et al. provide a detailed discussion of related work and much
   of the motivation that could be part of the paper under review. The
   submitted paper does not only contain no dedicated related work section,
   it only provides a single reference to a survey paper. This is certainly
   not sufficient.

   The purpose of the section on "Quantifying Dexterity in Human Motor
   Performance" remained somewhat unclear to me. The section start with the
   simple conclusion that recognizing an activity is not the same as
   recognizing the quality of an activity. The section provides two
   references and the final conclusion PCA is not suitable for accelerometer
   data because the application of PCA to accelerometer data could skew the
   analysis of the data itself. Unfortunately, I did not get why this is a
   general limitation of PCA.

   The following section describes one specific approach. While it is
   certainly fine to investigate a specific approach, it would be more
   convincing is the authors would discuss why this approach is promising
   compared to others.

   The paper presents two studies that applies the proposed approach. It
   seems that the first study has been described in the authors’ previous
   publications. Unfortunately, (and in contrast to CHI's anonymization
   policy) the authors removed the references from the list of references.
   The description of the first study is weak. No information about the
   participants are, for example, provided. The analysis remains on a very
   informal level. The description of the second study is much better. 
   While a number of participants took part in the study, the paper focussed
   on the data from 3 individual participants without any reason. Again. The
   analysis is weak and remains on the level of visual inspection. This is
   certainly not sufficient.

   Overall, the authors follow a very interesting direction. I agree that
   the activity recognition community focussed too much on simply
   recognizing activities instead of determining the qualities of the
   activities. Unfortunately, the paper provides no clear contribution and
   no discussion of previous work. Instead, the paper should clearly
   motivate the work, the contribution should be clearly articulated, and I
   recommend to reflect on previous work in a dedicated related work
   section. The description of the first study in unclear and the analysis
   not helpful. The description of the second study is much better. However,
   the analysis only considers three participants and remains on a level
   that is not helpful at all. In conclusion, the paper is not connected to
   previous work and the studies provide no contribution. Therefore, I would
   not argue for accepting the paper.

   [1] Khan et al.: Beyond activity recognition: skill assessment from
   accelerometer data. Proc. UbiComp, 2015.

The Meta-Review

   The scores provided by the reviewers cover a considerable range
   (2.0-4.5). All reviewers agree that the general topic is interesting and
   relevant. R3 provides a detailed assessment of the paper. That I largely
   agree with. According to R3, the general direction and topic of the
   submission are relevant for the community. Major limitations of the
   paper, according to R3, are that "the authors don’t present any
   statistical evaluation to underline their claims", that "the authors
   don’t answer how “useful” their metric is", that "how the approach
   compares to other Time Series Analysis methods assessing the quality of
   movements", and that it is unclear "what is new in the authors approach".
   Furthermore, R3 provided references to highly relevant related work that
   needs to be discussed. Overall, I agree with R3's assessment of the
   paper. While the direction is interesting, the work is not ready for
   publication.

   If the authors decide to provide a rebuttal, they might want to:
   * Provide an overview about the paper's connection to related work
   provided by R3.
   * Clearly state the paper's contribution beyond the state of the art.
   * Discuss why visual inspection is sufficient or provide quantitative
   results.
   * Discuss why only reporting results of 3 participants is sufficient or
   provide results for the other participants.

Publicity Headline



------------------------ Submission 2133, Review 1 ------------------------

Reviewer:           external

Your Assessment of this Paper's Contribution to HCI

   This work presents a power spectral density plots to characterize
   dynamical data based on dexterity of activity as measured from Inertial
   Measurement Units (IMUs).  They show that techniques from time-series
   analysis can be used to measure how human activity is performed and
   coordinated.

   By analysis of simple, repetitive actions using saws, they reconstruct
   time series and show that their differences could show the variation in
   dexterity of the activity participants.   
   In that case, they also explore the ratios of the log of frequency to log
   of power in the signal, showing that this could be interpreted as the
   level of stability in the control of the saw for this task, with lower
   dexterity arising from less stable control and resulting in a shallower
   slope in the graph.

   Similar methods of analysis is performed on analyzing 2 steps on two
   types of dances; comparing an expert dancer, intermediate dancer and not
   dancer.




Overall Rating

   4.5 . . . Between possibly accept and strong accept 

Expertise

   2  (Passing Knowledge)

The Review

   Significance of the paper's contribution to HCI and the benefit that
   others can gain from the contribution: why do the contribution and
   benefit matter?

        Clear relevance for the CHI field. It analyzes a signal in terms of
   quality which can easily find applications on HCI.



   Originality of the work: what new ideas or approaches are introduced? 

        References 17 and 18 are not uploaded to evaluate possible overlap.
   However, based on the references presented it is the an original
   application of time series reconstruction tackled towards dexterity.

   We want to emphasize that an acceptable paper must make a clear
   contribution to Human-Computer Interaction;

         It has a clear contribution to HCI      

   Validity of the work presented: how confidently can researchers and
   practitioners use the results?
   Presentation clarity;
           The results are clearly presented and the technically sound..


   Relevant previous work: is prior work adequately reviewed? 
            Yes.


   Questions:

   1.	Were only 3 participants studied in the sawing case? This was not
   clarified. 

   2.	Why only few illustrative cases are used to show the technique. What
   can be concluded and quantified by looking at the data of the
   13participans. Can you quantify the degree of expertise further by
   comparing the differences of several participants?

   3.	Why in the dancing case it was not shown the plot log of frequency to
   log of power in the signal as in the previous case?


------------------------ Submission 2133, Review 2 ------------------------

Reviewer:           external

Your Assessment of this Paper's Contribution to HCI

   Main contribution: 
   (1) new recording technology that enables the use of a combination of
   sensors that facilitates longitudinal studies of activity over long
   period of time,  and 
   (2) shift the focus from specific actions or events to a focus on how
   activity might change over time. It certainly allows a welcome renewal of
   the characterization of dexterity.


Overall Rating

   4.5 . . . Between possibly accept and strong accept 

Expertise

   3  (Knowledgeable)

The Review

   Significance of the paper's contribution to HCI and the benefit that
   others can gain from the contribution: why do the contribution and
   benefit matter? 
   The main contribution is twofold
   1/ propose the use of new recording technologies (combination of sensors)
   that allow for analysing activity over long period of time contrary to
   techniques usually measuring discrete actions;
   2/ this technology breakthrough will have real theoretical advances as it
   allows for a shift of focus in the study of activity.  It should 
   participate in better assisting people especially in case of
   rehabilitation. 

   Originality of the work: what new ideas or approaches are introduced? We
   want to emphasize that an acceptable paper must make a clear contribution
   to Human-Computer Interaction; 
   Finding reliable ways to analyse behaviour and characterise how it can
   vary over long periods of time is a challenge in a world where people do
   interact with many kind of computers for hours throughout the day. This
   paper is a step in this direction.

   Validity of the work presented: how confidently can researchers and
   practitioners use the results? 
   The recording techniques as well as the analytical methods described in
   this paper propose an positive way to explore how activity changes over
   time. The methods (recording and analysis) described in the paper can be
   applied to real life activity, which represents a true step forward.

   Presentation clarity; 
   Good. 

   Relevant previous work: is prior work adequately reviewed? 
   Yes


------------------------ Submission 2133, Review 3 ------------------------

Reviewer:           external

Your Assessment of this Paper's Contribution to HCI

   The paper describes a method to calculate some metric (authors call it
   “dexterity”) for assessing a user’s skill for sawing by jewelry
   students and salsa dancing. Overall interesting for the CHI community.

   +interesting topic
   - crucial definitions missing
   -lack of detail in the methodology
   -comparison to other methods missing
   -results hard to reproduce

Overall Rating

   1.0 - Reject: I would argue for rejecting this paper. 

Expertise

   4  (Expert )

The Review

   +interesting topic
   - crucial definitions missing
   -lack of detail in the methodology
   -comparison to other methods missing
   -results hard to reproduce

   The paper leaves me conflicted. I like the general direction and the
   topic of the submission, I don't feel the contributions are enough for a
   CHI paper and the paper has a lot of issues in terms of reproducibility,
   methodology and related work.

   The direction of the research is relevant to the community and I
   encourage the authors to continue submitting to the CHI related
   conferences even though the current work lacks maturity.
   I hope the comments bellow increase the quality of the next submission.

   “From visual inspection …” actually for me the difference in motion
   is already visible from the “raw” acceleration or velocity data (the
   authors use both optical trackers and IMUs, yet it’s not sure which
   metrics they use from each. IMUs give angular! velocity, acceleration and
   magnetic field readings … one can also get quaternions). This leads me
   to the biggest problem of the work, I’m not sure what the authors used
   for their analysis, the plots show “raw velocity profile” and the
   y-axis is inscribed with “raw data”. It seems hidden in an undefined
   reference “Details of the data collection and analysis can be found in
   [18].
   The authors don’t present any statistical evaluation to underline their
   claims .e.g.
   “ …expert dancers are better able to moderate their actions in
   response to contextual demands in a way that produces a state space
   reconstruction that appears consistent. ”

   Also the authors don’t answer how “useful” their metric is. I’m
   fairly familiar with IMU based activity recognition and can detect the
   skill of a dance performer or athlete just looking at the raw signal …
   Not sure why I need their technique for analysis.

   From the title, I expected some automatic classification, from the data
   obtained this is definitely possible. What is unclear to me is how the
   approach compares to other Time Series Analysis methods assessing the
   quality of movements (e.g. Dynamic Time Warping comes to mind). Also from
   the write-up I don’t really understand what is new in the authors
   approach, it seems that  they apply an already known method? The
   introduction just mentions the research questions but not the concrete
   contributions of the work.

   The experimental description is lacking for both experiments. It’s
   unclear which apparatus was used (which IMU units) the exact experimental
   procedure is lacking. For me, it’s very difficult to reproduce the
   experiments, if I would try. Also the expertise levels are fairly crude.
   As far as I understand, there are only 3 skill classes for the dancing
   (assigned a priori by the length of training: no-dancer,
   intermediate,expert).


   Regarding related work, the papers cited are a bit dated (except of the
   Tutorial from Bulling et al.) and not sufficient.  The authors cite
   previous works of  Ploetz  but not the most recent (most relevant). There
   are a lot of CHI and UbiComp researchers looking into skill assessment
   using wearable and other sensors. 
   Khan, Aftab, et al. "Beyond activity recognition: skill assessment from
   accelerometer data." Proceedings of the 2015 ACM International Joint
   Conference on Pervasive and Ubiquitous Computing. ACM, 2015.

   Khan et al. is the most relevant of the related work and I think answers
   a couple of questions the authors raise in their introduction.

   There are a lot of papers using other methods to evaluate and compare
   “dexterity” related metrics. One field with a lot of references and
   related work is handwriting recognition. 

   Di Brina, Carlo, et al. "Dynamic time warping: A new method in the study
   of poor handwriting." Human movement science 27.2 (2008): 242-255.

   Also evaluating motion is very common in sports, the work presented here
   reminds me on older quantitative signal level assessments:
   Ohgi, Y., Yasumura, M., Ichikawa, H. & Miyaji, C. , 2000, Analysis of
   stroke technique using acceleration sensor ic in freestyle swimming, in
   A. J. Subic & S. J. Haake, eds, ‘The Engineering of SPORT’, Blackwell
   Science, pp. 503–511.
   De Morais, Wagner O., and Nicholas Wickström. "A serious computer game
   to assist Tai Chi training for the elderly." Serious Games and
   Applications for Health (SeGAH), 2011 IEEE 1st International Conference
   on. IEEE, 2011.
   Heinz, Ernst, et al. "Using wearable sensors for real-time recognition
   tasks in games of martial arts-an initial experiment." Computational
   Intelligence and Games, 2006 IEEE Symposium on. IEEE, 2006.

   Structure:
   Basically well written, yet hard to follow structure. No direct  related
   work section, the intro reads strange. Wondering why the authors have the
   activity recognition architecture in Figure 1 if they don’t do any
   classification. Also there are a lot of different tool chains etc.
   similar and different to Figure 1 … not necessary why this was included
   (also the Bulling reference seems strange as not so related to the paper
   direction … general activity recognition overview for people new or
   unfamiliar to the field).

   Also the paper is not correctly anonymized: (see
   http://chi2015.acm.org/authors/chi-anonymization-policy/ )

   “The work reported in this paper is partly supported by a studentship
   from National Council for Science and Technology, CONACyT, Mexico. “
   two blinded references:
   	16.	Xx  
   	17.	Xx  
   Overall I cannot recommend the paper for acceptance. Yet encourage the
   authors in their research, it’s a bit early from the results provided
   yet an interesting direction.



