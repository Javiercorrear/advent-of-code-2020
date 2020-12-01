from entries import entries

def getInput():
    REF_NUMBER = 2020
    for entry in entries:
        testNumber = REF_NUMBER - entry
        if testNumber in entries:
            return entry * testNumber

print( getInput() )