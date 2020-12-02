from entries import entries

def getRightInputs():
    rightPassCount = 0
    for passInput in entries:
        policy, password = passInput.split(':')
        charRange, requiredChar = policy.split(' ')
        minChar, maxChar = charRange.split('-')
        reqCharCount = 0
        for passChar in password:
            if passChar == requiredChar:
                reqCharCount += 1
        if reqCharCount >= int(minChar) and reqCharCount <= int(maxChar):
            rightPassCount += 1
    return rightPassCount


print(getRightInputs())