"""
Module to visualize created plans.
"""

import os
import sys
import matplotlib.pyplot as plt

import environment as env

class Plotter:
    """
    Helper class to plot created plans.
    """
    def __init__(self, x_init, x_goal, x_map, y_map):
        self.x_init, self.x_goal = x_init, x_goal
        self.environment = env.Environment(x_map, y_map)
        self.obstacles = self.environment.create_obstacle_map_update()

    def update_obstacles(self, obstacles):
        self.obstacles = obstacles

    def animate(self, path, visited, name):
        self.plot_grid(name)
        self.plot_visited(visited)
        self.plot_path(path)
        plt.show()

    def plot_grid(self, name):
        obstacles_x = [x[0] for x in self.obstacles]
        obstacles_y = [x[1] for x in self.obstacles]

        plt.plot(self.x_init[0], self.x_init[1], "bs")
        plt.plot(self.x_goal[0], self.x_goal[1], "gs")
        plt.plot(obstacles_x, obstacles_y, "sk")
        plt.title(name)
        plt.axis("equal")
        plt.show()


    def plot_visited(self, visited, color='gray'):
        if self.x_init in visited:
            visited.remove(self.x_init)

        if self.x_goal in visited:
            visited.remove(self.x_goal)

        count = 0

        for x in visited:
            count += 1
            plt.plot(x[0], x[1], color=color, marker='o')
            plt.gcf().canvas.mpl_connect('key_release_event',
                                         lambda event: [exit(0) if event.key == 'escape' else None])

            if count < len(visited) / 3:
                length = 20
            elif count < len(visited) * 2 / 3:
                length = 30
            else:
                length = 40

            if count % length == 0:
                plt.pause(0.001)
        plt.pause(0.01)


    def plot_path(self, path, color='r', flag=False):
        path_x = [path[i][0] for i in range(len(path))]
        path_y = [path[i][1] for i in range(len(path))]

        if not flag:
            plt.plot(path_x, path_y, linewidth='3', color='r')
        else:
            plt.plot(path_x, path_y, linewidth='3', color=cl)

        plt.plot(self.x_init[0], self.x_init[1], "bs")
        plt.plot(self.x_goal[0], self.x_goal[1], "gs")

        plt.pause(0.01)


if __name__ == '__main__':
    start = (5, 5)
    goal = (45, 25)
    xmap = 51
    ymap = 31

    plot = Plotter(start, goal, xmap, ymap)
    plot.plot_grid('test')
