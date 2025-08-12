text = input()
delimiter = input()
# Write your code below
text_new = text.split()
text_final = delimiter.join(text_new)
print(text_final)