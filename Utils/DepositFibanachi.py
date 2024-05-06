from datetime import date
from math import sqrt

def fibonacci():
    today = str(date.today()).split('-')
    day = int(today[2])
    phi = (1 + sqrt(5)) / 2
    psi = (1 - sqrt(5)) / 2
    return int((phi**day - psi**day) / sqrt(5))