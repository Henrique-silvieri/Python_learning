# Create a program that has a function called grades() that can receive multiple grades from students 
# and will return a dictionary with the following information:
# A) Quantity of grades
# B) The highest grade
# C) The lowest grade
# D) The class average
# E) The situation (optional)
# Also, add the docstrings for the function.

def grades(*grade, situation=False):
    """
    grades(*grade, situation=False)
    :param grade: One or more grade of a student.
    :param situation: (Optional) If True, display the student's situation.
    :return: A dict containing several piaces of information about the student.
    """
    
    informations = dict()
    informations['total'] = len(grade)
    informations['maior'] = max(grade)
    informations['menor'] = min(grade)
    sumGrade = sum(grade)
    informations['média'] = sumGrade/len(grade)
    if situation:
        if informations['média'] >= 7:
            informations['situação'] = 'BOA'
        elif 7 > informations['média'] >= 4:
            informations['situação'] = 'RASOÁVEL'
        else:
            informations['situação'] = 'RUIM'
    return informations


values = grades(9, 8, 5, 5, situation=True)
print(values)
