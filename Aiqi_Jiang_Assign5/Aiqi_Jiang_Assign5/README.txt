Steps to run the program under directory of Aiqi_Jiang_Assign5:
1. python ExtractURLs.py
(This is to extract all urls from html files I parsed from source pages of each query,
there are 3 output files: info_need_1_urls, info_need_2_urls and info_need_3_urls)
2. I marked relevance of each results and store them into 3 files:
    info_need_1_marked_relevance, info_need_2_marked_relevance and info_need_3_urls_marked_relevance.
3. python ComputeMetrics.py
(This is to calculate precisions as required in a5, output file is:
precision_info_file to store calculation results)
* Sorry QueryMetrics.txt seems to not support table displaying, please refer to QueryMetrics.docx
or QueryMetrics.pdf for reading, thanks so much!

Discussion:
1. A short note about other aspects of each search engine, excluding the relevance of the results. What
did you like or dislike about the presentation of the results, other features on the page etc.
About the presentation of the results, I want to say that Bing have more ads and they are more likely to be
located at top although I excluded them for assignment, especially when quering for info_need_2. I don't like so.
I like what Google does for ads, it has fewer than Bing and tends to put ads at the end of pages.
Besides, I find that for different queries, the performance and features of Google and Bing varies too.
For info_need_1 about a musical, Bing tend to have more extensice searching range including UK than Google
(I set both search engines' region to be United States).
For info_need_2 and info_need_3 about wine and lens, it seems that Bing has more advertisement-style results including
ecommerce websites, personal blogs of some wine tasters and training courses for tasting wines, which is not
ideal for my target.

2. A one or two sentence answer to each of these questions:
What was the most difficult part of this assignment?
    I think the most difficult part of the assignment is extracting out correct urls for query results and I tested
different strategies to resolve it, using both libraires of re and BeautifulSoup.
    How to justify the relevance of each result cost me much time too. Besides searching keywords,
I need to read title of each paragraph in articles too. Some irrelevant results seems to have
useful title name too, but actually links you other useless places such as advertisements and ecommerce websites, so
I have to be very careful.

What was the easiest part?
    The easiest part is to calculate precision as required. I just need to put all
    relevance info a dictionary and traverse them to do calculations with known equation,
    the results turned out quickly.
3. In doing this assignment, what did you learn about any of the engines that most surprised you?
I am most surprised by Bing. Although there are many advertisements in it, actually I don't need to
worry about extracting out advertisement results. When I check the source page of the pages I find that
Bing exclude urls of these advertisements. So this surprises me and give me much convenience to extract
out correct urls from Bing's web pages in html form.
