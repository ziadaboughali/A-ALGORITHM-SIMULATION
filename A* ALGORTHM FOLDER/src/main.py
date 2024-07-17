from maze import generateMaze
from state import State 
from repeatedForwardAStar import repeatedForwardA as rfa
from repeatedBackwardAStar import repeatedBackwardA as rba
from adaptiveAStar import adaptiveA as aa
import matplotlib.pyplot as plt

# global variable for grid size and the number of mazes to run on
ROWS = 101
MAZE_NUM = 50

def main():

    avgForwardTime, avgBackwardTime, avgAdaptiveTime, avgExpandedForward, avgExpandedBackward, avgExpandedAdaptive = 0, 0, 0, 0, 0, 0

    # looping through all 50 mazes and running the three A Star algos on them
    for grids in range(0, MAZE_NUM):
        # printing each maze
        print("Maze", grids + 1, ":")
        print(generateMaze())
        print("")
        print("-------------------------------------------------------------------------")

        # preliminary stuff
        grid = generateMaze()
        start = (0, 0)
        goal = (len(grid) - 1, len(grid) - 1)
        
        # testing repeated forward A Star
        print("Repeated Forward A Star Statistics:")
        try:
            rfa_agent_path = None
            while rfa_agent_path is None:
                astar_rfa = State(ROWS, start, goal)
                rfa_agent_path, expanded, iterations, running_time = rfa(astar_rfa, grid)
                avgForwardTime += running_time
                avgExpandedForward += expanded
                print("Number of expanded cells:", expanded)
                print("Number of iterations:", iterations)
                print("Running time:", running_time, "seconds")
                # Plot the grid with the highlighted path
                plt.imshow(grid, cmap='gray')
                for i in range(len(rfa_agent_path) - 1):
                    plt.plot([rfa_agent_path[i][1], rfa_agent_path[i+1][1]], [rfa_agent_path[i][0], rfa_agent_path[i+1][0]], 'r')
                # indicating start position in blue
                plt.plot(start[1], start[0], 'bo')
                # indicating goal position in green
                plt.plot(goal[1], goal[0], 'go')
                plt.xticks([])
                plt.yticks([])
                plt.show()
                # saving the output to a file
                filename = 'repeated_forward_grid_' + str(grids + 1) + '.png'
                plt.savefig(filename)
                plt.clf()
                print("-------------------------------------------------------------------------")
        except:
            print("No path could be found on this maze for repeated forward A Star")
            print("")
        
        # testing repeated backward A Star
        print("Repeated Backward A Star Statistics:")
        try:
            rba_agent_path = None
            while rba_agent_path is None:
                astar_rba = State(ROWS, start, goal)
                rba_agent_path, expanded, iterations, running_time = rba(astar_rba, grid)
                avgBackwardTime += running_time
                avgExpandedBackward += expanded
                print("Number of expanded cells:", expanded)
                print("Number of iterations:", iterations)
                print("Running time:", running_time, "seconds")
                # Plot the grid with the highlighted path
                plt.imshow(grid, cmap='gray')
                for i in range(len(rba_agent_path) - 1):
                    plt.plot([rba_agent_path[i][1], rba_agent_path[i+1][1]], [rba_agent_path[i][0], rba_agent_path[i+1][0]], 'r')
                # indicating start position in blue
                plt.plot(start[1], start[0], 'bo')
                # indicating goal position in green
                plt.plot(goal[1], goal[0], 'go')
                plt.xticks([])
                plt.yticks([])
                plt.show()
                # saving the output to a file
                filename = 'repeated_bakward_grid_' + str(grids + 1) + '.png'
                plt.savefig(filename)
                plt.clf()
                print("-------------------------------------------------------------------------")
        except:
            print("No path could be found on this maze for repeated backward A Star")
            print("")

        # testing adaptive A Star
        print("Adaptive A Star Statistics:")
        try:
            aa_agent_path = None
            while aa_agent_path is None:
                astar_aa = State(ROWS, start, goal)
                aa_agent_path, expanded, iterations, running_time = aa(astar_aa, grid)
                avgAdaptiveTime += running_time
                avgExpandedAdaptive += expanded
                print("Number of expanded cells:", expanded)
                print("Number of iterations:", iterations)
                print("Running time:", running_time, "seconds")
                # Plot the grid with the highlighted path
                plt.imshow(grid, cmap='gray')
                for i in range(len(aa_agent_path) - 1):
                    plt.plot([aa_agent_path[i][1], aa_agent_path[i+1][1]], [aa_agent_path[i][0], aa_agent_path[i+1][0]], 'r')
                # indicating start position in blue
                plt.plot(start[1], start[0], 'bo')
                # indicating goal position in green
                plt.plot(goal[1], goal[0], 'go')
                plt.xticks([])
                plt.yticks([])
                plt.show()
                # saving the output to a file
                filename = 'adaptive_a_grid_' + str(grids + 1) + '.png'
                plt.savefig(filename)
                plt.clf()
                print("-------------------------------------------------------------------------")
                print("")
        except:
            print("I could not reach the target using adaptive A Star")
            print("No path could be found on this maze for adaptive A Star")
            print("-------------------------------------------------------------------------")
            print("")

    averageForwardTime = avgForwardTime / MAZE_NUM
    print("The average run time (in seconds) for repeated forward A* was: %f" % averageForwardTime)
    averageForwardExpandedCells =  avgExpandedForward / MAZE_NUM
    print("The average expanded cells for repeated forward A* was: %d" % averageForwardExpandedCells)

    averageBackwardTime = avgBackwardTime / MAZE_NUM
    print("The average run time (in seconds) for repeated backward A* was: %f" % averageBackwardTime)
    averageForwardExpandedCells =  avgExpandedBackward / MAZE_NUM
    print("The average expanded cells for repeated backward A* was: %d" % averageForwardExpandedCells)

    averageAdaptiveTime = avgAdaptiveTime / MAZE_NUM
    print("The average run time (in seconds) for adaptive A* was: %f" % averageAdaptiveTime)
    averageAdaptiveExpandedCells =  avgExpandedAdaptive / MAZE_NUM
    print("The average expanded cells for adaptive A* was: %d" % averageAdaptiveExpandedCells)
    print("")
    print("-------------------------------------------------------------------------")

if __name__ == '__main__':
    main()