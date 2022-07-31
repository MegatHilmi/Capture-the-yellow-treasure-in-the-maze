#Part 1: Setting Up The Maze
import math                           # Able to make a complex mathematical calculation
import turtle                         # The turtle module provides turtle grpahic primitives
import numpy as np                    # Able to use large, multidimensional arrays and matrices


wn = turtle.Screen()                  # This function is used to return the list of turtles on the screen
wn.bgcolor("black")                   # Set the background colour with black
wn.title("A Maze Game")               # Put the title of the pop up with "A Maze Game"
wn.setup(700,700)                     # This method is used to set the sized and position of the main window
wn.tracer(0)                          # Will render the game much faster
current_row_location = 0              # Set the current row location with 0
current_column_location = 0           # Set the current column location with 0


# Create Pen class
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)  
        self.shape("square")          # Set the wall shape with square
        self.color("white")           # Set the wall colour with white
        self.penup()                  # Turtle are able to move around the screen, but will not draw 
        self.speed(0)                 # Animation controls how quickly the turtle turns and moves (0 means the fastest)

# Create Player class
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")          # Set the player shape with square
        self.color("blue")            # Set the player colour with blue
        self.penup()
        self.speed(0)

    def is_collision(self, other):                  # Creating is_collision function if player collide with treasure
        a = self.xcor() - other.xcor()              # This is x coordinate player minus with coordinate of treasure
        b = self.ycor() - other.ycor()              # This is x coordinate player minus with coordinate of treasure
        distance = math.sqrt((a ** 2) + (b ** 2))   # To calculate the distance player

        if distance < 5:              # If distance less than 5
            return True               # return true (Already collide)
        else:
            return False              # return false (Not collide yet)

# Create Treasure class
class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")          # Set the treasure shape with circle
        self.color("gold")            # Set the treasure colour with gold
        self.penup()
        self.speed(0)
        self.goto(x,y)                # The treasure will move based on x and y value

    def destroy(self):                # Create destroy function
        self.goto(2000,2000)          # There is no destroy function in turtle, so what we do we move it out of the screen
        self.hideturtle()             # This function is to make the turtle invisible

# Create Red Treasure class
class Red_Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")          # Set the red treasure shape with circle
        self.color("red")             # Set the treasure colour with red
        self.penup()
        self.speed(0)
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

# Create Green Treasure class
class Green_Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")          # Set the green treasure shape with circle
        self.color("Green")           # Set the treasure colour with green
        self.penup()
        self.speed(0)
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

levels = [""]                         #Create levels list

level_1 = [                           # Create the maze in 2D array consist of characters
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXX          XXXXX",
    "XR XXXXXXX  XXX XX  XXXXX",
    "X  G        XXX XX  XXXXX",
    "X       XX              X",
    "X XXXX  XX  XXX         X",
    "X XXXX  XX  XXX XX  XX  X",
    "X XXXX GXX    X XX  G   X",
    "X  XXX          XXT XX  X",
    "X  XXXRRXXXXXXXXXXRGXX  X",
    "X        R              X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"   
]



environment_rows = len(level_1)             # define the environment rows       
environment_columns = len(level_1[1])       # Define the environment columns

# Create a 3D numpy array to hold the current Q-values for each state and action pair: Q(s, a) 
# The array contains environment rows and enviroment columns (to match the shape of the environment), as well as a third "action" dimension.
# The "action" dimension consists of 4 layers that will allow us to keep track of the Q-values for each possible action in.
# Each state (see next cell for a description of possible actions). 
# The value of each (state, action) pair is initialized to 0.
q_values = np.zeros((environment_rows, environment_columns, 4))

# Define actions
# Numeric action codes: 0 = up, 1 = right, 2 = down, 3 = left
actions = ['up', 'right', 'down', 'left']

# Initialize the rewards with -1
rewards = np.full((environment_rows, environment_columns), -1.)

for y in range(len(level_1)):
        for x in range (len(level_1[y])):
            #NOTE the orderof y and x in the next line
            character = level_1[y][x]         # Get the character at each x,y coordinate

            if character == "X":              # Check if it is an X (representing wall)
                rewards[y][x] = -100          # The reward list will be set to -100

            if character == "T":              # Check if it is a T (representing Treasure)
                rewards[y][x] = 100           # The reward list will be set to 100  

            if character == "R" or character == "G":    # Check if it is a G and R (representing green treasure and red treasure)
                rewards[y][x] = -30                     # The reward list will be set to -30

