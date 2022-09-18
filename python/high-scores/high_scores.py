def latest(scores):
    return scores[-1]


def personal_best(scores):
    scores = sorted(scores, reverse = True)
    return scores[0]


def personal_top_three(scores):
    scores = sorted(scores, reverse = True)
    return scores[0:3]
