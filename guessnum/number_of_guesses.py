def comments(tries):
    if tries == 1:
        return "You are a mind reader!"
    elif 2 <= tries <= 4:
        return "Most impressive."
    elif 5 <= tries <= 8:
        return "You can do better than that."
    else:
        return "Have you got no shame?!"