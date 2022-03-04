from abc import abstractmethod


class Cell:
    def __init__(self, row=0, col=0):
        self._row = row
        self._col = col
        self._occupant = None
        self._color = None
        self._hours = 0

    # TODO: hours getter and setter
    @property
    def hours(self):
        return self._hours

    # DONE TODO: occupant getter
    @property
    def occupant(self):
        return self._occupant

    def set_occupant(self, obj):
        # DONE TODO: set occupant for the Plain cell
        #       return whether success or not
        if self._occupant == None:
            self._occupant = obj
            return True
        else:
            if self._occupant.interact_with(obj):
                self._occupant = obj
                return True
            return False

        # END TODO

    def remove_occupant(self):
        # DONE TODO: remove the occupant
        self._occupant = None

        # END TODO

    def display(self):
        # DONE TODO: print a string to display the cell
        #       and the occupant in the cell
        if self._occupant != None:
            print(
                f"{self._color} {self._occupant.display()}{self._color} \033[0m   ",
                end="",
            )
        else:
            print(f"{self._color}   \033[0m   ", end="")

        # END TODO


class Plain(Cell):
    def __init__(self, row, col):
        Cell.__init__(self, row, col)
        self._color = "\033[1;32;42m"
        self._hours = 1


class Mountain(Cell):
    def __init__(self, row, col):
        Cell.__init__(self, row, col)
        self._color = "\033[1;37;47m"

    def set_occupant(self, obj):
        # DONE TODO: return False
        return False

        # END TODO


class Swamp(Cell):
    def __init__(self, row, col):
        Cell.__init__(self, row, col)
        self._color = "\033[1;34;44m"
        self._hours = 2
