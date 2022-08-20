from pprint import pprint
from collections import deque


graph = {}

graph['me'] = ['Oleg', 'Yurii', 'Vlad']

graph['Oleg'] = ['Lev', 'Vlad Junior']

graph['Lev'] = []
graph['Vlad Junior'] = []

graph['Yurii'] = ['Dima', 'Dmytro']
graph['Dima'] = ['Oleg', 'Petro']
graph['Dmytro'] = []
graph['Petro'] = []

graph['Vlad'] = ['Olga', 'Ivan']
graph['Olga'] = []
graph['Ivan'] = []


pprint(graph)


def is_fan(name):
    return name.startswith('O')


def search_fan():
    search_queue = deque()

    search_queue += graph['me']
    already_searched = []
    counter = 0
    while search_queue:

        person_name = search_queue.popleft()
        # print('Name to search', person_name)
        if person_name not in already_searched:
            print('Name to search', person_name)
            counter += 1
            if is_fan(person_name):
                print(person_name, 'Is a fan!')
                print(counter)
                return True
            else:
                search_queue += graph[person_name]
                already_searched.append(person_name)

    print('Did not found!')
    return False


print('*' * 80)
search_fan()


print('|' * 80)

graph = {}

graph['start'] = {}

graph['start']['B'] = 6
graph['start']['A'] = 2

print(graph['start'].keys())
print(graph['start']['A'])
print(graph['start']['B'])

graph['A'] = {}
graph['A']['finish'] = 5
graph['A']['B'] = 3

graph['B'] = {}
graph['B']['finish'] = 1

graph['finish'] = {}

# Costs of relations
costs = {}

costs['B'] = 6
costs['A'] = 2

costs['finish'] = float('inf')

print(float('inf'))

# Parents nodes
parents = {}

parents['A'] = 'start'
parents['B'] = 'start'

processed = []


def find_lowest_node_cost(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def dijikstra_search():
    # Знайти вузол з найменшою варсітю серед необроблених
    node = find_lowest_node_cost(costs)
    print(node)

    while node is not None:  # якщо пройдені всі вузли цикл завершуємо
        cost = costs[node]

        neighbors = graph[node]

        for neighbor in neighbors:  # перебираємо усіх сусідів поточного вузла
            new_cost = cost + neighbors[neighbor]
            # Якщо до сусіда можна дійти швидше через поточний вузол
            if costs[neighbor] > new_cost:
                # оновлюємо вартість цього вузла
                costs[neighbor] = new_cost
                # Цей вузол стає батьком для наших нових сусідів
                parents[neighbor] = node

        processed.append(node)  # Помічаємо вузол як оброблений
        # Шукаємо наступний вузол з найменшою вартістю
        node = find_lowest_node_cost(costs)
        print(node)


print('+' * 80)
dijikstra_search()
