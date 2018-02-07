# Board
#
# Feb. 7, 2018
# Xiao Xin, Yindong Sun

# Specification
#
# dimension: number of dots on each side
# dot id: assume dot position at (i, j)
#         id = i * dimension + j
# edge: tuple of the id of two dots
# box: the minimal square surrounded by edges
# dox id: the id of the upper left dot of the square

class Board:
  def __init__(self, dimension):
    self.dimension = dimension
    self.edges = set()

  def __max_edge_number__(self):
    return (self.dimension - 1) * dimension * 2

  def is_filled(self):
    return len(self.edges) == self.__max_edge_number__()

  def number_of_boxes(self):
    return (self.dimension - 1) * (self.dimension - 1)

  def add_edge(self, new_edge):
    # TODO:
    #   return a list of the ID of boxes 
    #   that are colored
    raise NotImplementedError("TO BE IMPLEMENTED")
