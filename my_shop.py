import my_player as pl
import random



class Shop:

    def __init__(self, pl):
        self.__price_health = 1000
        self.__price_sweeper = 500
        self.__player = pl
        
    def buy_health(self):

        if self.__player.get_money() >= self.__price_health:
            self.__player.change_money(-(self.__price_health))
            self.__player.change_hp(1)
        else:
            self.say_y_broke()
        
    def buy_sweepers(self):
        
        if self.__player.get_money() >= self.__price_sweeper:
            self.__player.change_money(-(self.__price_sweeper))
            self.__player.change_sweepers(1)
        else:
            self.say_y_broke()

    def show_shop(self):
        player_input = ''
        while player_input != '0':
            player_input = input('Press ''(q)'' if you want buy HEALTH or ''(w)'' if y want SWEEPERS or ''(e)'' to EXIT ? -->')
            match player_input:
                case 'q':
                    self.buy_health()
                case 'w':
                    self.buy_sweepers()
                case 'e':
                    break
                case _:
                    print('TRY to ENTER  (h),(s),(e),')
        
    def say_y_broke(self):

        print('Y DONT HAVE ENOUGH MONEY')
