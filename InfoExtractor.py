from bs4 import BeautifulSoup
import requests as req


class InfoExtractor():
    def __init__(self, html, find_first_tag, find_second_tag, remove_opening_tag, remove_closing_tag):
        self.second_layer_result = None
        self.first_layer_result = None
        self.html = html
        self.find_first_tag = find_first_tag
        self.find_second_tag = find_second_tag
        self.remove_opening_tag = remove_opening_tag
        self.remove_closing_tag = remove_closing_tag

    def first_layer(self):
        l1 = BeautifulSoup(self.html, "html.parser")
        self.first_layer_result = l1.find_all(self.find_first_tag)
        # l2 = BeautifulSoup(first_layer_result, "html.parser")
        # second_layer_result = l2.find_all(self.find_second_tag)
        return str(self.first_layer_result)

    def second_layer(self, first_layer_result):
        l2 = BeautifulSoup(first_layer_result, "html.parser")
        self.second_layer_result = l2.find_all(self.find_second_tag)
        return self.second_layer_result

    def do_all_filter(self):
        text = str(self.second_layer(self.first_layer()))
        temp_list = text.replace(self.remove_opening_tag, "\"")
        final_list = temp_list.replace(self.remove_closing_tag, "\"")
        return final_list


class Links():
    def __init__(self, url):
        self.url = url

    def getLinks(self):
        links = list()
        html_page = req.get(self.url)
        soup = BeautifulSoup(html_page.content, "html.parser")
        for link in soup.findAll('a', {'class': 'txt upcase bold sanscond fsz17'}):
            links.append(link.get('href'))
        return links

    def get_tables(self):
        url = "https://www.autoevolution.com/moto/harley-davidson-electra-glide-ultra-classic-1995.html#aeng_harley-davidson-electra-glide-ultra-classic-3000-1337-1"
        html = req.get(url)
        soup = BeautifulSoup(html.content, "html.parser")
#         TODO get table
