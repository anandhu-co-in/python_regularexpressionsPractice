# \w
# Matches alphanumeric characters, that is a-z, A-Z, 0-9, and underscore(_)
# \W
# Matches non-alphanumeric characters, that is except a-z, A-Z, 0-9 and _
# \d
# Matches digits, from 0-9.
# \D
# Matches any non-digits.
# \s
# Matches whitespace characters, which also include the \t, \n, \r, and space characters.
# \S
# Matches non-whitespace characters.
# \A
# Matches the expression to its right at the absolute start of a string whether in single or multi-line mode.
# \Z
# Matches the expression to its left at the absolute end of a string whether in single or multi-line mode.
# \n
# Matches a newline character
# \t
# Matches tab character
# \b
# Matches the word boundary (or empty string) at the start and end of a word.
# \B
# Matches where \b does not, that is, non-word boundary





import re
string="23456782345678"

print("------------------------------")
#Find all matches of 34 as string list
matches=re.findall(r"34",string)
print(matches)

print("------------------------------")
#Find matche in beginning
matches=re.match(r"234",string)
print(matches)

matches=re.match(r"82345678",string)
print(matches)

print("------------------------------")
#Search for match not nessesarily at bgining
matches=re.search(r"82345678",string)
print(matches)

print("------------------------------")
#Get iterrator of matchds
string="abchddndabcjdagkabcd"
matches=re.finditer(r"abc",string)
for match in matches:
    print(match)
    print(match.span(),match.start(),match.end(), match.group())

print("------------------------------")
#Match all charecotrs
string="abchddndabcjdagkabcd."
matches=re.finditer(r".",string)
for match in matches:
    print(match.group())

print("------------------------------")
#Match dot
string="abchddndabcjdagkabcd."
matches=re.finditer(r"\.",string)
for match in matches:
    print(match.group())

print("------------------------------")
#Match at start ^
string="abchddndabcjdagkabcd."
matches=re.finditer(r"^abc",string)
for match in matches:
    print(match.group())

print("------------------------------")
#Match at  $
string="abchddndabcjdagkabcd."
matches=re.finditer(r"abcd.$",string)
for match in matches:
    print(match.group())

print("------------------------------")
#Match digints with \d
string="abchddnd223abcj2d6a20gkab77cd."
matches=re.finditer(r"\d\d",string)
for match in matches:
    print(match.group())

print("------------------------------")
#Match non digits with \D
string="abchddnd223abcj2d6a20gkab77cd."
matches=re.finditer(r"\D\d\D",string)
for match in matches:
    print(match.group())

print("------------------------------")
#Match any alpha numeric \w -- \W is opposite
string="abchddnd223abcj2d6a20gkab77cd."
matches=re.finditer(r"\w\W",string)
for match in matches:
    print(match.group())

print("------------------------------")
#Match at start of each block \b<somechars>
string="abcfg abcwerf abcdabc helloabc"
matches=re.finditer(r"\babc",string)
for match in matches:
    print(match.group())

print("------------------------------")
#Using set [] to match set of charactoers
string="abcfg abcwerf abcdabc helloabc"

matches=re.finditer(r"[ab]",string)
for match in matches:
    print(match.group())

print("------------------------------")
#Using set [] to match range
string="abcfg abcwerf ab2452cdabc hellSBoabc"

matches=re.finditer(r"[A-Za-z0-9]",string)
for match in matches:
    print(match.group())


print("------------------------------")
# Quantifieers - * for zero of more occurence, + for one or more occurence etc
string = "hello_f123"
matches = re.finditer(r"\d*", string)
for match in matches:
    print(match)

print("------------------------------")
matches = re.finditer(r"\d+", string) # If we simply use \d, without * or +, it will look for single character matches
for match in matches:
    print(match)


print("------------------------------")
# ?Optional
string = "hello_123 hello2123"
matches = re.finditer(r"_?\d+", string)  # We are lokking for one or more digits, after an optional underscore
for match in matches:
    print(match)



print("------------------------------")
# {} Specifying exact no of digits
string = "hello_123 hello2122"
matches = re.finditer(r"_?\d{3}", string)  # We are lokking for 3 digits, after an optional underscore -- you can say it as range 3 to 4 by {3,4}
for match in matches:
    print(match)




print("------------------------------")
string="""
Mr. Suresh
22/12/2021
04.06.2021
2/12/2011
2/12/2012
2/12/2013
Mrs. Reshma
"""

matches = re.finditer(r"(Mr|Mrs)\.\s\w+", string)
for match in matches:
    print(match)

print("------------------------------")
matches = re.finditer(r"\d{1,2}/\d{2}/\d\d\d\d", string)
for match in matches:
    print(match)

print("------------------------------")
matches = re.finditer(r"\d{1,2}/\d{2}/\d\d1[1-3]", string)
for match in matches:
    print(match)


emails="""
email@example.com
firstname.lastname@example.com
email@subdomain.example.com
firstname+lastname@example.com
email@123.123.123.123
email@[123.123.123.123]
"email"@example.com
1234567890@example.in
"""

print("----------------------------------------")
matches = re.finditer(r"[a-zA-Z0-9-]+@[a-zA-Z]+\.(com|in)", emails)
for match in matches:
    print(match.group(0))
    print(match.group(1))

print("----------------------------------------")
#Split method
test_string="123abc23456abcIUG"
print(re.split("abc",test_string)) # o/p ['123', '23456', 'IUG']

print("----------------------------------------")
#sub method to replace patterns
test_string="123abc23456abcIUG"
print(re.sub("abc","--XXXX--",test_string)) #123--XXXX--23456--XXXX--IUG

print("------------------------------")
#Using flags, for example, using ignore case flag to match regardless of case
string="abc hello world World wOr7Ld"
matches = re.finditer(r"woR(\d*)ld", string,re.IGNORECASE)
for match in matches:
    print(match)
    print(match.group(1))


#Check if match
print("------------------------------")

if re.match(r"abc", 'hello1_@153'):
    print("MATCH")
else:
    print("NO MATCH")

print("------------------------------")

if re.match(r"[\w]*_@1", 'hello_@153'):
    print("MATCH")
else:
    print("NO MATCH")

print("------------------------------")
#Match at start ^
string="b223.a"
matches=re.finditer(r"^[^a3]+2",string) # i think ^ inside the set, to match all not from the set, outside, it says in begginging
for match in matches:
    print(match.group())