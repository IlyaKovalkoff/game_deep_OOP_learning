from cell import Cell
import my_player as pl
import my_shop as sh
import random
import player_input as pi
#((()))(((())))((((()))))(((((())))))
class GameEngine:

    def __init__(self):

        self.__field_size_x = 15
        self.__field_size_y = 10
        self.__mine_rate = 30
        self.__healh_rate = 2
        self.__money_rate = 10
        self.__sweeper_rate = 5
        self.__mine_field = None # Initialized in start_game method
        self.__player = pl.Player()
        self.__shop = sh.Shop(self.__player)
        self.__player_input = pi.PlayerInput()

    def configure_next_lvl(self):
        self.__field_size_x += 0
        self.__field_size_y += 0
        
        self.__mine_rate += 0 
        self.__healh_rate += 0 
        self.__money_rate += 0
        self.__sweeper_rate += 0

    def print_game_over(self):
        print('''                                                                                                            ⠄⠄⣿⣿⣿⣿⠘⡿⢛⣿⣿⣿⣿⣿⣧⢻⣿⣿⠃⠸⣿⣿⣿⠄⠄⠄⠄⠄
                                                                                                            ⠄⠄⣿⣿⣿⣿⢀⠼⣛⣛⣭⢭⣟⣛⣛⣛⠿⠿⢆⡠⢿⣿⣿⠄⠄⠄⠄⠄
                                                                                                            ⠄⠄⠸⣿⣿⢣⢶⣟⣿⣖⣿⣷⣻⣮⡿⣽⣿⣻⣖⣶⣤⣭⡉⠄⠄⠄⠄⠄
                                                                                                            ⠄⠄⠄⢹⠣⣛⣣⣭⣭⣭⣁⡛⠻⢽⣿⣿⣿⣿⢻⣿⣿⣿⣽⡧⡄⠄⠄⠄
                                                                                                            ⠄⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣶⣌⡛⢿⣽⢘⣿⣷⣿⡻⠏⣛⣀⠄⠄
                                                                                                            ⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠙⡅⣿⠚⣡⣴⣿⣿⣿⡆⠄
                                                                                                            ⠄⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⣱⣾⣿⣿⣿⣿⣿⣿⠄
                                                                                                            ⠄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⠄
                                                                                                            ⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠣⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄
                                                                                                            ⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠑⣿⣮⣝⣛⠿⠿⣿⣿⣿⣿⠄
                                                                                                            ⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄''')

    def field_generation(self):
        field = []
        chance_nxLvl = random.randrange(1, self.__field_size_x - 1 , 1)
        for y in range(self.__field_size_y):
            field.append([])
            
            for x in range (self.__field_size_x):
                if x == 0 or y == 0 or x == self.__field_size_x -1 or y == self.__field_size_y -1:
                    field[y].append(Cell().wall())
                else:
                    chance = random.randrange(1, 100, 1)
                    if 0 < chance < self.__mine_rate:    
                        field[y].append(Cell().mine())
                    elif self.__mine_rate < chance < self.__mine_rate + self.__money_rate:
                        field[y].append(Cell().money())
                    elif self.__mine_rate + self.__money_rate < chance < self.__mine_rate + self.__money_rate + self.__sweeper_rate:
                        field[y].append(Cell().sweeper())
                    elif self.__mine_rate + self.__money_rate + self.__sweeper_rate < chance < self.__mine_rate + self.__money_rate + self.__sweeper_rate + self.__healh_rate:
                        field[y].append(Cell().health())
                    else:

                        field[y].append(Cell().empty())
        field[self.__field_size_y - 1 ][chance_nxLvl] = Cell().door()
                
        return field

    def count_mines(self, around_x, around_y):
        count = 0 
        y = around_y - 1
        while y <= around_y + 1:
            x = around_x - 1
            while x <= around_x + 1 :
                if self.__mine_field[y][x].is_mine():
                    count += 1
                x += 1
            y += 1
        return count

    def marking_mines(self):
        x, y = self.__player.get_pos()
        self.__player_input.read()
        if self.__player_input.is_up_left():
            self.__mine_field[y + 1][x - 1].marking()
        elif self.__player_input.is_up():    
            self.__mine_field[y + 1][x].marking()
        elif self.__player_input.is_up_right():
            self.__mine_field[y + 1][x + 1].marking()
        elif self.__player_input.is_left():
            self.__mine_field[y][x - 1].marking()
        elif self.__player_input.is_right():
            self.__mine_field[y][x + 1].marking()
        elif self.__player_input.is_down_left():
            self.__mine_field[y - 1][x - 1].marking()
        elif self.__player_input.is_down():
            self.__mine_field[y - 1][x].marking()
        elif self.__player_input.is_down_right():
            self.__mine_field[y - 1][x + 1].marking()
        else:
            pass
        
    def mine_detector(self, player):
        pl_x, pl_y = player.get_pos()
        
        count = 0
        y  = pl_y - 1
        while y <= pl_y + 1:
            x = pl_x - 1
            while x <= pl_x + 1:
                if not self.__mine_field[y][x].is_wall() and not self.__mine_field[y][x].is_door():
                    self.__mine_field[y][x].reveal(self.count_mines(x,y))
                
                x += 1
            y += 1
      
    def is_pos_exit(self, player):
        x, y = player.get_pos()
        if self.__mine_field[y][x].is_door():
            return True
     
    def print_stats(self, player):
        print('PLAYER HAS:',player.get_health() , 'HEALTH',
                ',', player.get_money(), '$ AND', player.get_sweepers(), 'SWEEPERS')
                    
    def show_field(self, player):
        y = len(self.__mine_field) - 1
        offset= ''
        line_count = 0
        help_strings = [] 
        if self.__player_input.is_help_enabled():
            help_strings = self.__player_input.get_help()

        while y >= 0:
            x = 0
            line = offset
            
            while x < len(self.__mine_field[y]):
                pl_x, pl_y = player.get_pos()
                
                if x == pl_x and y == pl_y:
                    line += self.__mine_field[y][x].get_icon()[0] + player.get_icon()
                else:
                    line += self.__mine_field[y][x].get_icon()
                x += 1
            if line_count < len(help_strings):
                line += help_strings[line_count]
                line_count += 1
            y -= 1
                
            print(line)

    def start_game(self):
        

        while not self.__player_input.is_exit():

            self.__mine_field = self.field_generation()
            self.__player.set_field(self.__mine_field)
            self.__player.set_pos(self.__field_size_x/2, 1)
            self.__mine_field[1][int(self.__field_size_x/2)].empty()
            while not self.__player_input.is_exit():
                
                if self.__player.is_dead():
                    self.print_game_over()
                    exit(0)

                if self.is_pos_exit(self.__player):
                    break
            
                self.mine_detector(self.__player)
                self.show_field(self.__player)
                self.print_stats(self.__player)

                if self.__player_input.is_marking_mode_pressed():
                    self.__player_input.switch_marking_mode()

                if self.__player_input.is_marking_mode_on():
                    self.marking_mines()

                else:
                    self.__player_input.read()

                    if self.__player_input.is_up():
                        self.__player.move_up()

                    elif self.__player_input.is_down():
                        self.__player.move_down()

                    elif self.__player_input.is_left():
                        self.__player.move_left()
                    
                    elif self.__player_input.is_right():
                        self.__player.move_right()

                    elif self.__player_input.is_up_left():
                        self.__player.move_up_left()

                    elif self.__player_input.is_up_right():
                        self.__player.move_up_right()

                    elif self.__player_input.is_down_left():
                        self.__player.move_down_left()

                    elif self.__player_input.is_down_right():
                        self.__player.move_down_right()
                    
                    elif self.__player_input.is_exit():
                        pass

                    elif self.__player_input.is_use_sweep():
                        self.__player.sweep()

                    elif self.__player_input.is_switch_help_pressed():
                        self.__player_input.switch_help_enabled()

                    # --------------- FOR TEST -------------------
                    elif self.__player_input.is_test_buy_health():
                        self.__shop.buy_health()

                    elif self.__player_input.is_test_buy_sweepers():
                        self.__shop.buy_sweepers()
                    # -----------------<<<>>>---------------------
                    elif self.__player_input.is_marking_mode_pressed():
                        pass
        
                    else:
                        self.__player_input.print_help_if_user_press_wrong_key()

            if self.__player_input.is_exit():
                    break
            self.__shop.show_shop()
            self.configure_next_lvl()


game = GameEngine()
game.start_game()