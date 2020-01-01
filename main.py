import imp
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

if __name__ == "__main__":

	# import moduls q2,q3.
	q2 = imp.load_source('Q2.crawl', 'Q2.crawl.py')
	q3 = imp.load_source('Q3.playerPageRank', 'Q3.playerPageRank.py')
	# get xpath from file.
	xpaths = getXPaths()
	start_url = "/wiki/Andy_Ram"
	res2 = q2.crawl(start_url, xpaths)
	print('\n'.join([':     '.join(x) for x in res]))
	res3 = q3.playerPageRank(res2)
	print(res3)

