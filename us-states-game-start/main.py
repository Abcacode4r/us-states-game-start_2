import turtle
import csv
import pandas

screen=turtle.Screen()
screen.title("Us states game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
states_name=data.state.to_list()
guessed_states= []
while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50: Guess the state.",
                                    prompt="What's another states name?").title()
    if answer_state=="Exit":
        missing_states=[]
        for state in states_name:
            if state not in guessed_states:
                missing_states.append(state)
        df=pandas.DataFrame(missing_states)
        df.to_csv("missing_states")
        print(missing_states)
        break
    if answer_state in states_name:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())









