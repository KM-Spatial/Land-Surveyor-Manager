from django.contrib import messages
from django.shortcuts import render, redirect
import math

from requests import request


def join_distance(y_end, y_start, x_end, x_start):
    """
    Calculate the distance between a set of coordinates
    Given 2 Coordinate Pairs each containing Y and X values
    """
    y_dif = float(y_end) - float(y_start)
    x_dif = float(x_end) - float(x_start)
    return math.sqrt(math.pow(y_dif, 2) + math.pow(x_dif, 2))


def join_direction(y_end, y_start, x_end, x_start):
    """
    Calculate the bearing/direction from the start point to the
    end point given two coordinate pairs with X and Y values
    """
    y_dif = float(y_end) - float(y_start)
    x_dif = float(x_end) - float(x_start)
    # Calculate Initial Angle
    angle = math.atan2(y_dif, x_dif)

    # Find the Quadrant

    # 2nd Quad
    if x_dif < 0 < y_dif or x_dif < 0 and y_dif < 0:
        quad = 180

    elif x_dif > 0 > y_dif:
        quad = 360

    else:
        quad = 0

    return math.degrees(angle) + int(quad)


def to_dms(direction):
    """
    convert decimal degrees to deg-min-sec
    based on the Float value of the direction
    """
    degree = int(direction)
    minutes_float = (direction - degree) * 60
    minutes = int(minutes_float)
    seconds = (minutes_float - minutes) * 60

    return degree, minutes, seconds


def polar_calculation(direction, distance, x, y):
    """
    Calculate a polar ...
    Split the direction into Degrees, Minutes and Seconds based on the separator (.)
    Given only the input value of direction in the format deg.min.sec (i.e -> 123.45.21)
    After the direction is split.. then convert it to decimal degrees for calculation preparation
    Calculate the coordinates of the points (X, y)
    """
    direction = direction.split('.', 2)
    # degrees
    deg = direction[0]
    # minutes
    minute = direction[1]
    # seconds
    sec = direction[2]

    # convert into decimal degrees
    dec_deg = int(deg) + (float(minute) / 60) + (float(sec) / 3600)


    # calculate X-Coordinates
    # FIXME: Make sure calculation works well
    x_coordinate = float(x) + (float(distance) * math.degrees(math.cos(dec_deg)))
    y_coordinate = float(y) + (float(distance) * math.degrees(math.sin(dec_deg)))

    return y_coordinate, x_coordinate


# Calculating the Join from Input
def calculate_join(request, form):
    y_start = request.POST.get('y_start')
    x_start = request.POST.get('x_start')
    y_end = request.POST.get('y_end')
    x_end = request.POST.get('x_end')
    # calculate distance
    distance = join_distance(y_end, y_start, x_end, x_start)
    # calculate direction
    direction = join_direction(y_end, y_start, x_end, y_end)
    # convert into DMS
    dms = to_dms(direction)
    # Save to Database
    save_data = request.POST.get('saved')
    if save_data == 'on':
        instance = form.save(commit=False)
        instance.distance = distance
        instance.direction_dd = direction
        instance.direction_deg = dms[0]
        instance.direction_min = dms[1]
        instance.direction_sec = dms[2]
        instance.user = request.user  # Save result to user profile
        instance.save()
        messages.success(request, "Join computation complete and data stored successfully")

    context = {
        'form': form,
        'distance': distance,
        'direction': direction,
        'degree': dms[0],
        'minutes': dms[1],
        'seconds': dms[2]
    }
    return render(request, 'computation/join.html', context)


# User Input for Polar
def calculate_polar(request, form):
    x = request.POST.get('x')
    y = request.POST.get('y')
    direction = request.POST.get('direction')
    distance = request.POST.get('distance')

    # calculate polar
    try:
        polar = polar_calculation(direction, distance, x, y)
        y_coordinate = polar[0]
        x_coordinate = polar[1]
    except:
        messages.warning(request, 'An error occurred while trying to decode the direction input. Please make sure you '
                                  'have entered the direction in the correct format specified (i.e. DDD.MM.SS). Take '
                                  'note of the full-stop to separate Degrees, Minutes and Seconds')
        return render(request, 'error.html')

    # Save to Database
    save_data = request.POST.get('saved')
    if save_data == 'on':
        instance = form.save(commit=False)
        instance.x_coordinate = polar[1]
        instance.y_coordinate = polar[0]
        instance.user = request.user  # Save result to user profile
        instance.save()
        messages.success(request, "Coordinates calculated and stored successfully")

    context = {
        'form': form,
        'y': y_coordinate,
        'x': x_coordinate,
    }

    return render(request, 'computation/polar.html', context)
