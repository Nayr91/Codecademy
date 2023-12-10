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
    genre = ""
    while genre == "":
        request = input_request().lower()
        for i in range(len(potential_names)):
            if request == matching_potential[i].lower():
                genre = matching_potential[i]
                break
            for j in potential_names[i]:
                if j.lower() == request:
                    genre = matching_potential[i]
                    break
        if genre == "":
            print("Name not in list, try again")
    
    genre_tree = master_tree.find_child(genre)
    if genre_tree == False:
        print("Unable to find")
        
    print("The top 5 game recommendations are as follows:")
    print(f"1. {genre_tree.children[0].data}")
    print(f"2. {genre_tree.children[1].data}")
    print(f"3. {genre_tree.children[2].data}")
    print(f"4. {genre_tree.children[3].data}")
    print(f"5. {genre_tree.children[4].data}")    
    more_data = int(input("Which game would you like to more about?\n"))
    genre_tree.children[more_data - 1].all_data()
    
   
def input_request():
    x = input("Which Genre are you interested in? \n")
    return x

welcome()