import re
text = "Hello Viewers, How are you? "
pattern =  "You | about"
wordmatch  = re.search(pattern, text)
print(wordmatch)

#Special characters with specific meanings

# 1. '.' - Any character except newline.

# 2. '^' - Start of string

# 3. '$' - End of string

# 4. '*' - O or more repetions.

# 5. '+' - 1 or more repetitions

# 6. '?' - O or 1 repetition.

# 7. '[]' - Set of characters

# 8. '\' - Escape characte