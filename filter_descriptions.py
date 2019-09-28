file = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18,
        19, 20, 21, 22, 23, 24, 25, 26,
        27, 28, 29, 30, 31, 32, 33, 34,
        35, 36, 37, 38]

r = '<div class="mgbot_20" itemprop="description">'
r2 = '<strong class="intro dispblock">'
r3 = "</strong>"  # replace with "\n"
r4 = "</div>"
r5 = '''<span class="txtglos" data-url="https://www.autoevolution.com/auto-glossary/a.html#ge-antilock-braking-system" title="ABS - click for definition">ABS</span>'''

for i in file:
    with open('descriptions/model{}.txt'.format(i), 'r') as reader:
        text = reader.read()
        l1 = text.replace(r, "")
        l2 = l1.replace(r2, "")
        l3 = l2.replace(r3, "")
        l4 = l3.replace(r4, "")
        l5 = l4.replace(r4, "ABS")
        l6 = l5.replace("<br/>", "")
        l7 = l6.replace("[", "\"")
        l8 = l7.replace("]", "\",")
    new_file = open("final/descriptions/descriptions{}.txt".format(i), "w+")
    new_file.write("{}".format(l8))
    new_file.close()
