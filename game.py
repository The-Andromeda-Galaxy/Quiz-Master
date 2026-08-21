import pgzrun

TITLE = "Quiz"
WIDTH= 870
HEIGHT=650

marque_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
timer_box = Rect(0,0,150,150)
skip_box = Rect(0,0,150,330)
score_box = Rect(0,0,150,50)

marque_box.move_ip(0,0)
question_box.move_ip(20,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
timer_box.move_ip(700,100)
skip_box.move_ip(700,270)
score_box.move_ip(700,50)

score = 0
timer_left = 10
question_file_name = "questions.txt"
marquee_msg = ""
is_game_over = False
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
questions = []
question_count = 0 
question_index = 0

def draw():
    global marquee_msg
    screen.clear()
    screen.fill("#5D4157")
    screen.draw.filled_rect(marque_box,"#5D4157")
    screen.draw.filled_rect(question_box,"#C4CBB7")
    screen.draw.filled_rect(timer_box,"#D299C2")
    screen.draw.filled_rect(score_box,"#D299C2")
    screen.draw.filled_rect(skip_box,"#CFD9DF")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"#C4CBB7")

    marquee_msg = f"Welcome to Quiz Master, You are at question {question_index}/{question_count}"
    screen.draw.textbox(marquee_msg,marque_box,color = "white")
    screen.draw.textbox(f"{timer_left}",timer_box, color ="#43233A", shadow = (0.5,0.5),scolor = "white")
    screen.draw.textbox(f"score:{score}",score_box, color = "#511740")
    screen.draw.textbox("SKIP",skip_box,color = "#252A2D", angle = -90)
    screen.draw.textbox("Hello World",question_box, color = "#4D5146", shadow = (0.5,0.5),scolor = "white")
    for answer_box in answer_boxes:
        screen.draw.textbox("hello world",answer_box,color = "#2D302A")

def move_marquee():
    marque_box.x = marque_box.x - 2
    if marque_box.right < 0:
        marque_box.left = WIDTH

def update():
    move_marquee()

pgzrun.go()