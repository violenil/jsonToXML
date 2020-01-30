import json

f = open("movie_json.json", 'r')
content = json.load(f)

with open('movieData.xml', 'w') as output:
    for m in content:
        output.write("<movie>\n")
        output.write("\t<title>" + m["Movie_name"] + "</title>\n")
        output.write("\t<actors>\n")
        for actor in m["Characters"]:
            output.write("\t\t<actor>" + actor + "</actor>\n")
        output.write("\t</actors>\n")

output.close()
