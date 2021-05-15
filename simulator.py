#!/usr/bin/env python3

import math

G = 6.67428e-11

AU = (149.6e6 * 1000) 
SCALE = 250 / AU

class Body():

    name = 'Body'
    mass = None
    vx = vy = 0.0
    px = py = 0.0

    def attraction(self, other):

        if self is other:
            raise ValueError("Attraction of object %r to itself requested"
                             % self.name)

        sx, sy = self.px, self.py
        ox, oy = other.px, other.py
        dx = (ox-sx)
        dy = (oy-sy)
        d = math.sqrt(dx**2 + dy**2)

        if d == 0:
            raise ValueError("Collision between objects %r and %r"
                             % (self.name, other.name))

        f = G * self.mass * other.mass / (d**2)

        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        return fx, fy


def loop(bodies):

    timestep = 24*3600 

    step = 1

    while (step <= 365 * 1000):
        step += 1

        force = {}
        for body in bodies:
            total_fx = total_fy = 0.0
            for other in bodies:
                if body is other:
                    continue
                fx, fy = body.attraction(other)
                total_fx += fx
                total_fy += fy

            force[body] = (total_fx, total_fy)

        for body in bodies:
            fx, fy = force[body]
            body.vx += fx / body.mass * timestep
            body.vy += fy / body.mass * timestep

            body.px += body.vx * timestep
            body.py += body.vy * timestep



def main():
    sun = Body()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10**30

    earth = Body()
    earth.name = 'Earth'
    earth.mass = 5.9742 * 10**24
    earth.px = -1*AU
    earth.vy = 29.783 * 1000      

    venus = Body()
    venus.name = 'Venus'
    venus.mass = 4.8685 * 10**24
    venus.px = 0.723 * AU
    venus.vy = -35.02 * 1000

    loop([sun, earth, venus])


if __name__ == '__main__':
    main()
