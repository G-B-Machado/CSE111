EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016

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
    return WATER_DENSITY*9.80665*height/1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """calculates the loss pressure from the pipe
    Parameter:
        all float numbers: pipe_diameter, pipe_length, friction_factor, fluid_velocity
    Return: the direct results from the formula
    """
    return -friction_factor*pipe_length*WATER_DENSITY*(fluid_velocity**2)/(2000*pipe_diameter)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """calculates the loss pressure from the fittings
    Parameter:
    all float numbers: fluid_velocity, quantity_fittings
    Return: the direct results from the formula
    """
    return -0.04*WATER_DENSITY*(fluid_velocity**2)*quantity_fittings/2000

def reynolds_number (hydraulic_diameter, fluid_velocity):
    """calculates the reynolds_number
    Parameter:
    all float numbers: hydraulic_diameter, fluid_velocity
    Return: the direct results from the formula
    """
    return WATER_DENSITY*hydraulic_diameter*fluid_velocity/WATER_DYNAMIC_VISCOSITY 

def pressure_loss_from_pipe_reduction (larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    k = (0.1+50/reynolds_number)*(((larger_diameter/smaller_diameter)**4)-1)
    print(k)
    return -k*WATER_DENSITY*(fluid_velocity**2)/2000

def convert_kpa_to_psi(pressure):
    """Compute the conversion of kpa to psi
    Parameter:
    The pressure
    Return: the direct results from the formula
    """
    return pressure * 0.14503773773020923

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {convert_kpa_to_psi(pressure):.1f} psi")


if __name__ == "__main__":
    main()