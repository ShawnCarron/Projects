# Problem -> Collatz Conjecture: 
"""
    Pick any integer 'x' to start with. 'x' should be divided by 2 if it is even, and multiplied by 3 + 1 if it is odd. 
    No matter the initial value choosen if this method is repeated enough times the series will ultimately reach cycles {4, 2, 1}.
"""
x: int = int(input("Please choose a even number to start with: "))

def collatz_sequence(x):
  """
  Takes any number and performs the calcualation of: if 'x' is even divide by two. If 'x' is odd multiply by 3 and add 1.

  Example --> \nPlease choose a even number to start with: 23\n
                [23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1] 
  Args:
      x (_type_): Takes any integer as a paramater

  Returns:
      _type_: Returns list of numbers that will always end in 4, 2, 1
  """
  global seq
  seq = [x]
  if x < 1:
    return []
  while x > 1:
      if x % 2 == 0:
        x = x // 2
      else:
        x = 3 * x + 1 
      seq.append(x)
  return seq

def find_patterns():
  pass
  
def count_steps():
  # Test to see how many steps it took to get to 4-2-1
  count = len(seq) - 3
  return(f"{x} was your starting integer and the 4-2-1 pattern appeared after {count} steps.")



# Print out the collatz conjecture sequence
print(collatz_sequence(x))
print(count_steps())