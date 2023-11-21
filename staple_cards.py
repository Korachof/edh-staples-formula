


class Staples:
    def __init__(self, name, color, cardType):
        self._name = name
        self._color = color
        self._cardtype = cardType
        
    def get_name(self):
        return self._name
    
    def get_color(self):
        return self._color
    
    def get_type(self):
        return self._cardtype

    def set_name(self, newName):
        self._name = newName
        
        if self._name == newName:
            return True
        
    def set_color(self, newColor):
        self._color = newColor
        
        if self._color == newColor:
            return True
        
    def set_type(self, newType):
        self._cardtype = newType
        
        if self._cardtype == newType:
            return True 
        
    
