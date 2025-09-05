from matplotlib import pyplot as plt
from matplotlib import animation
from random import uniform


class Particle:
    __slots__ = ("x","y","ang_vel")

    def __init__(self, x, y, ang_vel):

        self.x = x
        self.y = y
        self.ang_vel = ang_vel      #Angular velocity - decides the rotation direction

    

class ParticleSimulator:
    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 1e-4
        nsteps = int(dt/timestep)

        for i in range(nsteps):
            #calculate direction
            for p in self.particles:
                norm = (p.x ** 2 + p.y ** 2) ** 0.5
                v_x = -p.y / norm
                v_y = p.x / norm
            
                #calculate displacement
                d_x = timestep * p.ang_vel * v_x
                d_y = timestep * p.ang_vel * v_y

                p.x += d_x
                p.y += d_y



def visualize(simulator):
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure(figsize=(8,8))
    # ax = plt.subplot(111,aspect = 'equal')
    # line, = ax.plot(X, Y, 'ro')
    # line, = plt.plot(X, Y, 'o')   
    # print(plt.plot(X, Y, 'o'))
    line, = plt.plot(X, Y)   
    # print(plt.plot(X, Y))
    print(line)
    plt.axis([-1,1,-1,1])
    # plt.xlim = (-1, 1)
    # plt.ylim = (-1, 1)

    
    def init():
        line.set_data([], [])
        return line,        #comma is important!  <- Same as idx 0

    def animate(i):
        simulator.evolve(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]  
        print(max(X))
        print(max(Y))


        line.set_data(X, Y)         
        return line,               

    anim = animation.FuncAnimation(fig=fig,
                                   func=animate,
                                   init_func=init,
                                   blit=True,
                                   interval=10)
    plt.show()

def test_visualize():
    particles = [Particle(0.3,0.5,1),
                 Particle(0.0,-0.5,-1),
                 Particle(-0.1,-0.4,3)]
    simulator = ParticleSimulator(particles=particles)
    visualize(simulator=simulator)


def test_evolve():
    particles = [Particle(0.3,0.5,1),
                 Particle(0.0,-0.5,-1),
                 Particle(-0.1,-0.4,3)]
    simulator = ParticleSimulator(particles)

    simulator.evolve(0.1)

    p0, p1, p2 = particles

    def fequal(a, b, eps=1e-5):
        return abs(a-b) < eps
    
    assert fequal(p0.x, 0.210269)
    assert fequal(p0.y, 0.543863)


    assert fequal(p1.x, -0.099334)
    assert fequal(p1.y, -0.490034)

    assert fequal(p2.x, 0.191358)
    assert fequal(p2.y, -0.365227)

def benchmark():
    particles = [Particle(uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0))
                          for i in range(1000)]

    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)



if __name__ == '__main__':
    # test_visualize()
    # test_evolve()
    benchmark()
