import sys
import os
import re

# import urllib.request

stat_file = "stats.txt"
urls_file = "URLsCrawled.txt"

domain = "https://en.wikipedia.org"
to_find_url_rule = '<a href="/wiki/.*?"'

max_depth = 5
page_size = 0
min_size = sys.maxsize
max_size = 0

def a1_crawler(seedUrl, num_pages):
    """
    crawl urls starting from seedUrl.
    input parameters: seedUrl,
    :param seedUrl: the starting url
    :param num_pages: max number of pages to crawl out
    """
    to_crawl_pages = []
    # store pages that have been crawled
    visited = set()
    # initiate statistics info into array stat
    stat = [max_size, min_size, 0, 1]
    to_crawl_pages.append(seedUrl)
    depth = 0

    # crawl out urls and store them into url file line by line
    file = open(urls_file, "w+")
    while to_crawl_pages and len(visited) < num_pages:
        size = len(to_crawl_pages)
        for i in range(size):
            frontier = to_crawl_pages.pop(0)
            crawl_links(frontier, to_crawl_pages, visited, file, stat)
            if len(visited) > num_pages:
                break
        depth = depth + 1
        if depth > max_depth:
            break
    file.close()

    # store statistics info into file
    write_statics(stat, num_pages, stat)
    return

def crawl_links(link, page_to_be_crawled, visited, file, stats):
    """
    crawl wiki links
    :param link: wiki url found
    :param page_to_be_crawled: page to be crawled
    :param visited: store pages that have been visited
    :param file: opened file
    :param stats: statistics info array
    """
    # get contents array of links
    path = os.getcwd() + "/crawled_files/"
    file_name = os.path.join(path, str(stats[3]) + ".txt");
    urllib.request.urlretrieve(link, file_name)
    response = urllib.request.urlopen(link).read()
    size = sys.getsizeof(response)

    stats[0] = max(stats[1], size)
    stats[1] = min(stats[0], size)
    stats[2] = stats[2] + size
    stats[3] = stats[3] + 1
    file.write(link + "\n")
    contents = response.decode('utf-8')
    # print("end end!")

    urls = re.findall(to_find_url_rule, contents)
    for url in urls:
        url = domain + url[9:-1]
        if url.count(":") <= 1 and "Main_Page" not in url and "Cookie_statement" not in url:
            if url not in visited and url not in page_to_be_crawled:
                page_to_be_crawled.append(url)
    visited.add(link)
    return

def write_statics(stat, num_pages, depth):
    """
    write statistics info into file
    :param stat: statistics array to store statistics info
    :param num_pages: number of pages that have been crawled
    :param depth: the depth reached
    """
    file = open(stat_file, "w+")
    file.write("Maximum size: " + str(stat[0]) + " bytes\n")
    file.write("Minimum size: " + str(stat[1]) + " bytes\n")
    file.write("Average size: " + str(stat[2] / num_pages) + " bytes\n")
    file.write("Maximum depth reach: " + str(depth))
    file.close()
    return
