from entries import entries

def getInput():
    REF_NUMBER = 2020
    for entry in entries:
        for entry2 in entries:
            for entry3 in entries:
                if entry + entry2 + entry3 == REF_NUMBER:
                    return entry * entry2 * entry3

print( getInput() )