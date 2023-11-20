from re import I


class Staples:
    def __init__(self, name, color):
        self._name = name
        self._color = color
        
    def get_name(self):
        return self._name
    
    def get_color(self):
        return self._color

    def set_name(self, newName):
        self._name = newName
        
        if self._name == newName:
            return True
        
    def set_color(self, newColor):
        self._color = newColor
        
        if self._color == newColor:
            return True
        
    
