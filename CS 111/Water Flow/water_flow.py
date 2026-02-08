"""
 an engineer must design the system and ensure water 
 will flow to all buildings in the city. An engineer 
 must choose the tower height, pipe type, pipe diameter, 
 and pipe path. Engineers use software to help them make 
 these choices and design a working water distribution 
 system.

 Write a Python program that could help an engineer 
 design a water distribution system. During this prove 
 milestone, you will write three program functions and 
 three test functions as described in the Steps section 
 below.
"""

def water_column_height(tower_height, tank_height):
    height = tower_height + (3/4)*(tank_height)
    return height

def pressure_gain_from_water_height(height):
    pressure = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height)/1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    loss = (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2)/(2000 * pipe_diameter)    
    return loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    loss = (-.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings)/2000
    return loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    reynolds = (WATER_DENSITY * hydraulic_diameter * fluid_velocity)/WATER_DYNAMIC_VISCOSITY
    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    constant = (.1 + (50/reynolds_number)) * (((larger_diameter/smaller_diameter)**4) - 1)
    loss = (-constant * WATER_DENSITY * fluid_velocity**2)/2000
    return loss

def kPa_to_psi(pressure):
    psi = pressure/6.895
    return psi

EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = .0010016

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

    psi = kPa_to_psi(pressure)
    print(f"Pressure at house: {pressure:.1f} kilopascals or {psi:.1f} psi")
    
    with open('water_flow.txt', 'w') as file_object:
        print(f"tower height = {tower_height}", file=file_object)
        print(f"tank height = {tank_height}", file=file_object)
        print(f"length of pipes from tank to lot = {length1}", file=file_object)
        print(f"number of 90 degree angles in supply pipe = {quantity_angles}", file= file_object)
        print(f"length of pipe from supply to house = {length2}", file= file_object)
        print(f"Pressure at house: {pressure:.1f} kilopascals or {psi:.1f} psi",file=file_object)


if __name__ == "__main__":
    main()