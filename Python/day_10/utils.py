class GraphNode:
    def __init__ (self, value):
        self.value = value

        self.north = False
        self.south = False
        self.west = False
        self.east = False

        self.defined_direction()

    def defined_direction(self):
        match self.value:
            case "|" :
                self.north = True
                self.south = True
            case "-":
                self.east = True
                self.west = True
            case "L":
                self.north = True
                self.east = True
            case "J":
                self.north = True
                self.west = True
            case "7":
                self.south = True
                self.west = True
            case "F":
                self.south = True
                self.east = True
            case "S" :
                self.north = True
                self.south = True
                self.east = True
                self.west = True
            case _:
                pass
