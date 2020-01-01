import random


def playerPageRank(listOfPairs):
    node_to_index = {}
    nodes = []
    for link in listOfPairs:
        from_node = link[0]
        to_node = link[1]
        if from_node not in nodes:
            nodes.append(from_node)
            node_to_index[from_node] = len(nodes) - 1
        if to_node not in nodes:
            nodes.append(to_node)
            node_to_index[to_node] = len(nodes) - 1
    out_edges = {i: [] for i in range(len(nodes))}
    for link in listOfPairs:
        from_node = link[0]
        to_node = link[1]
        out_edges[node_to_index[from_node]].append(to_node)

    percentage_jump = 85
    num_iterations = 200000

    count_arr1 = [0] * int(num_iterations / 2)
    count_arr2 = [0] * int(num_iterations / 2)

    current_page = random.randrange(0, len(nodes))
    print(f'starting node is {nodes[current_page]}')

    for i in range(num_iterations):
        rand = random.randrange(0, 100)
        if rand < percentage_jump:
            if not out_edges[current_page]:
                current_page = random.randrange(0, len(nodes))
            else:
                current_page = node_to_index[random.choice(out_edges[current_page])]
        else:
            current_page = random.randrange(0, len(nodes))
        print(f'p({i}): current page is {nodes[current_page]}')
        if i < num_iterations / 2:
            count_arr1[current_page] += 1
        else:
            count_arr2[current_page] += 1

    page_rank = {}
    count_arr1 = [count_arr1[i] / len(count_arr1) for i in range(len(count_arr1))]
    count_arr2 = [count_arr2[i] / len(count_arr2) for i in range(len(count_arr2))]
    for i in range(len(nodes)):
        page_rank[nodes[i]] = [count_arr1[i], count_arr2[i]]

    return page_rank
