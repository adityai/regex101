# Regular expressions with Python
## Match patterns

### Basic usage

import re
reobj = re.compile(r"""[$"'\n\d/\\]""")

### Options

reobj = re.compile("[$\"'\n\\d/\\\\]", re.VERBOSE | re.IGNORECASE | re.DOTALL | re.MULTILINE)


### Test if a match can be found in the subject string

if reobj.search("test$"):
    print("Successful match")
else:
    print("No match")

##### To use the same regex repeatedly, compile the regex object

if reobj.search("test1$"):
    print("Successful match")
else:
    print("No match")


### Test whether a RegEx matches the subject string entirely

if re.match("\w\d\d\d", "c123"):
    print("Successful match of entire subject string")
else:
    print("No match of entire subject string")


### Retrieve the matched text

matchobj = re.search("\w\w\w\d\d", "12qwe11")
if matchobj:
 result = matchobj.group()
else:
 result = ""
print("Result = " + result)


##### To use the same regex repeatedly, compile the regex object

reobj = re.compile("\d+")
matchobj = reobj.search("You like the number 12 or 15?")
if matchobj:
 result = matchobj.group()
else:
 result = ""
print("Result = " + result)


### Determine the position and length of the match

matchobj = re.search(r"\d+", "QQWQWE123QAS1231ASA")
if matchobj:
 matchstart = matchobj.start()
 matchlength = matchobj.end() - matchstart
print("Match position = " + str(matchstart))
print("Match length = " + str(matchlength))


##### To use the same regex repeatedly, compile the regex object

reobj = re.compile(r"\d+")
matchobj = reobj.search("QQWQWE123QAS1231ASA")
if matchobj:
 matchstart = matchobj.start()
 matchlength = matchobj.end() - matchstart
print("Match position = " + str(matchstart))
print("Match length = " + str(matchlength))


### Retrieve part of the matched text

matchobj = re.search("http://([a-z0-9.-]+)", "http://ab1adaa2fef1.com!@")
if matchobj:
 result = matchobj.group(1)
else:
 result = ""
print("Result = " + result)


##### To use the same regex repeatedly, use a compiled object:

reobj = re.compile("http://([a-z0-9.-]+)")
matchobj = reobj.search("http://ab1adaa2fef1.com!@")
if matchobj:
 result = matchobj.group(1)
else:
 result = ""
print("Result = " + result)


### Determine the position and length of the match

matchobj = re.search(r"\d+", "asa31231asda121")
if matchobj:
 matchstart = matchobj.start()
 matchlength = matchobj.end() - matchstart
print ("Match start = " + str(matchstart) + "\nMatch length = " + str(matchlength))


##### To use the same regex repeatedly, use a compiled object:

reobj = re.compile(r"\d+")
matchobj = reobj.search("asa31231asda121")
if matchobj:
 matchstart = matchobj.start()
 matchlength = matchobj.end() - matchstart
print ("Match start = " + str(matchstart) + "\nMatch length = " + str(matchlength))

### Retrieve part of the matched text

matchobj = re.search("http://([a-z0-9.-]+)", "Please visit http://www.regexcookbook.com for more information.")
if matchobj:
 result = matchobj.group(1)
else:
 result = ""
print(result)


##### To use the same regex repeatedly, use a compiled object:

reobj = re.compile("http://([a-z0-9.-]+)")
matchobj = reobj.search("Please visit http://www.regexcookbook.com for more information.")
if matchobj:
 result = matchobj.group(1)
else:
 result = ""
print(result)


### Named capture

matchobj = re.search("http://(?P<domain>[a-z0-9.-]+)", "Please visit http://www.regexcookbook.com for more information.")
if matchobj:
 result = matchobj.group("domain")
else:
 result = ""
print(result)


### Retrieve a List of All Matches
### The lucky numbers are 7, 13, 16, 42, 65, and 99.

result = re.findall(r"\d+", "The lucky numbers are 7, 13, 16, 42, 65, and 99.")
print(result)


##### To use the same regex repeatedly, use a compiled object:
reobj = re.compile(r"\d+")
result = reobj.findall("The lucky numbers are 7, 13, 16, 42, 65, and 99.")
print(result)

### Iterate over all matches

for matchobj in re.finditer(r"\d+", "The lucky numbers are 7, 13, 16, 42, 65, and 99."):
    # Here you can process the match stored in the matchobj variable
    print(matchobj.group(0))


##### To use the same regex repeatedly, use a compiled object:

reobj = re.compile(r"\d+")
for matchobj in reobj.finditer("The lucky numbers are 7, 13, 16, 42, 65, and 99."):
    # Here you can process the match stored in the matchobj variable
    print(matchobj.group(0))


### Validate Matches in Procedural Code
### List only numbers that are multiples of 13

list = []
for matchobj in re.finditer(r"\d+", "The lucky numbers are 7, 13, 16, 42, 65, and 99."):
    if int(matchobj.group()) % 13 == 0:
        list.append(matchobj.group())
print(list)


##### To use the same regex repeatedly, use a compiled object:

