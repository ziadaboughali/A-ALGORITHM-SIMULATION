from heapq import *
from random import *
import time

# repeted backward A Star -- only difference from repeated Forward A Star is that you just flip start and goal
# Repeated backward A Star goes from the goal to the start
def repeatedBackwardA(self, grid):
    # Initialize the iteration counter and the expanded cells counter
    iterations = 0
    expanded = 0
    # Start the timer
    start_time = time.time()

    # (0,1) = north, (0,-1) = south, (1,0) = west, (-1,0) = east
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
    closed_list = set()
    came_from = {}
    
    # the g vaue of starting node is always 0
    state_g = {self.goal: 0}
    state_f = {self.goal: self.manhattan(self.goal, self.start)}
    open_list = []
    # pushing the nodes into the open list
    heappush(open_list, (state_f[self.goal], self.goal))

    # traversing through the maze/grid by popping elements/state (cells) from the open list
    while open_list:
        current_state = heappop(open_list)[1]

        if current_state == self.start:
            # Stop the timer
            end_time = time.time()
            agent_path = []
            while current_state in came_from:
                agent_path.append(current_state)
                current_state = came_from[current_state]
            self.distance = len(agent_path)
            # Return the path, the number of expanded cells, the number of iterations, and the running time
            return agent_path, expanded, iterations, end_time - start_time

        closed_list.add(current_state)

        # Increment the expanded cells counter
        expanded += 1 
        self.closed_list.add(current_state)

        # need to check neighbors and calculate their f values
        for i, j in neighbors:
            successor = current_state[0] + i, current_state[1] + j
            heuristic_g = state_g[current_state] + self.manhattan(current_state, successor)
            self.h = self.manhattan(current_state, self.start)
            # checking blocked status
            if 0 <= successor[0] < self.size:
                if 0 <= successor[1] < self.size:
                    if grid[successor[0]][successor[1]] == 1:
                        continue
                else:
                    continue
            else:
                continue
            if successor in closed_list and heuristic_g >= state_g.get(successor, 0):
                continue
            if heuristic_g < state_g.get(successor, 0) or successor not in [i[1] for i in open_list]:
                self.g.add(heuristic_g)
                came_from[successor] = current_state
                state_g[successor] = heuristic_g
                state_f[successor] = heuristic_g + self.manhattan(successor, self.start)
                heappush(open_list, (state_f[successor], successor))
        
        # Increment the iteration counter
        iterations += 1

    print("I cannot reach the target in repeated backward A Star")
    return False
