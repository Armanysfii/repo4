file = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18,
        19, 20, 21, 22, 23, 24, 25, 26,
        27, 28, 29, 30, 31, 32, 33, 34,
        35, 36, 37, 38]

for i in file:
    with open('years/years{}.txt'.format(i), 'r') as reader:
        text = reader.read()
        l1 = text.replace('[<em class="nowrap col-black faded" itemprop="vehicleModelDate">', "\"")
        l2 = l1.replace("</em>]", "\",")
    newfile = open("final/years/years{}.txt".format(i), "w+")
    newfile.write("{}".format(l2))
    newfile.close()
