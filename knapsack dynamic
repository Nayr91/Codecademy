def dynamic_knapsack(weight_cap, weights, values):
  rows = len(weights) + 1
  cols = weight_cap + 1
  # Set up 2D array
  matrix = [ [y for y in range(cols)] for x in range(rows) ]

  # Iterate through every row
  for index in range(rows):
    # Initialize columns for this row
    matrix[index] = [ -1 for y in range(cols) ]

    # Iterate through every column
    for weight in range(cols):
      # Write your code here
      if index == 0 or weight == 0:
        matrix[index][weight] = 0
      elif weights[index - 1] <= weight:
        including_item = values[index - 1] + matrix[index - 1][weight - weights[index - 1]]

        excluding_item = matrix[index - 1][weight]
      
        matrix[index][weight] = max(including_item, excluding_item)
      else:
        matrix[index][weight] = matrix[index - 1][weight]
  # Return the value of the bottom right of matrix
  return matrix[rows-1][weight_cap]
