import re

m = re.search(r'([\w.]+)@([\w.]+)', 'blah nick.p@gmail.com yatt @')

print(m.group())
print(m.group(1))


# Using parentheses around a pattern “captures” the text matched by that pattern and sends it as an argument to the view function.