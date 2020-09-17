# Author: Alexander Dietz apd5560@psu.edu
# Collaborator: Jeremy Bell jjb6692@psu.edu
# Collaborator: Balade Shala bks5681@psu.edu
# Collaborator: Emily Davis ekd5306@psu.edu
# Section: 6
# Breakout: 3

def sum_n(n):
  if (n==0):
    return 0
  else:
    return n + sum_n(n-1)
    
def print_n(s,n):
  if (n==0):
    return
  else:
    print(s)
    print_n(s,n-1)
    return

def run():
  n = int(input("Enter an int: "))
  print(f"sum is {sum_n(n)}.")
  s = input("Enter a string: ")
  print_n(s,n)

if __name__ == "__main__":
  run()