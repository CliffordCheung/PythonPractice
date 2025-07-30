temperature = int(input()) # Don't change this line
weather = "unset"
# Type your code below
if temperature < 0:
    weather = "Freezing"
elif temperature >= 0 and temperature <= 15:
    weather = "Cold"
elif temperature > 15 and temperature <=25:
    weather = "Mild"
else:
    weather = "Hot"


# Don't change the line below
print(f"weather = {weather}")