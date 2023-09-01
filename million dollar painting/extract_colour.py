import colorgram
color_list = []
colors = colorgram.extract("million.jpg",12)
print(color_list)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colour = (r, g, b)
    color_list.append(colour)

print(color_list)