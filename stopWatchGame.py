# "Stopwatch: The Game"
import simplegui
# define global variables
counter = 0
tries = 0
wins = 0
percent = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t // 600
    b = (t // 100) % 6
    c = (t // 10) % 10
    d = t % 10
    
    return str(a) + ":" + str(b) + str(c) + "." + str(d) 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global tries, wins, percent
    
    if timer.is_running():
        timer.stop()
        
        tries += 1
        if counter % 10 == 0:
            wins += 1
    
    percent = wins * 100 // tries
    
        
def reset():
    global tries, counter, percent, wins
    tries = 0
    counter = 0
    percent = 0
    wins = 0
    timer.stop()
   

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1
    return counter

# define draw handler
def draw(canvas):
    global percent, tries
    canvas.draw_text(format(counter), (110, 110), 45, "Yellow")
    
    if tries > 0:
            
            if percent <= 25:
                canvas.draw_text(update(), (0, 25), 25, "Red")
            
            elif percent >= 75:
                canvas.draw_text(update(), (0, 25), 25, "Green")
                
            else:
                canvas.draw_text(update(), (0, 25), 25, "White")
            

def update():
    global tries, wins
    return str(wins) + "/" + str(tries)

def quit():
    frame.stop()
    
# create frame
frame = simplegui.create_frame("Watch game", 300, 200)
# register event handlers
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
button1 = frame.add_button('Start', start, 100)
button2 = frame.add_button('Stop', stop, 100)
button3 = frame.add_button('Reset', reset, 100)
label1 = frame.add_label('')
button4 = frame.add_button('Quit', quit, 100)

# start frame
frame.start()


