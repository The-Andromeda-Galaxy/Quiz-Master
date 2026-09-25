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
    screen.draw.textbox(question[0].strip(),question_box, color = "#4D5146", shadow = (0.5,0.5),scolor = "white")
    index = 1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(),answer_box,color = "#2D302A")
        index = index+1

def move_marquee():
    marque_box.x = marque_box.x - 2
    if marque_box.right < 0:
        marque_box.left = WIDTH

def update():
    move_marquee()

def read_question_file():
    global question_count, questions
    q_file = open(question_file_name,"r")
    for question in q_file:
        questions.append(question)
        question_count = question_count + 1
    q_file.close()

def read_next_question():
    global question_index
    question_index = question_index+1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                game_over()
        index = index + 1
    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score,timer_left, questions,question
    score = score + 1
    if questions:
        question = read_next_question()
        timer_left = 10
    else:
        game_over()

def game_over():
    global question,timer_left,is_game_over
    msg = f"Game Over - Correct Answers:{score}"
    question = [msg,"-","-","-","-",5]
    timer_left = 0
    is_game_over = True

def skip_question():
    global is_game_over, question, timer_left
    if questions and not is_game_over:
        question = read_next_question()
        timer_left = 10
    else:
        game_over()

def update_time_left():
    global timer_left
    if timer_left:
        timer_left = timer_left-1
    else:
        game_over()

read_question_file()
question = read_next_question()
clock.schedule_interval(update_time_left,1)
pgzrun.go()