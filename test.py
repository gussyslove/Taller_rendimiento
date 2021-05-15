from time import time
import cy_simulator
import simulator


def run_simulator(simulator):
    AU = (149.6e6 * 1000)
    sun = simulator.Body()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10**30

    earth = simulator.Body()
    earth.name = 'Earth'
    earth.mass = 5.9742 * 10**24
    earth.px = -1 * AU
    earth.vy = 29.783 * 1000

    venus = simulator.Body()
    venus.name = 'Venus'
    venus.mass = 4.8685 * 10**24
    venus.px = 0.723 * AU
    venus.vy = -35.02 * 1000

    simulator.loop([sun, earth, venus])


def main():
    start_time = time()
    run_simulator(simulator)
    end_time=time()
    time_python=end_time-start_time
    print("Execution time (python)="+str(time_python))
    start = time()
    run_simulator(cy_simulator)
    end_time=time()
    time_cython=end_time-start
    print("Execution time (cython)="+str(time_cython))
    speedUp = round(time_python/time_cython, 3)
    print("speedUp="+str(speedUp))
if __name__ == '__main__':
    main()
