

from collections import deque

unsearched = deque([starting_node])

def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_movies(node):
        if is_goal(m):
            return m
        unsearched.append(m)