list = []
reobj = re.compile(r"\d+")
for matchobj in reobj.finditer("The lucky numbers are 7, 13, 16, 42, 65, and 99."):
    if int(matchobj.group()) % 13 == 0:
        list.append(matchobj.group())
print(list)


### Find a Match Within Another Match
#### Find all numbers marked as bold. If some bold text contains multiple numbers, match all of them separately. For example, when processing the string 1 <b>2</b> 3 4 <b>5 6 7</b>
list = []
innerre = re.compile(r"\d+")
for outermatch in re.finditer("(?s)<b>(.*?)</b>", "1 <b>2</b> 3 4 <b>5 6 7</b>"):
    list.extend(innerre.findall(outermatch.group(1)))
print(list)

### Replace All Matches

result = re.sub("before", "after", "Red before green before blue after yellow.")
print(result)


##### To use the same regex repeatedly, use a compiled object:

reobj = re.compile("before")
result = reobj.sub("after", "Red before green before blue after yellow.")
print(result)


### Replace Matches Reusing Parts of the Match
#### Match pairs of words delimited by an equals sign, and swap those words in the replacement.

result = re.sub(r"(\w+)=(\w+)", r"\2=\1", "ten=10 twenty=20 thirty=30")
print(result)


##### To use the same regex repeatedly, use a compiled object:

reobj = re.compile(r"(\w+)=(\w+)")
result = reobj.sub(r"\2=\1", "ten=10 twenty=20 thirty=30")
print(result)


### Named Capture

result = re.sub(r"(?P<left>\w+)=(?P<right>\w+)", r"\g<right>=\g<left>", "ten=10 twenty=20 thirty=30")
print(result)


# To use the same regex repeatedly, use a compiled object:

reobj = re.compile(r"(?P<left>\w+)=(?P<right>\w+)")
result = reobj.sub(r"\g<right>=\g<left>", "ten=10 twenty=20 thirty=30")
print(result)


#3.16 Replace Matches with Replacements Generated in Code
####1. Replace all numbers in a string with the number multiplied by two
####2. Both code snippets call the function computereplacement. This function needs to be declared before you can pass it to sub().

def computereplacement(matchobj):
    return str(int(matchobj.group()) * 2)

result = re.sub(r"\d+", computereplacement, "I have 2 hands, 2 legs, 1 nose, 2 eyes, 2 ears, 10 fingers and ten toes.")
print(result)

##### To use the same regex repeatedly, use a compiled object:

reobj = re.compile(r"\d+")
result = reobj.sub(computereplacement, "I have 2 hands, 2 legs, 1 nose, 2 eyes, 2 ears, 10 fingers and ten toes.")
print(result)


### Replace All Matches Within the Matches of Another Regex
#### Red <b>before</b> <b>green before</b> blue <b>before</b> yellow <b>after tangerine</b>

innerre = re.compile("before")
def replacewithin(matchobj):
    return innerre.sub("after", matchobj.group())
result = re.sub("<b>.*?</b>", replacewithin, "Red <b>before</b> <b>green before</b> blue <b>before</b> yellow <b>after tangerine</b>")
print(result)


#3.18 Replace All Matches Between the Matches of Another Regex
#### Replace straight double quotes with curly double quotes, but you only want to replace the quotes outside of HTML tags:

##### "text" <span class="middle">"text"</span> "text"


innerre = re.compile('"([^"]*)"')
result = "";
lastindex = 0;
subject = '"text" <span class="middle">"text"</span> "text"'
for outermatch in re.finditer("<[^<>]*>", subject):
 # Search and replace through the text between this match,
 # and the previous one
    textbetween = subject[lastindex:outermatch.start()]
    result += innerre.sub(u"\u201C\\1\u201D", textbetween)
    lastindex = outermatch.end()
 # Append the regex match itself unchanged
    result += outermatch.group()
# Search and replace through the remainder after the last regex match
    textafter = subject[lastindex:]
    result += innerre.sub(u"\u201C\\1\u201D", textafter)
print(result)

### Split a string
#### Split a string with HTML tags in it along the HTML tags.

subject = 'I like <b>bold</b> and <i>italic</i> fonts'
result = re.split("<[^<>]*>", subject)
# To use the same regex repeatedly, use a compiled object:
reobj = re.compile("<[^<>]*>")
result = reobj.split(subject)
print(result)


### Split a String, Keeping the Regex Matches
#### Split a string with HTML tags in it along the HTML tags, and also keep the HTML tags.

subject = 'I like <b>bold</b> and <i>italic</i> fonts'
result = re.split("(<[^<>]*>)", subject)
#To use the same regex repeatedly, use a compiled object:
reobj = re.compile("(<[^<>]*>)")
result = reobj.split(subject)
print(result)


### Search line by line
#### If you have a multiline string, split it into an array of strings first, with each string in the array holding one line of text:

lines = re.split("\r?\n", "Testing 1 search in multiline\n with regex 2")

# Then, iterate over the lines array:
reobj = re.compile("\d+")
for line in lines[:]:
    if reobj.search(line):
        print("The regex matches line")
    else:
        print("The regex does not match line")


