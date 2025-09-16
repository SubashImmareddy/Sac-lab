#Create a tuple
colors = ("red", "green", "blue")
print("Tuple:", colors)

#Access elements
print("First color:", colors[0])
print("Last color:", colors[-1])

#Tuple with one item (note the comma!)
single = ("only_one",)
print("Single item tuple:", single)

#Tuple unpacking
r, g, b = colors
print("Unpacked:", r, g, b)

#Length of tuple
print("Length:", len(colors))

#Check if item exists
if "green" in colors:
    print("Green is in tuple")

#Loop through tuple
for color in colors:
    print(color)

#Concatenate tuples (creates a new tuple)
more_colors = ("yellow", "purple")
combined = colors + more_colors
print("Combined tuple:", combined)

#Repeat tuples
repeat = colors * 2
print("Repeated tuple:", repeat)

#Tuple methods (count and index)
print("Count 'red':", colors.count("red"))
print("Index of 'blue':", colors.index("blue"))
