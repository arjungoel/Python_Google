import re
#match = re.search(pat, text)
#print(match.group())

def Find(pat, text):
    match = re.search(pat, text)
    if match:
        print(match.group())
    else:
        print('Not found')

Find('oel', 'arjun goel')
Find('.....un', 'arjun goel')
Find(r'c\.l', 'c.lled piiig much better:xyzgs')
Find(r':\w', 'blah:cat blah blah')
Find(r'\d\s\d\s\d', '1 2 3')
Find(r':.+', 'my name: arjun and I am a cloud engineer')
Find(r'[\w.]+@\w+', 'blah nick.p@gmail.com yatta @')
Find(r'[\w.]+@[\w.]+', 'blah nick.p@gmail.com yatta @')
Find(r'\w[\w.]*@[\w.]+', 'blah .nick.p@gmail.com yatta @')






# match does not point to an object that has a group behavior it just matched it points to nothing.
# re.search() goes from L->R and it satisfies as soon as it finds the solution.
# python gives an option to put a raw string 'r' which means do not do any special processing with backslashes('\'). Whatever I type just send it through absolutely raw and uninterpreted.
# It frees us from having to worry about layers of backslash processing.
# \w -> matches a word character (letter or digit or _).
# \d -> matches a digit(0-9)
# ... -> any character i.e. space, colon etc
# \w\w\w -> matches a character so long it looks like a word character (a-zA-Z, 0-9, _) 
# \s -> represents a whitespace character. \s is smart that it knows about space, tab, newline etc.
# Modifiers + and *  -> + means 1 or more and * means 0 or more.
# \w+
# The mnemonic for RE is it finds the leftmost solution the first one and the largest solution.
# \S  --> non-whitespace character