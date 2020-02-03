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
        output.write("\t<director>" + m["Director"] + "</director>\n")
        for r in m["Release_dates"]:
            output.write("\t<release>" + r + "</release>\n")
        if type(m["Plot"]) == str:
            output.write("\t<plot>\n" + m["Plot"] + "\n\t</plot>\n")
        output.write("</movie>\n")

output.close()
