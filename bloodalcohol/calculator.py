def b_alc_calc(alcohol, weight, gender, hours):
    distr_ratio = 0
    if gender == "m":
        distr_ratio = 0.73
    else:
        distr_ratio = 0.66

    BAC = (alcohol*5.14/weight*distr_ratio) - 0.017*(hours/60)
    return BAC