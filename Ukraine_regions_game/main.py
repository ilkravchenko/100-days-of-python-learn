import turtle
import pandas


def find_coordinates(region):
    region_coor = df[df.region == region]
    x_cor = int(region_coor.x.values)
    y_cor = int(region_coor.y.values)

    return x_cor, y_cor


screen = turtle.Screen()
screen.title('Ukraine regions Game')
screen.setup(1200, 800)
screen.tracer(0)
image = 'Kiev_highlighted.gif'
screen.addshape(image)

turtle.shape(image)

game_is_on = True
user_score = 0
FONT = ("Arial", 20, 'normal')
guessed_states = []

df = pandas.read_csv('regions.csv')
names_of_regions = df.region.to_list()

while game_is_on:
    screen.update()
    answer_region = screen.textinput(title=f"{user_score}/25 Guess The Region",
                                     prompt="What's another state's name?").lower()

    if answer_region == 'exit':
        missing_states = [region for region in names_of_regions if region not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Regions_to_learn.csv")
        break
    if answer_region in names_of_regions:
        guessed_states.append(answer_region)
        region = turtle.Turtle()
        region.hideturtle()
        region.penup()
        x, y = find_coordinates(answer_region)
        region.goto(x=x, y=y)
        region.write(answer_region, font=FONT)
        user_score += 1

# Regions to learn.csv