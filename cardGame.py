# implementation of card game - Memory

import simplegui
import random

DECK_WIDTH = 800
DECK_HEIGHT = 100

click_1, click_2 = 0, 0

# helper function to initialize globals
def new_game():
    global deck, cards_exposed, turns, states, LENGTH_LIST
    states = 0
    turns = 0
    
    deck = [ i % 8 for i in range(16)]
    LENGTH_LIST = len(deck)
    cards_exposed = [False for i in range(16)]
    
    random.shuffle(deck)
    label.set_text("Turns = " + str(turns))
    

    # define event handlers
def mouseclick(pos):
    # add game state logic here
    global states, turns,cards_exposed, click_1, click_2
    
    card_clicked = int(pos[0] / 50)
     
    if states == 0:
        states = 1
        click_1 = card_clicked
        cards_exposed[click_1] = True
    
    elif states == 1:
        if not cards_exposed[card_clicked]:
            states = 2
            click_2 = card_clicked
            cards_exposed[click_2] = True
            turns += 1
            
    elif states == 2:
        if not cards_exposed[card_clicked]:
            if deck[click_1] == deck[click_2]:
                pass
            else:
                cards_exposed[click_1] = False
                cards_exposed[click_2] = False
        
        click_1 = card_clicked
        cards_exposed[click_1] = True
        states = 1
        
    label.set_text("Turns = " + str(turns))
   
                        
# cards are logically 50x100 pixels in size    
def draw(c):
    for i in range(16):
        if cards_exposed[i]:
            c.draw_text(str(deck[i]), (i * (DECK_WIDTH / LENGTH_LIST) + 10 , DECK_HEIGHT / 2 + 13), 50, "Yellow")
        
        else:
            c.draw_polygon([(i * (DECK_WIDTH / LENGTH_LIST), 0),
                            ((i + 1)*(DECK_WIDTH / LENGTH_LIST), 0),
                            ((i + 1)*(DECK_WIDTH / LENGTH_LIST), DECK_HEIGHT),
                                  (i * (DECK_WIDTH / LENGTH_LIST), DECK_HEIGHT)],
                                  2, "Black", "Green")

  
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


