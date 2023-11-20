from tree import Tree
from data import *

def welcome():
    print("""
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          Welcome to the Nayr Game Recommender 3000!
          Please enter a Genre below and select from 
                   the options available!
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~         
          """)
    request = input_request()
    
    
def input_request():
    x = input("Which Genre are you interested in? \n")
    return x

welcome()