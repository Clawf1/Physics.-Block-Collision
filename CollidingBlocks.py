from vpython import *

mass_1 = 1
mass_2 = 10000
velocity_1 = 0
velocity_2 = -50
side = 2
dt = 0.00001


def velocity_after_block_collision(m_1, m_2, v_10, v_20):
    v_1 = (2 * m_2 * v_20 + v_10 * (m_1 - m_2)) / (m_1 + m_2)
    v_2 = (2 * m_1 * v_10 + v_20 * (m_2 - m_1)) / (m_1 + m_2)
    return v_1, v_2


def velocity_after_wall_collision(v_10):
    return -v_10



scene = canvas(
    title='Collisions', x=0, y=0, width=1000, height=300, center=vector(0, 0, 0), background=color.black, fov=0.05)
floor = box(pos=vector(0, -10.5, 0), length=50, height=1, width=5, color=color.white)
wall = box(pos=vector(-25.5, -6, 0), length=1, height=10, width=5, color=color.white)


block_1 = box(pos=vector(0, -8, 0), length=2 * side, height=2 * side, width=2 * side, color=color.red)
block_1.velocity = vector(velocity_1, 0, 0)
block_2 = box(pos=vector(23, -8, 0), length=2 * side, height=2 * side, width=2 * side, color=color.green)
block_2.velocity = vector(velocity_2, 0, 0)


collision_label = label(pos=vector(0, 8, 0), color=color.white, linecolor=color.black)
velocity_1_label = label(pos=vector(0, 5, 0), color=color.red, linecolor=color.black)
velocity_2_label = label(pos=vector(0, 2, 0), color=color.green, linecolor=color.black)


collision_count = 0
time = 0
rate_count = 0


while True:
    rate(20000)

    if block_2.pos.x - side < block_1.pos.x + side:
        velocity_1, velocity_2 = velocity_after_block_collision(
            mass_1, mass_2, velocity_1, velocity_2
        )
        block_1.velocity.x = velocity_1
        block_2.velocity.x = velocity_2
        collision_count += 1

    if block_1.pos.x - side <= wall.pos.x + 0.5:
        velocity_1 = velocity_after_wall_collision(velocity_1)
        block_1.velocity.x = velocity_1
        collision_count += 1

    block_1.pos += block_1.velocity * dt
    block_2.pos += block_2.velocity * dt

    if block_2.pos.x > 25:
        block_2.visible = False

    if block_1.pos.x > 25:
        block_1.visible = False

    if velocity_2 > velocity_1 >= 0:
        rate_count += 1
        if rate_count == 20000:
            break

    time += dt

    collision_label.text = f'Collisions: {collision_count}'
    velocity_1_label.text = f'Velocity 1: {block_1.velocity.x:.2f} m/s'
    velocity_2_label.text = f'Velocity 2: {block_2.velocity.x:.2f} m/s'
