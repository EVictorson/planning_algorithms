"""
Module to represent the environment in which we are planning
"""

class Environment:
    """ Class to represent the environment in which we are planning. """

    # cleaner than using a list comprehension as it will result in a
    # (0, 0) motion, which is invalid
    AVAILABLE_MOTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                         (1, 0), (1, -1), (0, -1), (-1, -1)]

    # a list of sets composed of (x,y) coords of interior wall
    # start and stop points
    APRIORI_STATIC_OBSTACLES = [((10, 15), (20, 15)),
                                ((20, 0), (20, 15)),
                                ((30, 15),(30, 30)),
                                ((40, 0), (40, 15))]

    def __init__(self, x:int, y:int):
        self.x_size = x
        self.y_size = y
        self.grid_size = (x, y)
        self.obstacles = self.create_obstacle_map_update()

    def update_obstacles(self, obstacles:set):
        """ Update the set of obstacles. """
        self.obstacles = obstacles

    def create_obstacle_map_update(self) -> set:
        """
        Create the obstacle map using set comprehensions
        timeit.timeit (n=1000000) = 8.440835892979521
        So, not only is this way cleaner, it's faster, too.
        """
        x = self.x_size
        y = self.y_size

        # create the top border of the map
        obstacle = {(i, 0) for i in range(x)}
        # create the bottom border of the map
        obstacle.update({(i, y - 1) for i in range(x)})
        # Create left vertical border of the map
        obstacle.update({(0,i) for i in range(y)})
        # Create the right vertical border of the map
        obstacle.update({(x - 1, i) for i in range(y)})

        # add static walls:
        for i in range(10, 21):
            obstacle.add((i, 15))
        for i in range(15):
            obstacle.add((20, i))

        for i in range(15, 30):
            obstacle.add((30, i))
        for i in range(16):
            obstacle.add((40, i))

        # TODO: clean up the above magic number values with
        # something less brittle:
        '''
        walls = self.APRIORI_STATIC_OBSTACLES

        for i in range(walls[0][0][0], walls[0][1][0])
                obstacle.add(i, walls[0][0][1])

        for i in range(walls[1][0][0], walls[1][0][0])
                obstacle.add(i, walls[0][0][1])
        '''


        return obstacle

    def create_obstacle_map_add(self) -> set:
        """
        Create obstacle map using set.add method.
        timeit.timeit (n=1000000) = 9.1082749539637
        """
        x = self.x_size
        y = self.y_size
        obstacle = set()

        # create the top border of the map
        for i in range(x):
            obstacle.add((i, 0))
        # create the bottom border of the map
        for i in range(x):
            obstacle.add((i, y - 1))
        # Create left vertical border of the map
        for i in range(y):
            obstacle.add((0, i))
        # Create the right vertical border of the map
        for i in range(y):
            obstacle.add(x - 1, i)

        return obstacle
