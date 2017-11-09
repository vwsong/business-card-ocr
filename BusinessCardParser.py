from ContactInfo import ContactInfo
import re

"""
Parses a person's business card to return relevant details (name, email, phone).
Uses regexes to match phone numbers and emails, and calculates which of the
possible lines are most likely to be names.

@param document: An input string which contains the business card OCR contents.
@return A ContactInfo object initialized with the correct name, phone, and email.
"""
def getContactInfo(document):
    possibleNames = []
    name = ""
    phone = ""
    email = ""

    lines = document.split("\n")

    # Iterate through all lines in business card
    for line in lines:
        lineName = isName(line)
        linePhone = isPhone(line) #ring ring
        lineEmail = isEmail(line)

        if lineName: # If it's a possible name, add it to possibleNames
            possibleNames.append(lineName[0])
        phone = linePhone[0] if linePhone else phone
        email = lineEmail[0] if lineEmail else email

    name = closestName(possibleNames, email)
    return ContactInfo(name, phone, email)

"""
Simple regex match to find the email.

@param line: current line to check if there's an email in.
@return An array with an email if there exists one, o.w. empty array.
"""
def isEmail(line):
    output = []
    matches = re.search("\S+@\S+\.\S+$", line)
    if matches:
        output.append(matches.group(0))
    return output

"""
Simple regex match to find a phone number, checks if it's a fax or not as well.

@param line: current line to check if there's a phone number in.
@return An array with a phone number if there exists one, o.w. empty array.
"""
def isPhone(line):
    output = []
    matches = re.search("(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]*\d{3}[\s.-]\d{4}", line) #Regex from StackOverflow
    if matches and "fax" not in line.lower():
        output.append(matches.group(0))
    return output

"""
Simple regex match to check if the line contains a name.

@param line: current line to check if there's a name in.
@return An array with a name if there exists one, o.w. empty array.
"""
def isName(line):
    output = []
    matches = re.search("^(\w+ \w+)$", line)
    if matches:
        output.append(matches.group(0))
    return output

"""
Finds the possible name with the highest LCS - that's the line with the closest
name.

@param possibleNames: list of possible names
@param email: email address which names are compared to
@return name that has the highest LCS.
"""
def closestName(possibleNames, email):
    name = ""
    emailName = email.split("@")[0]
    hiscore = 0
    for possibleName in possibleNames:
        lcsScore = lcs(possibleName, emailName)
        if lcsScore > hiscore:
            name = possibleName
            hiscore = lcsScore

    return name

"""
Common DP problem, usually used as one of the factors in determining how similar strings are.
I think edit distance _might_ be better, but I'm not as familiar with that problem
as I am with this one for now, and I think the accuracy difference b/t the two are
close to negligible.

@param X: The first string you want to compare
@param Y: The second string you want to compare
@return the length of the longest common subsequence.
"""

#Credits to GeeksForGeeks: http://www.geeksforgeeks.org/longest-common-subsequence/
def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in xrange(m+1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
