import re
from bs4 import BeautifulSoup
INFO_NEED_1_GOOGLE = "info_need_1_google.html"
INFO_NEED_1_URL = "info_need_1_urls"

def main():
    f = open(INFO_NEED_1_GOOGLE, 'r')
    soup = BeautifulSoup(f, "lxml")
    # print(soup.prettify())
    # print(soup.title.text)
    pat = "<h1 class=.*Search Results</h1>"
    # print(str(soup))
    gr = re.split(pat, str(soup))
    # print("text: {}".format(gr[1]))
    fw = open(INFO_NEED_1_URL, "w+")
    pat = 'a href=".*"'
    # ='.*'
    links = re.findall(pat, gr[1])
    #print("hi: {}".format(links[0]))
    pat = 'a href="|"'
    pat2 = '[https:|http:].*'
    idx = 0
    for l in links:
        if idx == 15:
            break
        ls = re.split(pat, l)
        if re.match(pat2, ls[1]):
            fw.write(ls[1] + "\n")
            idx += 1
            #print("ls is: {}".format(ls[1]))
        # print("hi: {}".format(ls[0]))
    # print("group: {}".format(m.group(0)))
    #soup = BeautifulSoup(gr[1], "lxml")
    # for link in soup.find_all("a"):
    #     print(str(link.get("href")))
        # if link.get("href") in gr[0]:
        #     continue
        # print("href: {}".format(link.get("href")))
        # fw.write(soup.get(link.get("href")))
    fw.close()
    f.close()
    # for h in soup.find_all("h1"):
    #     if "Search Results".__eq__(h.text):
    #         print("Inner Text: {}".format(h.text))
    #         print("Title: {}".format(h.get("title")))
    #         print("href: {}".format(h.get("href")))
main()

