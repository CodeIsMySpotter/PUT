import numpy as np



class Generator():

  def generate_int(range: int, length: int):

    return np.random.randint(1, range, length)