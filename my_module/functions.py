#!/usr/bin/env python
# coding: utf-8

# In[21]:


import random

import time

const = {

    'head_char' : '@', 

    'body_char' : '0', 

    'grid_char' : '*',

    'food_char' : 'F',
    
    'pois_char' : 'P',

    'time'      : 0.3, 

    'def_board' : 6,
    
    'pTime'     : 5,
    
    'input_message' : 'Enter w,a,s,d to move: ',
    
    'invalid_message' : 'Enter a valid command...',
    
    'win_message'  : 'You Won Son!',
    
    'death_message' : 'You Died Loser... Final Score: ',
    
    'hit_top_left'  : 'From running into top/left...',
    
    'hit_top_right' : 'From running into bottom/right...',
    
    'ate_yourself' : 'cause u ate urself',
    
    'ate_poison'   : 'Ate poison',

    }




class snake():
    """
    This is the class for the snake that will make the snake of the game.
    
    Attributes: 
        def_board(int) = the size of the board/grid.
    """

    previous_tail = [const['def_board'] - 1,const['def_board'] - 1]
 

    def __init__(self):
        """The constructor of the snake."""

        start = [0,0]

        self.pos = [start]

 
    def make_move(self, direct):
        
        """
        Used for the movement of the Snake.
        
        Parameters:
            direct(string): Makes the snake move. 
        """

        next_move = self.get_move(direct)

 
        #checks whether move was valid
        if next_move == 'Not Valid':

            return next_move

        #if move was valid then snake is in a new position
        else:

            self.pos.insert(0, next_move)

            self.previous_tail = self.pos.pop()

            return
    
 
    def eat(self):
        """
        Function that lets the snake eat the food/poison on the grid
        
        """

        copy = self.pos[len(self.pos) - 1]

        self.pos.append(copy)
 

    def get_head(self):
        """Returns the position of the head of the snake."""

        return self.pos[0]


    def get_tail(self):
        """Returns the position of the previous_Tail of the snake."""

        return self.previous_tail

 
    def get_neck(self):
        """Returns the position of the Neck of the snake if the lenght of 
        the position is greater than 1."""

        if len(self.pos) > 1:

            return self.pos[1]


        return

    
    def get_move(self, direction):
        """
        Control system that defines the movement of the snake.
        
        Parameter:
            direction = applies the direction entered by the player.
        
        """

        new_cord_x = self.get_head()[0]

        new_cord_y = self.get_head()[1]

        new_cord = [new_cord_x, new_cord_y]

 
        #allows player to move up
        if direction == 'w':

            new_cord[1] -= 1

 
       #allows player to move down
        elif direction == 's':

            new_cord[1] += 1

 
       #allows player to move left
        elif direction == 'a':

            new_cord[0] -= 1

 
       #allows player to move right
        elif direction == 'd':

            new_cord[0] += 1

 
       #if player does not make a valid move returns "Not Valid"
        else:

            return 'Not Valid'

 
        #returns the new location of the snake
        return new_cord

 
    def print_snake(self):
        """makes the snake visible on the grid."""

        for i in self.pos:

            print(i[0])

            print(i[1])

    
class grid():
    """
    The grid class will make the grid of the game.
    
    Attributes:
    
        size = arbitrary value 0 is set. Refers to the size of the grid
    
        game_grid = empty list. based on list the grid will be implemented
        
    """

    size = 0

    game_grid = []

 
    def __init__(self, board_size):
        """
        The constructor for the board.
        
        Parameters:
            board_size(int) = defines the size of the board.
        
        """

        size = 0

        self.game_grid = []

 
        #makes the columns of the board
        while size < board_size:

            row = []

            self.size = 0

 
            #makes the rows of the board
            while self.size < board_size:

                row.append(const['grid_char'])

                self.size += 1


            self.game_grid.append(row)

            size += 1

        
        self.game_grid[0][0] = const['head_char']

        self.game_grid[int(const['def_board']/2)][int(const['def_board']/2)]=const['food_char']
        
        self.game_grid[int(const['def_board']/4)][int(const['def_board']/4)]=const['pois_char']

 
    def print_grid(self):
        """Prints the grid of the game."""

        print('\n'.join([' '.join(it) for it in self.game_grid]))

 
    def change_char_h(self, x, y):
        """
        Changes the char of the head.
        
        Parameters:
            x(int) = the x-coordinate of the head.
            y(int) = the y-coordinate of the head.
            
        """

        self.game_grid[y][x] = '@'


    def change_char_b(self, x, y):
        """
        Changes the char of the body.
        
        Parameters:
            x(int) = the x-coordinate of the body.
            y(int) = the y-coordinate of the body.
            
        """

        self.game_grid[y][x] = '0'


    def change_char_g(self, x, y):
        """
        Changes the char of the grid.
        
        Parameters:
            x(int) = the x-coordinate of the grid.
            y(int) = the y-coordinate of the grid.
    
        """

        self.game_grid[y][x] = '*'

 
    def change_char_f(self, x, y):
        """
        Changes the char of the food.
        
        Parameters:
            x(int) = the x-coordinate of the food.
            y(int) = the y-coordinate of the food.
            
        """

        self.game_grid[y][x] = 'F'
    
   
    def change_char_p(self, x, y):
        """
        Changes the char of the poison
        
        Parameters:
            x(int) = the x-coordinate of the poison.
            y(int) = the y-coordinate of the poison.
        
        """
        
        self.game_grid[y][x] = 'P'

 
