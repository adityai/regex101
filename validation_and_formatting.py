import re

# Email
# Simple
subject = "admin@local host.com"
matchobj = re.search("^\S+@\S+$", subject)
if matchobj:
    print("Valid email: " + matchobj.group(0))
else:
    print("Invalid email: " + subject)

# Simple with restrictions on characters
subject = "admin@lo^calhost.com"
matchobj = re.search("^[A-Z0-9+_.-]+@[A-Z0-9.-]+$", subject, re.IGNORECASE)
if matchobj:
    print("Valid email: " + matchobj.group(0))
else:
    print("Invalid email: " + subject)

# Simple, with all valid local part characters
subject = "admin@loca*lhost.com"
matchobj = re.search("^[A-Z0-9_!#$%&'*+/=?`{|}~^.-]+@[A-Z0-9.-]+$", subject, re.IGNORECASE)
if matchobj:
    print("Valid email: " + matchobj.group(0))
else:
    print("Invalid email: " + subject)

# No leading, trailing, or consecutive dots
subject = "..admin@localhost.com"
matchobj = re.search("^[A-Z0-9_!#$%&'*+/=?`{|}~^-]+(?:\.[A-Z0-9_!#$%&'*+/=?`{|}~^-]+)*@[A-Z0-9-]+(?:\.[A-Z0-9-]+)*$", subject, re.IGNORECASE)
if matchobj:
    print("Valid email: " + matchobj.group(0))
else:
    print("Invalid email: " + subject)

# Top-level domain has two to six letters
subject = "admin@localhost.c"
matchobj = re.search("^[\w!#$%&'*+/=?`{|}~^-]+(?:\.[\w!#$%&'*+/=?`{|}~^-]+)*@(?:[A-Z0-9-]+\.)+[A-Z]{2,6}$", subject, re.IGNORECASE)
if matchobj:
    print("Valid email: " + matchobj.group(0))
else:
    print("Invalid email: " + subject)

# Validate and Format North American Phone Numbers
# determine whether a user entered a North American phone number, including the local area code, in a common format. These formats include 1234567890, 123-456-7890, 123.456.7890, 123 456 7890, (123) 456 7890, and all related combinations. If the phone number is valid, convert it to your standard format, (123) 456-7890
# Regex
subject = "1234512"
matchobj = re.search("^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$", subject, re.IGNORECASE)
if matchobj:
    print("Valid US phone #: " + matchobj.group(0))
else:
    print("Invalid US phone: " + subject)

subject = "1234567890"
matchobj = re.search("^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$", subject, re.IGNORECASE)
if matchobj:
    print("Valid US phone #: " + matchobj.group(0))
else:
    print("Invalid US phone: " + subject)

# Replace
# (\1) \2-\3
result = re.sub(r"^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$", r"(\1) \2-\3", "1234567890")
print(result)

# Eliminate invalid phone numbers
subject = "1234567890"
matchobj = re.search(r"^\(?([2-9][0-8][0-9])\)?[-. ]?([2-9][0-9]{2})[-. ]?([0-9]{4})$", subject)
if matchobj:
    print("Valid US phone #: " + matchobj.group(0))
else:
    print("Invalid US phone #: " + subject)

subject = "2123456789"
matchobj = re.search(r"^\(?([2-9][0-8][0-9])\)?[-. ]?([2-9][0-9]{2})[-. ]?([0-9]{4})$", subject)
if matchobj:
    print("Valid US phone #: " + matchobj.group(0))
else:
    print("Invalid US phone #: " + subject)

#Page# 268: Find phone numbers in documents
# Replace ^ and $ with \b boundary
subject = "2123456789"
matchobj = re.search(r"\(?\b([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})\b", subject)
if matchobj:
    print("Valid US phone #: " + matchobj.group(0))
else:
    print("Invalid US phone #: " + subject)

#Page 270 - 4.3 Validate International Phone Numbers

# Validate Traditional Date Formats
# Validate dates in the traditional formats mm/dd/yy, mm/dd/yyyy, dd/mm/yy, and dd/mm/yyyy. Use a simple regex that simply checks whether the input looks like a date, without trying to weed out things such as February 31st
# Solution 1: Match any of these date formats, allowing leading zeros to be omitted:
subject = "09 01 2000"
matchobj = re.search(r"^[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}$", subject)
if matchobj:
    print("Valid date: " + matchobj.group(0))
else:
    print("No date: " + subject)

subject = "09/01/2000"
matchobj = re.search(r"^[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}$", subject)
if matchobj:
    print("Valid date: " + matchobj.group(0))
else:
    print("No date: " + subject)

# Solution 2: Match any of these date formats, requiring leading zeros:
subject = "9/01/2000"
matchobj = re.search(r"^[0-3][0-9]/[0-3][0-9]/(?:[0-9][0-9])?[0-9][0-9]$", subject)
if matchobj:
    print("Valid date: " + matchobj.group(0))
else:
    print("No date: " + subject)

