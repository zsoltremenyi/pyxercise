import re


def zipcode(zipc):
    if re.match("^[0-9]+$", zipc):
        return zipc
    return "Zipcodes may only contain numbers."