class game_manager():
    """
    This is the class which manages the functioning of the game.
    
    Attributes:
        g_board = size of the grid the game is played on.
        pSnake = the snake that the players control.
        food_Coord = starting location of the food.
        pois_Coord = starting location of the poison.
        wait_Time = duration until food reappears on the board.
        p_Wait_Time = duration until poison reappears on the board.
        player_Score = keeps track of the score.
        frame_Counter = counter for the class.
        
    """

    g_board = grid(const['def_board'])

    p_snake = snake()

    food_coord = [int(const['def_board'] / 2),int(const['def_board'] / 2)]
    
    pois_coord = [int(const['def_board']/4), int(const['def_board']/4)]

    wait_time = -1
    
    p_wait_time = -5

    player_score = 0

    frame_counter = 0

    
    def play_game(self):
        """Condition for winning the game."""

        #if player gets the maximum possible score he wins
        if self.player_score >= const['def_board']**2 -1:

            print(const['win_message'])

            quit()
            
            
        was_valid = True

        print(self.player_score)

        self.update_board()

        self.g_board.print_grid()

        
        #input takes in the direction the player wants to travel
        move = input(const['input_message'])

 
        #wait time food is on the grid
        if self.wait_time > 0:

            self.wait_time -= 1
            
        #wait time the poison is on the grid  
        if self.p_wait_time > 0:
            
            self.p_wait_time -= 1

        #if the player makes an invalid move the game tells the player
        if self.p_snake.make_move(move) == 'Not Valid':

            print(const['invalid_message'])

            was_valid = False

        
        #this declares that the player has died
        if was_valid and not self.check_alive():

            print(const['death_message'], self.player_score)

            return            

        
        #the following two if statements are for the food to spawn and respawn
        #after the wait time the food will respawn in a new location
        if was_valid and self.check_ate_food():

            self.player_score += 1

            self.wait_time = 1
        

        if was_valid and self.wait_time == 0:

            self.wait_time = -1

            self.spawn_food()

            self.g_board.change_char_f(self.food_coord[0], self.food_coord[1])
    
    
        #the following two if statements are for poison to spawn and respawn
        #after the wait time the poison will respawn in a new location   
        if was_valid and self.p_wait_time < 0:
            
            self.p_wait_time += 1
            
            
        if was_valid and self.p_wait_time == 0:
           
            self.p_wait_time = -5
            
            self.spawn_poison()
            
            self.g_board.change_char_p(self.pois_coord[0],self.pois_coord[1])
 

        self.play_game()
        
        
    def check_alive(self):
        """This function checks whether the player is still alive"""

        head = self.p_snake.get_head()

        
        #tells player their are running into the top/left wall
        if head[0] < 0 or head[1] < 0:

            print(const['hit_top_left'])

            return False

 
        #tells player they are running into the bottom/right wall
        elif head[1] >= self.g_board.size or head[0] >= self.g_board.size:

            print(const['hit_top_right'])

            return False
        
 
        #tells player that they ran into themselves
        elif self.check_ate_yourself():

            print(const['ate_yourself'])

            return False
        
        
        #tells the player that they ate poison
        elif self.check_ate_poison():
            
            print(const['ate_poison'])
            
            return False

 

        return True
 

    def check_ate_yourself(self):
        """
        This function checks whether the player ate himself,i.e, 
        ran into themselves.
        
        """
        

        for i in self.p_snake.pos:

 

            if self.p_snake.pos.count(i) > 1:

                return True

 

        return False


    def check_ate_food(self):
        """"This function checks whether the player ate the food."""
        
        
        #if the position of the head is same as position of the food
        if self.p_snake.get_head() == self.food_coord:

            self.p_snake.eat()

            return True


        return False

    
    def check_ate_poison(self):
        """This function checks whether the player ate the poison."""
        
        
        #if the positino of the head is same as the position of the poison
        if self.p_snake.get_head() == self.pois_coord:
            
            return True
        
        return False
                           

    def spawn_food(self):
        """ 
        Randomly spawns the new food on the grid.
        
        """

        valid = False

        #gives the new x-coordinate and y-coordinate of new food on the grid.
        while not valid:

            n_loc_x = random.randint(0,const['def_board'] - 1)

            n_loc_y = random.randint(0,const['def_board'] - 1)

            n_loc = [n_loc_x, n_loc_y]


            if not self.p_snake.pos.count(n_loc)>0 and not n_loc==self.pois_coord:

                valid = True
                       

                       
        self.food_coord = n_loc
    
    
    def spawn_poison(self):
        """
        Randomly spawns new poison on the grid.
        
        """
        
        valid = False
        
        #gives the new x-coordinate and y-coordinate of the new poison on the grid.
        while not valid:
            
            new_loc_x = random.randint(0, const['def_board'] - 1)
            
            new_loc_y = random.randint(0, const['def_board'] - 1)
            
            new_loc = [new_loc_x, new_loc_y]
            
            
            if not self.p_snake.pos.count(new_loc) > 0:
                
                valid = True
                
        self.pois_coord = new_loc
        
    def update_board(self):
        """
        This function Updates the game board after evey round.
        
        """

        face = self.p_snake.get_head()

        tail = self.p_snake.get_tail()

        self.g_board.change_char_h(face[0],face[1])

        self.g_board.change_char_g(tail[0],tail[1])
        

        if len(self.p_snake.pos) > 1:

            second = self.p_snake.get_neck()

            self.g_board.change_char_b(second[0],second[1])

