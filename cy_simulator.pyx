#cython: language_level=3

cimport cython

cdef extern from "math.h":
    double cos(double x) nogil
    double sin(double x) nogil
    double atan2(double x, double y) nogil
    double sqrt(double x) nogil
    double pow(double x, double y) nogil

cdef double G = 6.67428e-11

cdef class Body(object):

    cdef public double vx, vy, px, py, mass
    cdef public str name

    def __init__(Body self):
        self.name = 'Body'
        self.mass = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.px = 0.0
        self.py = 0.0

    @cython.cdivision(True)
    cdef tuple attraction(Body self, Body other):
        cdef double fx, fy

        if self is other:
            raise ValueError("Attraction of object %r to itself requested"
                             % self.name)

        sx, sy = self.px, self.py
        ox, oy = other.px, other.py
        dx = (ox-sx)
        dy = (oy-sy)
        d = sqrt(dx**2 + dy**2)

        if d == 0:
            raise ValueError("Collision between objects %r and %r"
                             % (self.name, other.name))

        cdef double f = G * self.mass * other.mass / pow(d,2)

        theta = atan2(dy, dx)
        fx = cos(theta) * f
        fy = sin(theta) * f
        return fx, fy

@cython.cdivision(True)
def loop(list bodies):

    cdef int timestep = 24*3600  # One day

    cdef int step = 1

    cdef double total_fx, total_fy, fx, fy

    cdef dict force

    cdef Body body, other

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