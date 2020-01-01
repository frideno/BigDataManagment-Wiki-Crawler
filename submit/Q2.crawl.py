import requests
from lxml import html
import heapq
from time import sleep


def crawl(url, xpaths):
    """
    :param url: a tennis player url to start crawling from.
    :param xpath: xpath queries that used to crawl between two different tennis players pages.
    :rtype: a list of lists
    :return: list containing couples of [source url, crawled url]
    """

    prefix_url = 'https://en.wikipedia.org'
    res = []
    # counter dictionary for appearnce:
    urls_counter = {url: 0}

    # keeps max priority queue (negative keys) for the crawling priority - each element in it is:
    # (url appearnce count, url)
    priority_q = []
    heapq.heappush(priority_q, (0, url))

    # visited array to prevent loops
    visited = [' ']

    # keep explore tennis players until there is 100 of them.
    current_url = ' '
    for round in range(100):
        # gets most appeared url, and gets all tennis players related from it, by xpath.
        while current_url in visited:
            current_url = heapq.heappop(priority_q)[1]
        # print("--- getting " + prefix_url + current_url + " ---------")
        page = requests.get(prefix_url + current_url)
        doc = html.fromstring(page.content)
        sleep(3)
        urls = []
        for query in xpaths:
            urls += doc.xpath(query)
        # print(len(urls))

        # add current to visited
        visited.append(current_url)

        # count resutls
        for u in urls:
            if u in urls_counter:
                urls_counter[u] += 1
            else:
                urls_counter[u] = 1

        # add to priority queue by count:
        for u, c in urls_counter.items():
            heapq.heappush(priority_q, (-c, u))
        # add uniqly to result list.
        for u in set(urls):
            res.append([prefix_url + current_url, prefix_url + u])

    return res
