import csv
import turtle
import glob
import os


def graphical_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return t, wn, map_bg_img


def track_storm():
    """Animates the path of the storm.
    """
    (t, wn, map_bg_img) = graphical_setup()


    # your code above this
    # without the final call to wn.exitonclick() in main,
    # the background image will not be displayed
    # also need to return map_bg_img so that it is not garbage collected
    return t, wn, map_bg_img


def main():
    (t, wn, map_bg_img) = graphical_setup()

    storm_name = 'data\\' + input('Enter storm name:') + '.csv'
    storm_data = glob.glob('data/*')
    try:
        val = open(storm_name, 'r').readlines()
        val.pop(0)
        for x in val:
            subset = x.split(',')
            latitude = float(subset[2])
            longitude = float(subset[3])
            wind = int(subset[4])
            t.pendown()
            t.goto(longitude, latitude)
            if 74 <= wind <= 95:
                t.width(2)
                t.color('blue')
                t.write(1)
            elif 96 <= wind <= 110:
                t.width(3)
                t.color('green')
                t.write(2)
            elif 111 <= wind <= 129:
                t.width(7)
                t.color('yellow')
                t.write(3)
            elif 130 <= wind <= 156:
                t.width(11)
                t.color('orange')
                t.write(4)
            elif wind >= 157:
                t.width(15)
                t.color('red')
                t.write(5)
            else:
                t.width(1)
                t.color('white')
    except:
        print('Invalid storm name')
        exit(0)
    # also you'll need to fix the call below so that it calls
    # the track_storm function
    # wn, map_bg_img = track_storm(...)

    # the line below needs to be the last line of main()
    # you'll need to get the wn from track_storm
    wn.exitonclick()


if __name__ == "__main__":
    main()
