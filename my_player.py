import random
from cell import Cell

from my_shop import Shop as sp 




class Player:
   
    def __init__ (pl):
        pl.__x = None
        pl.__y = None
        pl.__field = None
        pl.__money = 0
        pl.__health = 3
        pl.__sweepers = 3

    def is_dead(pl):
        return pl.__health <= 0 

    def set_pos(pl,x,y):
        pl.__x = int(x)
        pl.__y = int(y)

    def get_money(pl):
        return pl.__money

    def get_sweepers(pl):
        return pl.__sweepers

    def get_health(pl):
        return pl.__health

    def change_hp(pl,points):
        pl.__health += points

    def change_money(pl, amount):
        pl.__money += amount

    def change_sweepers(pl, points):
        pl.__sweepers += points

    def get_pos(pl):
        return (pl.__x, pl.__y)

    def move_up_left(pl):
        if not pl.__field[pl.__y + 1][pl.__x - 1].is_wall():
            pl.__y += 1
            pl.__x -= 1
        pl.process_field_cell(pl.__field[pl.__y][pl.__x])

    def move_up_right(pl):
        if not pl.__field[pl.__y + 1][pl.__x + 1].is_wall():
            pl.__y += 1
            pl.__x += 1
        pl.process_field_cell(pl.__field[pl.__y][pl.__x])

    def move_down_left(pl):
        if not pl.__field[pl.__y - 1][pl.__x - 1].is_wall():
            pl.__y -= 1
            pl.__x -= 1
        pl.process_field_cell(pl.__field[pl.__y][pl.__x])

    def move_down_right(pl):
        if not pl.__field[pl.__y - 1][pl.__x + 1].is_wall():
            pl.__y -= 1
            pl.__x += 1
        pl.process_field_cell(pl.__field[pl.__y][pl.__x])

    def move_up(pl):
        if not pl.__field[pl.__y + 1][pl.__x].is_wall():
            pl.__y += 1
        pl.process_field_cell(pl.__field[pl.__y][pl.__x])

    def move_down(pl):
        if not pl.__field[pl.__y - 1][pl.__x].is_wall():
            pl.__y -= 1
        pl.process_field_cell(pl.__field[pl.__y][pl.__x])

    def move_left(pl):
        if not pl.__field[pl.__y][pl.__x - 1].is_wall():
            pl.__x -= 1
        pl.process_field_cell(pl.__field[pl.__y][pl.__x])

    def move_right(pl):
        if not pl.__field[pl.__y][pl.__x + 1].is_wall():
            pl.__x += 1
        pl.process_field_cell(pl.__field[pl.__y][pl.__x]) 

    def sweep(pl):
        y = pl.__y - 1 
        while y <= pl.__y + 1:
            x = pl.__x - 1
            while x <= pl.__x + 1 :
                if pl.__field[y][x].is_mine():
                    pl.__field[y][x].reveal_mine()
                x += 1
            y += 1
        pl.change_sweepers(-1)

    def set_field(pl, field):
        pl.__field = field

    def error(pl):
        print('Y MAKE MISTAKE')

    def process_field_cell(pl, cell):
        if cell.is_mine():
            pl.change_hp(-1)
            cell.empty() 
        elif cell.is_money():
            pl.change_money (random.randrange(30, 60, 1))
            cell.empty()
        elif cell.is_health():
            pl.change_hp(1)
            cell.empty()
        elif cell.is_sweeper():
            pl.change_sweepers(1)
            cell.empty()
            
            
    def get_icon(pl):
        return '♔ '
      
    


    
    
    


    

