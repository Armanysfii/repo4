import InfoExtractor

links = [
    "https://www.autoevolution.com/moto/harley-davidson/electra-glide/",
    "https://www.autoevolution.com/moto/harley-davidson/dyna/",
    "https://www.autoevolution.com/moto/harley-davidson/trike/",
    "https://www.autoevolution.com/moto/harley-davidson/freewheeler/",
    "https://www.autoevolution.com/moto/harley-davidson/street/",
    "https://www.autoevolution.com/moto/harley-davidson/ultra/",
    "https://www.autoevolution.com/moto/harley-davidson/sportster-1/",
    "https://www.autoevolution.com/moto/harley-davidson/street-glide/",
    "https://www.autoevolution.com/moto/harley-davidson/cvo/",
    "https://www.autoevolution.com/moto/harley-davidson/road-glide/",
    "https://www.autoevolution.com/moto/harley-davidson/road-king/",
    "https://www.autoevolution.com/moto/harley-davidson/softail/",
    "https://www.autoevolution.com/moto/harley-davidson/firefighter/",
    "https://www.autoevolution.com/moto/harley-davidson/peace-officer/",
    "https://www.autoevolution.com/moto/harley-davidson/police/",
    "https://www.autoevolution.com/moto/harley-davidson/sport-glide/",
    "https://www.autoevolution.com/moto/harley-davidson/forty-eight/",
    "https://www.autoevolution.com/moto/harley-davidson/iron/",
    "https://www.autoevolution.com/moto/harley-davidson/fxdr/",
    "https://www.autoevolution.com/moto/harley-davidson/superlow/",
    "https://www.autoevolution.com/moto/harley-davidson/cle/",
    "https://www.autoevolution.com/moto/harley-davidson/fire-rescue/",
    "https://www.autoevolution.com/moto/harley-davidson/fl/",
    "https://www.autoevolution.com/moto/harley-davidson/hummer/",
    "https://www.autoevolution.com/moto/harley-davidson/nova/",
    "https://www.autoevolution.com/moto/harley-davidson/s-3/",
    "https://www.autoevolution.com/moto/harley-davidson/scat/",
    "https://www.autoevolution.com/moto/harley-davidson/shrine/",
    "https://www.autoevolution.com/moto/harley-davidson/sportster-streamliner/",
    "https://www.autoevolution.com/moto/harley-davidson/sprint-2/",
    "https://www.autoevolution.com/moto/harley-davidson/sst-1/",
    "https://www.autoevolution.com/moto/harley-davidson/sx-1/",
    "https://www.autoevolution.com/moto/harley-davidson/topper/",
    "https://www.autoevolution.com/moto/harley-davidson/tour-glide/",
    "https://www.autoevolution.com/moto/harley-davidson/vr-1000/",
    "https://www.autoevolution.com/moto/harley-davidson/vrsc/",
    "https://www.autoevolution.com/moto/harley-davidson/xlcr/",
    "https://www.autoevolution.com/moto/harley-davidson/xr-1/"]

### GRAB TECH INFO
o = InfoExtractor.Links()
filename = 0
for models in links:
    f = 0
    filename = filename + 1
    tech_info_links = o.getLinks(models)
    file = open("model{}.txt".format(filename), "w+")
    for j in tech_info_links:
        table = o.get_tables(j)
        f = f + 1
        print(f, table, "\n")
        file.write("{} {} \n".format(f, table))
    file.close()
    f = 0


