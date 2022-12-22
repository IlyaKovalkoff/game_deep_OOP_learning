from cell import Cell
import my_player as pl
import my_shop as sh
import random


class PlayerInput:

    def __init__(self):
        self.__input = None

        self.__marking_mode_pressed = '*'
        self.__marking_mode = False

        self.__help_enabled = True

        self.__switch_help = 'h'
        self.__up_left = '7'
        self.__up = '8'
        self.__up_right = '9'
        self.__left = '4'
        self.__center = '5'
        self.__right = '6'
        self.__down_left = '1'
        self.__down = '2'
        self.__down_right = '3'

        self.__use_sweep = self.__center
        self.__exit = '0'

        self.__test_buy_sweepers = 'p'
        self.__test_buy_health = 't'
        

    def is_help_enabled(self):
        return self.__help_enabled
    
    def switch_help_enabled(self):
        self.__help_enabled = not self.__help_enabled

    def is_switch_help_pressed(self):
        return self.__input == self.__switch_help

    def get_help(self):
        return [
            'Key bindings:',
            'Move keys - "'+ self.__up + '", "' + self.__up_left + '", "' + self.__up_right + '", "' + self.__down + '", "' + self.__down_left + '", "' + self.__down_right + '", "'+ self.__left +'", "' + self.__right + '".',
            'Sweep - "' + self.__use_sweep + '".',
            'Marking mode on/off - "'+ self.__marking_mode_pressed +'", use move keys to set marks.',
            'Help on/off - "' + self.__switch_help + '".',
            'Exit - "' + self.__exit + '".']

    def print_help_if_user_press_wrong_key(self):
        print ('Y use wrong hotkeys, try press "' + self.__switch_help + '" to look at help menu')

    def read(self):
        self.__input = input('Where y go? -->')

    def is_up_left(self):
        return self.__input == self.__up_left

    def is_up_right(self):
        return self.__input == self.__up_right

    def is_down_left(self):
        return self.__input == self.__down_left

    def is_down_right(self):
        return self.__input == self.__down_right
        
    def is_up(self):
        return self.__input == self.__up

    def is_down(self):
        return self.__input == self.__down

    def is_left(self):
        return self.__input == self.__left
    
    def is_right(self):
        return self.__input == self.__right

    def is_up_left(self):
        return self.__input == self.__up_left

    def is_up_right(self):
        return self.__input == self.__up_right

    def is_down_left(self):
        return self.__input == self.__down_left
    
    def is_down_right(self):
        return self.__input == self.__down_right

    def is_use_sweep(self):
        return self.__input == self.__use_sweep

    def is_exit(self):
        return self.__input == self.__exit


    def is_marking_mode_on(self):
        return self.__marking_mode
    
    def switch_marking_mode(self):
        self.__marking_mode = not self.__marking_mode

    def is_marking_mode_pressed(self):
        return self.__input == self.__marking_mode_pressed

        

    def is_test_buy_sweepers(self):
        return self.__input == self.__test_buy_sweepers

    def is_test_buy_health(self):
        return self.__input == self.__test_buy_health


    


