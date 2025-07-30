level = int(input()) # Don't change this line
has_training = input() == "True" # Don't change this line
level_message = "None" # Don't change this line

# Write your code below
if level <= 0:
    level_message = "Invalid level"
elif level > 0 and level <= 5:
    level_message = "Basic weapons only"
elif level > 5 and level <= 10:
    if has_training:
        level_message = "Access to advanced weapons granted"
    else:
        level_message = "Need weapon training first"
else:
    level_message = "Access to all weapons granted"


# Don't change below this line
print(level_message)