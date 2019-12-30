import requests
from lxml import html
import heapq


def getXPaths():

    """
    question 1. xpath queriesn.
    this gives xpaths from file "xpathsQueries.txt"
    """

    xpaths = []
    with open("xpathQueries.txt") as xpaths_file:
        for line in xpaths_file:
            xpaths.append(line[:-1])

    return xpaths

def crawl(url, xpaths):
    """
    :param url: a tennis player url to start crawling from.
    :param xpath: xpath queries that used to crawl between two different tennis players pages.
    :rtype: a list of lists
    :return: list containing couples of [source url, crawled url]
    """

    res = []
    # counter dictionary for appearnce:
    urls_counter = {url: 0}

    # keeps max priority queue (negative keys) for the crawling priority - each element in it is:
    # (url appearnce count, url)
    priority_q = []
    heapq.heappush(priority_q, (0, url))

    # visited array to prevent loops
    visited = []

    # keep explore tennis players until there is 100 of them.
    while len(urls_counter) < 1000:
        # gets most appeared url, and gets all tennis players related from it, by xpath.
        current_url = heapq.heappop(priority_q)[1]
        print("--- getting " + current_url + " ---------")
        page = requests.get('https://en.wikipedia.org' +current_url)
        doc = html.fromstring(page.content)
        # sleep(3)
        urls = []
        for query in xpaths:
            urls += doc.xpath(query)
        print(len(urls))

        # add current to visited
        visited.append(current_url)

        # count resutls
        for u in urls:
            if u in urls_counter: urls_counter[u] += 1
            else: urls_counter[u] = 1

        # add to priority queue by count:
        for u, c in urls_counter.items():
            if u not in visited:
                heapq.heappush(priority_q, (-c, u))
        # add uniqly to result list.
        for u in set(urls):
            res.append([current_url, u])


    return res


if __name__ == "__main__":
    xpaths = getXPaths()
    andyurl = "/wiki/Andy_Ram"
    res = crawl(andyurl, xpaths)
    print('\n'.join([':     '.join(x) for x in res]))
    print(len(res))