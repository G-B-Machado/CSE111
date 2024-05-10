def water_column_height(tower_height, tank_height):
    """Computed the height of water column
    Parameter:
        tower_height: a number that represents a height of tower
        tank_height: a number that represents a height of tank
    Return: the result of the following formula (h = t + 3w/4)
    where tower_height is t and tank_height is w
    """
    return tower_height+(3*tank_height)/4

def pressure_gain_from_water_height(height):
    """calculates the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank.n
    Parameter:
        height: a number that represents a height of the water
    Return: the result of the following formula P = ρgh/1000
    h is the height of the water column in meters
    """
    return 998.2*9.80665*height/1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """calculates the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank.n
    Parameter:
        height: a number that represents a height of the water
    Return: the result of the following formula P = ρgh/1000
    h is the height of the water column in meters
    """
    return -friction_factor*pipe_length*998.2*(fluid_velocity**2)/(2000*pipe_diameter)