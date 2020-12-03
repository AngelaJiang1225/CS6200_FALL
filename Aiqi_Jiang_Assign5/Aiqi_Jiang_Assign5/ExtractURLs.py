import re
from bs4 import BeautifulSoup

# html files of source page for each query
INFO_NEED_1_GOOGLE = "info_need_1_google.html"
INFO_NEED_1_BING = "info_need_1_bing.html"
INFO_NEED_2_GOOGLE = "info_need_2_google.html"
INFO_NEED_2_BING = "info_need_2_bing.html"
INFO_NEED_3_GOOGLE = "info_need_3_google.html"
INFO_NEED_3_BING = "info_need_3_bing.html"

def main():
    # dictionary to store each information need with its files accordingly.
    html_dic = {"info_need_1_urls": [INFO_NEED_1_GOOGLE, INFO_NEED_1_BING],
                "info_need_2_urls": [INFO_NEED_2_GOOGLE, INFO_NEED_2_BING],
                "info_need_3_urls": [INFO_NEED_3_GOOGLE, INFO_NEED_3_BING]}
    for dic in html_dic.keys():
        # extract urls from google
        f = open(html_dic[dic][0], 'r')
        soup = BeautifulSoup(f, "lxml")
        pat = "<h1 class=.*Search Results</h1>"
        gr = re.split(pat, str(soup))
        fw = open(dic, "w+")
        pat = 'a href=".*"'
        links = re.findall(pat, gr[1])
        pat = 'a href="|"'
        pat2 = '[https:|http:].*'
        idx = 0
        fw.write("urls from google:\n")
        for l in links:
            if idx == 15:
                break
            ls = re.split(pat, l)
            if re.match(pat2, ls[1]):
                idx += 1
                fw.write(str(idx) + ". " + ls[1] + "\n")

        f.close()

        # extract urls from bing
        f = open(html_dic[dic][1], 'r')
        soup = BeautifulSoup(f, "lxml")
        pat = '<ol id="b_results">'
        gr = re.split(pat, str(soup))
        pat = 'li class="b_algo".*href="https?:.*"'
        links = re.findall(pat, gr[1])
        print(str(links))
        pat = 'li class="b_algo".*href="|"'
        fw.write("urls from bing:\n")
        idx = 0
        for l in links:
            print("l in link is: {}".format(l))
            if idx == 15:
                break
            ls = re.split(pat, l)
            idx += 1
            fw.write(str(idx) + ". " + ls[1] + "\n")
        fw.close()
        f.close()

main()

