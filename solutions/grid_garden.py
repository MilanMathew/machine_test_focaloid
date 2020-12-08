def grid_garden_hatch_time(grid_garden):
    """
    Returns the minimum time in seconds, for a grid garden to
    to have all its larvae hatched into butterflies.

        Parameters:
            grid_garden (list): A 2d list

        Returns:
            seconds (int): Time in seconds

    Convention: '0' denotes empty space, '1' a larva and '2' a butterfly.\n
    Note: Larvae only hatch if they come into contact with a butterfly.
    No butterfly, no hatching! Thats the motto of this grid garden.
    
    >>> grid_garden_hatch_time([])              # empty list
    -1
    >>> grid_garden_hatch_time([[]])            # empty 2d list
    -1
    >>> grid_garden_hatch_time([[], [], []])    # empty garden
    -1
    >>> grid_garden_hatch_time([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
    4
    >>> grid_garden_hatch_time([[1, 1, 1], [1, 1, 0], [0, 1, 1]])   # no butterfly
    -1
    >>> grid_garden_hatch_time([[0, 1, 0], [1, 2, 0], [0, 0, 1]])
    2
    >>> grid_garden_hatch_time([[0, 0, 0, 1], [1, 1, 0, 0], [0, 2, 0, 1], [1, 0, 1, 0]])
    4
    """
    from copy import deepcopy

    butterflies = []
    larvae = []

    # find the locations of each larva and butterfly
    for i in range(len(grid_garden)):
        for j in range(len(grid_garden[i])):
            if grid_garden[i][j] == 2:
                butterflies.append((i, j))
            elif grid_garden[i][j] == 1:
                larvae.append((i, j))

    # If there are no butterflies in the garden, it won't hatch new ones.
    if len(butterflies) == 0:
        return -1

    # build a garden similar to this one except this one has all its
    # larvae hatched into butterflies. This will be used to determine
    # when to stop looking for new butterflies.
    end_result = deepcopy(grid_garden)
    for larvai, larvaj in larvae:
        end_result[larvai][larvaj] = 2

    # avoid looking at the same block over and over again
    nodes = set(butterflies)
    seconds = 0
    while grid_garden != end_result:
        # increment timer for each loop.
        seconds += 1

        # initially starting at the known butterfly locations,
        # search all the four neighboring blocks, located vertically  
        # and horizontally but not diagonally.
        for x, y in nodes.copy():
            if x-1 >= 0:
                nodes.add((x-1, y))
                if grid_garden[x-1][y] == 1:
                    grid_garden[x-1][y] = 2
            if y-1 >= 0:
                nodes.add((x, y-1))
                if grid_garden[x][y-1] == 1:
                    grid_garden[x][y-1] = 2
            if x+1 < len(grid_garden):
                nodes.add((x+1, y))
                if grid_garden[x+1][y] == 1:
                    grid_garden[x+1][y] = 2
            if y+1 < len(grid_garden[x]):
                nodes.add((x, y+1))
                if grid_garden[x][y+1] == 1:
                    grid_garden[x][y+1] = 2
            
            # discard a block after searching it.
            nodes.discard((x, y))

    return seconds


if __name__ == "__main__":
    import doctest
    doctest.testmod()
