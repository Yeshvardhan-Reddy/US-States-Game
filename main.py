import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States  Game")
screen.setup(height=500, width=740)

image = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")
screen.addshape(image)
turtle.shape(image)

loc = turtle.Turtle()
loc.ht()
loc.penup()

us_states = data.state.to_list()
user_states = []

while len(user_states) < 50:
    user = screen.textinput(title=f"{len(user_states)}/50 Guess State", prompt="Guess another state")
    try:
        answer = user.title()
        state = data[data.state == answer]

        if answer in str(state):
            user_states.append(answer)
            x_cor = int(state.x)
            y_cor = int(state.y)
            loc.goto(x_cor, y_cor)
            loc.write(answer, align="left", font=("Courier", 10, "bold"))

        if answer == "Exit":
            missed_states = [state for state in us_states if state not in user_states]
            learn = pandas.DataFrame(missed_states)
            learn.to_csv("states_to_learn.csv")
            break
    except AttributeError:
        missed_states = [state for state in us_states if state not in user_states]
        learn = pandas.DataFrame(missed_states)
        learn.to_csv("states_to_learn.csv")
        break
    except TypeError:
        pass

if len(user_states) > 40:
    screen.clear()
    loc.goto(0, 0)
    loc.write("You guessed over 40 states. Congrats! You are a Champ!!", align='center', font=("Courier", 24, "bold"))

screen.exitonclick()
