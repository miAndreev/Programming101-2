def slope_style_score(scores):
    score = 0
    score_summ = sum(scores)
    score_summ = score_summ - min(scores) - max(scores)
    score = score_summ/(len(scores)-2)  
    #score = round(score, 2)
    return score