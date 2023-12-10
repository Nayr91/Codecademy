class Tree:
    def __init__ (self, data, genre=None, release= None, rating = None):
        self.data = data
        self.genre = genre
        self.release = release
        self.rating = rating
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        print(f"Adding {child} to {self}")
    
    def next_child(self, pick):
        new_node = self.children[pick]
        return new_node
    
    def add_game_data(self, genre, release, rating):
        self.genre = genre
        self.release = release
        self.rating = rating
        print(f"Adding {genre}, {release} and {rating} to {self.data}")
    
    def find_child(self, pick):
        for i in self.children:
            if i.data == pick:
                return i
        return False

    def all_data(self):
       print(f"{self.data} was released in {self.release} and we score it {self.rating}.")
