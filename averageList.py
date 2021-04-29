

#Returns None if there's an error.
def calculateAverage(inputList):
    sum = 0.0
    for i in inputList:
        try:
            value = float(i)
            sum += value
        except ValueError:
            return None
        except TypeError:
            return None
    try:
        average = float(sum) / len(inputList)
        return average
    except ZeroDivisionError:
        return None