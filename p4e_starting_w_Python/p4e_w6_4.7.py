# exersise 4.7
# Rewrite the grade program from the previous chapter
# using a function called computegrade that takes a score as its parameter
# and returns a grade as a string.


def computegrade(sc):
    if sc < 0.0:
        return 'Error: Score out of range'
    elif sc > 1.0:
        return 'Error: Score out of range'
    elif sc >= 0.9:
        return 'A'
    elif sc >= 0.8:
        return 'B'
    elif sc >= 0.7:
        return 'C'
    elif sc >= 0.6:
        return 'D'
    else:
        return 'F'

score = input('Enter Score: ')
sc = float(score)
grade = computegrade(sc)
print(grade)
