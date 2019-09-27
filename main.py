from bs4 import BeautifulSoup
import InfoExtractor
import requests as req

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
# o = InfoExtractor.Links()
# filename = 0
# for models in links:
#     f = 0
#     filename = filename + 1
#     tech_info_links = o.getLinks(models)
#     file = open("model{}.txt".format(filename), "w+")
#     for j in tech_info_links:
#         table = o.get_tables(j)
#         f = f + 1
#         print(f, table, "\n")
#         file.write("{} {} \n".format(f, table))
#     file.close()
#     f = 0


# # <em class ="nowrap col-black faded" itemprop="vehicleModelDate" > 2019 - Present </em>
# for html in links:
#     html_page = req.get(html)
#     soup = BeautifulSoup(html_page.content, "html.parser")
#     page = InfoExtractor.InfoExtractor(soup, '"h1", {class: "padcol2 newstitle innews"}','"em", {class: nowrap col-black faded}','<em class ="nowrap col-black faded" itemprop="vehicleModelDate" >', '</em>')
# print(page.do_all_filter())


#### get description of each tech info page

# o = InfoExtractor.Links()
# filename = 0
# for model in links:
#     f = 0
#     filename = filename + 1
#     tech_info_links = o.getLinks(model)
#     file = open("model{}.txt".format(filename), "w+")
#     for each_tech_link in tech_info_links:
#         html = req.get(each_tech_link)
#         soup = BeautifulSoup(html.content, "html.parser")
#         result = soup.find_all("div", {"class": "mgbot_20", "itemprop": "description"})
#         f = f + 1
#         print(f, result, "\n")
#         file.write("{} {} \n".format(f, result))
#     file.close()
#     f = 0

# test = """[<div class="mgbot_20" itemprop="description"><strong class="intro dispblock">The new Harley Davidson Electra Glide motorcycle is equipped with the Milwaukee-Eight 107 engine.</strong> For 2019, the new electronic cruise control system, rear dampers with manually adjustable emulsion technology, a 49 mm front suspension for the Showa valve and Brembo brakes with optional Reflex Linked and <span class="txtglos" data-url="https://www.autoevolution.com/auto-glossary/a.html#ge-antilock-braking-system" title="ABS - click for definition">ABS</span> features. Harley's frame is a double-height / double-swing arrangement of welded sections of light steel tubes. The steering head adjusts the 26-degree rake with a height of 6.7 cm on a 64-inch wheelbase for tracking.</div>]
# [<div class="mgbot_20" itemprop="description"><strong class="intro dispblock">The MoCo have combined retro cruiser looks with the functionality and comfort of a modern, fully-equipped touring two-wheeler in the embodiment of the 2016 MY Harley Davidson Electra Glide Ultra Classic.</strong> At its heart lies a Twin-Cooled, four stroke, 1690cc, High Output Twin Cam 103 engine paired to a six-speed manual transmission, that reaches its peak torque of 138 Nm at 3750 rpm. <br/>
# <br/>
# Technology-wise, it boasts the latest developed by the House of Milwaukee, such as <span class="txtglos" data-url="https://www.autoevolution.com/auto-glossary/a.html#ge-antilock-braking-system" title="ABS - click for definition">ABS</span> as standard, traction control and whatnot, plus a full color touch screen display, front speakers, a Boom! box radio, the H-d smart security system and air-adjustable suspension.</div>]
# [<div class="mgbot_20" itemprop="description"><strong class="intro dispblock">Designed for US customers with smaller inseams, but who still want a strong foothold on the ground when stopped, the MoCo has launched the 2015 MY Harley Davidson Electra Glide Ultra Classic Low.</strong> The American engineers have lowered the suspension, thus making the seat height and the ground clearance 1.7"/0.7" lower than the base Electra Glide Ultra Classic.<br/>
# <br/>
# In every other aspect, it is identical to the base model. It features the dependable High Output Twin Cam 103 engine mated to a six-speed manual transmission, and state-of-the-art technologies such as air-adjustable suspension, Reflex-linked Brembo brakes plus the comfortable, heated two-up seat with lumbar support and pillion armrests.</div>]
# """
# print(BeautifulSoup(test, "html.parser").prettify())


o = InfoExtractor.Links()
filename = 0
for model in links:
    f = 0
    filename = filename + 1
    tech_info_links = o.getLinks(model)
    file = open("years{}.txt".format(filename), "w+")
    for each_tech_link in tech_info_links:
        html = req.get(each_tech_link)
        soup = BeautifulSoup(html.content, "html.parser")
        result = soup.find_all("em", {"class": "nowrap col-black faded", "itemprop": "vehicleModelDate"})
        f = f + 1
        print(f, result, "\n")
        file.write("{} {} \n".format(f, result))
    file.close()
    f = 0
