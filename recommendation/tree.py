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
    