treasures = []                                # Define a treasures list

levels.append(level_1)                        # Add maze to maze list


#Create Level Setup Function
def setup_maze(level,current_row_location,current_column_location):
    for y in range(len(level)):
        for x in range (len(level[y])):
            #NOTE the orderof y and x in the next line
            character = level[y][x]           # Get the character at each x,y coordinate
            screen_x = -288 + (x * 24)        # Calculate the screen x coordinates
            screen_y = 288 - (y * 24)         # Calculate the screen y coordinates

            if character == "X":                    # Check if it is an X (representing a wall)
                pen.goto(screen_x, screen_y)        # The pen will got to the screen based in the coordinate given
                pen.stamp()
                walls.append((screen_x, screen_y))  # Add coordinates to wall list

            if character == "P":                    # Check if it is a P (representing the player)
                current_row_location = screen_y     # Get the y coordinate in screen 
                current_column_location = screen_x  # Get the x coordinate in screen
                player.goto(screen_x, screen_y)

            if character == "T":                                    # Check if it is a T (representing Treasure)
                treasures.append(Treasure(screen_x,screen_y))       # Store the coordinate of the treasure in the treasure list

            if character == "R":                                    # Check if it is a R (representing Red Treasure)
                others.append(Red_Treasure(screen_x,screen_y))      # Store the coordinate of the treasure in the other list

            if character == "G":                                    # Check if it is a T (representing  Green Treasure)
                others.append(Green_Treasure(screen_x,screen_y))    # Store the coordinate of the treasure in the other list

    return current_row_location,current_column_location             # Return the current x and y coordinate of player
    

def get_next_action(current_row_index, current_column_index, epsilon):          # Create the get next action function
    if np.random.random() < epsilon:                                              # If a randomly chosen value between 0 and 1 is less than epsilon, 
        return np.argmax(q_values[current_row_index, current_column_index])         # Then choose the most promising value from the Q-table for this state.
    else:             
        return np.random.randint(4)    

def get_next_location(current_row_index, current_column_index, action_index):   # Define a function that will get the next location based on the chosen action
    move_to_y = 0                                                               # Initialize the move_to_y with 0
    move_to_x = 0                                                               # Initialize the move_to_x with 0
    new_row_index = current_row_index                                           # set new_row_index with the current player's row coordinate
    new_column_index = current_column_index                                     # set new_column_index with the current player's column coordinate

    if actions[action_index] == 'up':                                           # This part will be chosen if the action index is 0
        new_row_index -= 1                                                      # Row coordinate will be minus with 1
        move_to_x = player.xcor()                                               # Get current x coordinate in environment
        move_to_y = player.ycor() +24                                           # Get the current y coordinate in the environment with by moving up
        player.goto(move_to_x,move_to_y)                                        # Move the new location to display the player

    elif actions[action_index] == 'right':                                      # This part will be chosen if the action index is 1
        new_column_index += 1                                                   # Column coordinate will plus with 1
        move_to_x = player.xcor() +24                                           # Get the current x coordinate in the environment with by moving right
        move_to_y = player.ycor() 
        player.goto(move_to_x,move_to_y)

    elif actions[action_index] == 'down':                                       # This part will be chosen if the action index is 2
        new_row_index += 1                                                      # Row coordinate will be plus with 1
        move_to_x = player.xcor()
        move_to_y = player.ycor() -24                                           # Get the current y coordinate in the environment with by moving down
        player.goto(move_to_x,move_to_y)

    elif actions[action_index] == 'left':                                       # This part will be chosen if the action index is 3
        new_column_index -= 1                                                   # Column coordinate will be minus with 1
        move_to_x = player.xcor() -24                                           # Get the current x coordinate in the environment with by moving right
        move_to_y = player.ycor() 
        player.goto(move_to_x,move_to_y)

    return move_to_y,move_to_x                                                  # Return the latest coordinate of the player


def coordinatetranslation(y,x):                                                 # this coordinate tranlation function used to translate from environment coordinate to the 2D array coordinate
    new_y = -1 * ((y-288)/24)
    new_x = ((x + 288)/24)
    return int(new_y),int(new_x)                                                # Return the x and y translated coordinate


