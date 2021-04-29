

#Returns -2 if invalid inputs, -1 if negative inputs, returns the volume otherwise.
def volume(w,l,h):
    try:
        widthInt = float(w)
        heightInt = float(h)
        lengthInt = float(l)
        if(widthInt < 0 or heightInt < 0 or lengthInt < 0):
            return -2
        return widthInt * heightInt * lengthInt
    except ValueError:
        return -1
    except TypeError:
        return -1
