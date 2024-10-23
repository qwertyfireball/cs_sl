text = "I am a string"
print(text)

# format strings
fstring = f"The text variable is {text}"
print(fstring)

# Triple quotes
text = """i want smth on mulitiple
lines"""

# "/n" creates a new line
text = "hello\nim bob"
print(text)

# "/t" creates a new tab
text = "this is what\ttab does"
print(text)

# "//" creates a backslahs
text = "this is what backlash does\\"
print(text)

# \ seperates quotes
text = 'double_quote:"'
print(text)

# "\r\n" creates a new line and from character 1
text = "this is what\r\nthis does"
print (text)

# How strings are stored, unicode
# Western Letters = 1 byte
# Middle East = 2 bytes
# Emoji = 4 bytes

pi = "\u03c0"
print (pi)