def startGame(current_row_location,current_column_location,counter,epsilon):                                                                # This function is to start the AI playing game
    row,column = setup_maze(levels[1],current_row_location,current_column_location)                                                         # Setup the environment and display it 
    current_row_location,current_column_location = coordinatetranslation(row,column)                                                        # Translate the environment coordinate

    while len(treasures) != 0:                                                                                                              # This loop will keep going until the agent found the yellow treasure
        action_index = get_next_action(current_row_location, current_column_location, epsilon)                                              # Call the get_next_action function 
    
        #perform the chosen action, and transition to the next state (i.e., move to the next location)
        old_row_location, old_column_location = current_row_location, current_column_location                                                # Store the old row and column indexes
        row1,column1 = get_next_location(current_row_location, current_column_location, action_index)                                        # Get the new environment coordinate after call the get_next_location function
   
        current_row_location,current_column_location = coordinatetranslation(row1,column1)                                                   # Translate the row1 and column1 coordinate
        reward = rewards[current_row_location,current_column_location]                                                                       # Receive the reward for moving to the new state 
        old_q_value = q_values[old_row_location,old_column_location,action_index]                                                            # Get the old Q value from previous state
        temporal_difference = reward + (discount_factor * np.max(q_values[current_row_location,current_column_location])) - old_q_value      # calculate the temporal difference

        #update the Q-value for the previous state and action pair
        new_q_value = old_q_value + (learning_rate * temporal_difference)                                                                    # Calculate the Q value
        q_values[old_row_location,old_column_location,action_index] = new_q_value                                                            # Update the Q value for previous state and action pair

        wn.tracer(0)                                                # Will render the game much faster
        for treasure in treasures:
            if player.is_collision(treasure):                       # To check whether player already collide with treasure or not
                print ("Treasure has already been captured.")
                treasure.destroy()                                  # Destroy the treasure
                treasures.remove(treasure)                          # Remove the treasure from the trerasure list
                break                                               # Break the while loop

        if(reward < -20):                                           # Check whether the player get reward less than -20 in that state (already collide with wall, red treasure or green treasure)
            print("reward = ",reward)
            break                                                   # Break the while loop to start new episode


        if counter == 500:                                          # If the player already move 500 steps without collide with wall, red treasure or greean treasure and also not capture the yellow treasure
            break                                                   # Break the while loop

        counter += 1                                                # Add counter with 1 for each player step
        wn.update()                                                 # To update the display environment 



#the robot is allowed to travel without colliding with wall, red treasure, or green treasure
def get_shortest_path(current_row_location,current_column_location):                                        # Define a function that will get the shortest path between player location to the yellow treasure
    row,column = setup_maze(levels[1],current_row_location,current_column_location)                         # Setup the environment for the testing
    current_row_location,current_column_location = coordinatetranslation(row,column)

    while len(treasures) != 0:
        action_index = get_next_action(current_row_location, current_column_location, 1.)
        row1,column1 = get_next_location(current_row_location, current_column_location, action_index)
        current_row_location,current_column_location = coordinatetranslation(row1,column1)

        wn.tracer(0) 
        for treasure in treasures:
            if player.is_collision(treasure):
                print ("Treasure has already been captured.")
                treasure.destroy()                                                                           # Destroy the treasure
                treasures.remove(treasure)                                                                   # Remove the treasure from the treasure list
        
        wn.update()
    print("test is finish")


#Create class instances
pen = Pen()
player = Player()


#create wall coordinate list
walls = []

#create others treasures
others = []

#define an epsilon greedy algorithm that will choose which action to take next (i.e., where to move next)
#define training parameters
epsilon = 0.9                                                                       # The percentage of time when we should take the best action (instead of a random action)
discount_factor = 0.9                                                               # Discount factor for future rewards
learning_rate = 0.9                                                                 # The rate at which the AI agent should learn

for episode in range(600):                                                         # Run through hundreds of time training episodes
    counter = 0
    print("episode = ",episode)
    print("\n")
    startGame(current_row_location,current_column_location,counter,epsilon)         # Start the training
print('Training complete!')


start_the_game = input("Are you ready to start the game? [y/n]:")                   # Ask the user to display the shortest path
if(start_the_game == "y"):
    print("start the test")
    get_shortest_path(0,0)

print("The tests are completed.")