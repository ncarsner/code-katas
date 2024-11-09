"""
GOAL: Back-end filtering of survey/vote/ranking values
if front-end processes fail
to prevent fraudulent, spam, or otherwise unqualified submissions.
"""
from random import randint

no_of_survey_questions = 10
no_of_participants = 237
min_score = 1
max_score = 10

# QUALITY CONTROL QUESTIONS (e.g. question 6 is "please enter 5 for this question")
control_questions = {6: 5}

# RAW LIST OF LISTS (user input)
unfiltered_responses = [
    [randint(min_score, max_score) for j in range(no_of_survey_questions)]
    for _ in range(no_of_participants)
]

# FILTERED LIST OF USER INPUT BASED ON: 1) CONTROL QUESTION VALUES and 2) NOT ALL RESPONSE VALUES ARE THE SAME
filtered_responses = [
    subset for subset in unfiltered_responses
    if all(subset[k - 1] == v for k, v in control_questions.items()) and (len(set(subset)) != 1)
]

filtered_pct = len(filtered_responses) / len(unfiltered_responses)

# DISPLAY UNFILTERED RESPONSES AND AVG QUESTION SCORES
print(
    f"\nParticipants: {len(unfiltered_responses):,}\nFiltered: {len(filtered_responses)} ({filtered_pct:.1%} of unfiltered list)\n"
)

for question in range(no_of_survey_questions):
    score_unf = sum([r[question] for r in unfiltered_responses]) / len(unfiltered_responses)
    score_fil = sum([r[question] for r in filtered_responses]) / len(filtered_responses)
    print(
        f"Question {question + 1} avg: {score_unf:.1f} | filtered: {score_fil:.1f} -- diff: {score_fil-score_unf:+.1f}"
    )


# >>> SAMPLE OUTPUT
# Participants: 1,000
# Filtered: 104 (10.4% of unfiltered list)

# Question 1 avg: 5.4 -- filtered: 5.4 -- diff: +0.0
# Question 2 avg: 5.5 -- filtered: 5.6 -- diff: +0.0
# Question 3 avg: 5.5 -- filtered: 5.3 -- diff: -0.2
# Question 4 avg: 5.6 -- filtered: 5.6 -- diff: +0.0
# Question 5 avg: 5.5 -- filtered: 5.8 -- diff: +0.3
# Question 6 avg: 5.4 -- filtered: 5.0 -- diff: -0.4
# Question 7 avg: 5.5 -- filtered: 5.2 -- diff: -0.2
# Question 8 avg: 5.5 -- filtered: 5.3 -- diff: -0.3
# Question 9 avg: 5.3 -- filtered: 4.8 -- diff: -0.5
# Question 10 avg: 5.6 -- filtered: 5.2 -- diff: -0.4
