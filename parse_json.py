import json

# some JSON:
data = oEmbed('https://youtu.be/dQw4w9WgXcQ', maxwidth=640, maxheight=480)
print(data)
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])