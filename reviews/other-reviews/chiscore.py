#!/usr/bin/env python

# chmod +x chiscore.py 

# I also have a simple script to calculate the average weighted score 
# (the one you would see in PCS as a reviewer). You can just feed it 
# a reviews.txt file from PCS, as follows:

# $ ./chiscore.py review-2133.txt 
# Scores: 3.0 (exp. 2), 2.0 (exp. 3), 4.5 (exp. 2), 4.5 (exp. 3), 1.0 (exp. 4)
# Average score: 2.85

# It has been my experience that papers above 3.25 have a reasonable chance 
# of getting in with a good rebuttal and bumped up scores 
# (those above 3.5 of course stand a better chance). Papers below 3 are more difficult. 
# Those below 2.5 typically do not make it to the PC meeting, but writing a rebuttal 
# can still help, you never know.  The 1AC (primary) and 2AC (secondary) scores are 
# also essential.

#  Jo Vermeulen [j.vermeulen@cs.bham.ac.uk] 




from __future__ import print_function
import sys
import re

"""Parses a review rating."""
def parse_rating(line, lineno):
    # e.g. '3.5 . . . Between neutral and possibly accept'
    m = re.search("[0-9](.[0-9])*", line)

    if m is None:
        print("Rating not found on line %d." % lineno)
        print("Are you sure this is the right format?")
        print("Exiting..")
        sys.exit(1)

    return m.group(0)

"""Parses an expertise rating."""
def parse_expertise(line, lineno):
    # e.g. '3  (Knowledgeable)'
    m = re.search("[0-9]", line)
    if m is None:
        print("Expertise not found on line %d." % lineno)
        print("Are you sure this is the right format?")
        print("Exiting..")
        sys.exit(1)

    return m.group(0)

"""Returns the weighted average for a list of (score,expertise) tuples.""" 
def weighted_score(scores, weights = {1:0.75,2:1.0,3:1.25,4:1.5}): 
    # weights = PCS weights 
    #   e.g. 1 = No knowledge, 2 = Passing knowledge, 3 = Knowledgeable, 4 = Expert

    used_weights = []
    wsum = 0
    for (score, expertise) in scores:
        # Get weight
        weight = weights[expertise]
        # Calculate weighted sum
        wsum += score * weight
        # Add to list of used weights for denomerator
        used_weights.append(weight)

    return wsum / sum(used_weights)

"""Parses a PCS review.txt file."""
def parse_reviews(reviews):
    score_exp = [] # List of ratings and expertises 
    rflag = False  # Next line is a review rating
    eflag = False  # Next line is an expertise score 
    lineno = 0

    for line in reviews:
        lineno += 1
        line = line.rstrip()
        # Ignore blank lines
        if not line: continue 

        if 'Overall Rating' in line or 'Overall Recommendation' in line:
            # Skip and use next line for rating
            rflag = True
            continue
        if 'Expertise' in line or 'Confidence' in line:
            # Skip and use next line for expertise
            eflag = True
            continue

        if rflag:
            # Parse and add a review rating
            score_exp.append(parse_rating(line, lineno))
            rflag = False
        elif eflag:
            # Parse and add an expertise rating
            score_exp.append(parse_expertise(line, lineno))
            eflag = False
                
    # Combine score and expertises pairwise: e.g. (3,3), (4.5,4), (2,2)
    scores = zip(score_exp[0::2], score_exp[1::2])
    # Convert to ints and floats for calculations
    scores = [(float(s),int(e)) for (s,e) in scores]

    # Calculate result
    result = weighted_score(scores)
    pscores = ', '.join(["%.1f (exp. %d)" % (s,e) for (s,e) in scores])
    print("Scores:", pscores)
    print("Average score: %.2f" % result)

    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        # Try to read from stdin
        #   e.g. cat review-1024.txt | ./chiscore.py
        rfile = sys.stdin
    else:
        # Review text file provided as input
        #   e.g. $ ./chiscore.py review-1024.txt
        rfile = open(sys.argv[1])

    # Calculate and print result
    parse_reviews(rfile)

    # Cleanup
    if rfile is not sys.stdin:
        rfile.close()
