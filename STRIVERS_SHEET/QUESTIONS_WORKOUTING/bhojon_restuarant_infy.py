"""
Problem Statement:
Bhojon is a restaurant company that has started a new wing in a city. They have every type
of cook except a meatball artist. They want to hire one from a pool of candidates. Each
candidate has a skill rating. Bhojon wants to hire the candidate whose skill rating is closest to
their required skill level. If two candidates are equally close, hire the one with the lower skill
rating.



"""

no_candidate=int(input())
candidates=list(map(int,input().split(" ")))
skill_rate=int(input())
skill_change=float('+inf')
for index,candidate in enumerate(candidates):# we get the index and val
    change=abs(candidate-skill_rate)
    if change<skill_change:
        skill_change=change
        res=candidate
    if change==skill_change:
        res=min(candidate,res)
    else:
        continue


print(res)