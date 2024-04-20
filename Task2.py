import random
import time
import pandas as pd
import matplotlib.pyplot as plt
from collections import deque

# Function to generate random and unique numbers for a given range
def generate_random_unique_numbers(start, end, count):
    return random.sample(range(start, end + 1), count)

# Function to build a tree for a given set of inputs
def build_tree(input_list):
    return input_list

# Breadth-First Search (BFS)
def bfs(tree, goal):
    queue = deque([tree])
    while queue:
        node = queue.popleft()
        if node == goal:
            return True
        if isinstance(node, list):
            queue.extend(node)
    return False

# Depth-First Search (DFS)
def dfs(tree, goal):
    stack = [tree]
    while stack:
        node = stack.pop()
        if node == goal:
            return True
        if isinstance(node, list):
            stack.extend(node[::-1])
    return False

# Generate random and unique numbers for each range
ranges = [(1000, 40000), (40001, 80000), (80001, 200000), (200001, 1000000)]
sets_of_inputs = [generate_random_unique_numbers(start, end, 100) for start, end in ranges]

# Build trees for each set of inputs
trees = [build_tree(input_set) for input_set in sets_of_inputs]

# Initialize DataFrame to store results
results = pd.DataFrame(columns=['Range', 'BFS Time (s)', 'DFS Time (s)'])

# Perform BFS and DFS on each tree and calculate the time taken
for i, tree in enumerate(trees):
    goal_index = len(tree) - 220
    if goal_index >= 0:  # Ensure goal index is non-negative
        goal_node = tree[goal_index]

        bfs_start_time = time.time()
        bfs_result = bfs(tree, goal_node)
        bfs_time = time.time() - bfs_start_time

        dfs_start_time = time.time()
        dfs_result = dfs(tree, goal_node)
        dfs_time = time.time() - dfs_start_time

        results.loc[i] = [f"{ranges[i][0]}-{ranges[i][1]}", bfs_time, dfs_time]
    else:
        print(f"Skipping tree {i+1} as it has less than 220 nodes.")

# Filter out trees with less than 220 nodes
results = results[results['Range'] != '200001-1000000']

# Plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(results['Range'], results['BFS Time (s)'], color='blue', alpha=0.5, label='BFS Time (s)')
plt.bar(results['Range'], results['DFS Time (s)'], color='green', alpha=0.5, label='DFS Time (s)')
plt.xlabel('Range')
plt.ylabel('Time (seconds)')
plt.title('Time Taken by BFS and DFS')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
