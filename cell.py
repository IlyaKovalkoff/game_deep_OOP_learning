class Cell:

    def __init__(self):
        self.__value = ''
        self.__is_revealed = False
        self.__is_mine_sweeped = False
        self.__is_marked = False
        self.__mines_around  = 0 

    def mine(self):
        self.__value = '*'
        return self 

    def door(self):
        self.__value = '!'
        self.__is_revealed = True
        return self

    def money(self):
        self.__value = '$'
        return self 
    
    def sweeper(self):
        self.__value = '#'
        return self 

    def health(self):
        self.__value = '♥'
        return self 
    
    def wall(self):
        self.__value = '='
        self.__is_revealed = True
        return self 
        
    def empty(self):
        self.__value = '-'
        return self 
    
    def reveal(self, mines_around):
        self.__is_revealed = True
        if mines_around == 0:
            self.__mines_around = '.'
        else:
            self.__mines_around = mines_around

    def reveal_mine(self):
        self.__is_mine_sweeped = True

    def marking(self):
        self.__is_marked = not self.__is_marked
            
    def is_marked(self):
        return self.__is_marked

    def is_door(self):
        return self.__value == '!'

    def is_empty(self):
        return  self.__value == '-'
    
    def is_health(self):
        return self.__value == '♥'
    
    def is_wall(self):
        return  self.__value == '='

    def is_sweeper(self):
        return  self.__value == '#'
    
    def is_mine(self):
        return  self.__value == '*'

    def is_money(self):
        return  self.__value == '$'

    def get_icon(self):
        if self.is_marked() and not self.is_mine_revealed():
                return str(self.__mines_around) + '⚑ '
        if self.is_empty():
            if self.is_revealed():
                return str(self.__mines_around) + '  '
            else:
                return '   '
        elif self.is_revealed():
            if self.is_mine():
                if self.is_mine_revealed():
                    return str(self.__mines_around) + '* '
                else:
                    return str(self.__mines_around) + '  '
            if self.is_wall() or self.is_door():
                return self.__value + '  '

            return str(self.__mines_around) + self.__value + ' '
        else:
            return '   ' 
      
                
    def is_revealed(self):
        return self.__is_revealed 

    def is_mine_revealed(self):
        return self.__is_mine_sweeped