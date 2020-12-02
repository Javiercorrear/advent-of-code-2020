from entries import entries

def getRightInputs():
    rightPassCount = 0
    for passInput in entries:
        policy, password = passInput.split(': ')
        positionsToVerify, requiredChar = policy.split(' ')
        firstPosition, secondPosition = positionsToVerify.split('-')
        existsInFirstPosition = password[int(firstPosition)-1] == requiredChar
        existsInSecondPosition = password[int(secondPosition)-1] == requiredChar
        if ( existsInFirstPosition or existsInSecondPosition ) and not(existsInFirstPosition and existsInSecondPosition):
            rightPassCount += 1
    return rightPassCount


print(getRightInputs())
