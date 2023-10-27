from math import sqrt, sin, cos
import random
import tkinter as tk

dt = 0.1
G = 1


class Particle:
    fx = 0.0
    fy = 0.0
    
    def __init__(self, x0, y0, vx0, vy0, mass, canvas):
        self.x_curr = x0
        self.y_curr = y0
        self.vx_curr = vx0
        self.vy_curr = vy0
        self.m = mass
        r = mass ** 0.15 * 10
        self.shape = canvas.create_oval(x0 - r, y0 - r, x0 + r, y0 + r, fill="green")
    
    def calc_ext_force(self):
        self.ext_fx = 0.0
        self.ext_fy = 0.0
    
    def calc_int_force(self, neighbors):
        self.int_fx = 0.0
        self.int_fy = 0.0
        for neighbor in neighbors:
            r = sqrt((self.x_curr - neighbor.x_curr) ** 2 + (self.y_curr - neighbor.y_curr) ** 2)
            f = G * self.m * neighbor.m / r ** 2
            self.int_fx += f * (neighbor.x_curr - self.x_curr) / r
            self.int_fy += f * (neighbor.y_curr - self.y_curr) / r
    
    def calc_resultant_force(self):
        self.fx = self.ext_fx + self.int_fx
        self.fy = self.ext_fy + self.int_fy
    
    def calc_acceleration(self):
        self.ax_curr = self.fx / self.m
        self.ay_curr = self.fy / self.m
    
    def calc_velocity(self):
        self.vx_next = self.vx_curr + self.ax_curr * dt
        self.vy_next = self.vy_curr + self.ay_curr * dt
    
    def calc_position(self):
        self.x_next = self.x_curr + self.vx_curr * dt
        self.y_next = self.y_curr + self.vy_curr * dt
    
    def update_frame(self, canvas):
        canvas.move(self.shape, self.vx_curr * dt, self.vy_curr * dt)


def main():
    root = tk.Tk()
    CENTER_X = 300
    CENTER_Y = 300
    canvas = tk.Canvas(root, width=2 * CENTER_X, height=2 * CENTER_Y)
    canvas.pack()
    
    N = 1
    CENTER_MASS = 1e4
    
    rdata = [random.uniform(50, 100) for _ in range(N)]
    theta_data = [random.uniform(0, 6.28) for _ in range(N)]
    xdata = [rdata[i] * cos(theta_data[i]) + CENTER_X for i in range(N)]
    ydata = [rdata[i] * sin(theta_data[i]) + CENTER_Y for i in range(N)]
    vdata = [sqrt(G * CENTER_MASS / rdata[i]) for i in range(N)]
    vxdata = [vdata[i] * (CENTER_Y - ydata[i]) / rdata[i] for i in range(N)]
    vydata = [vdata[i] * (xdata[i] - CENTER_X) / rdata[i] for i in range(N)]
    mass_data = [random.uniform(1e-3, 1e-1) for _ in range(N)]
    
    particles = [
        Particle(xdata[i], ydata[i], vxdata[i], vydata[i], mass_data[i], canvas)
        for i in range(N)
    ]
    particles += [Particle(CENTER_X, CENTER_Y, 0.0, 0.0, CENTER_MASS, canvas)]
    
    while True:
        for i in range(len(particles)):
            particles[i].calc_ext_force()
            
            neighbors = [particles[j] for j in range(len(particles)) if j != i]
            particles[i].calc_int_force(neighbors)
            
            particles[i].calc_resultant_force()
            particles[i].calc_acceleration()
            
            particles[i].calc_velocity()
            particles[i].vx_curr = particles[i].vx_next
            particles[i].vy_curr = particles[i].vy_next
            
            particles[i].calc_position()
            particles[i].x_curr = particles[i].x_next
            particles[i].y_curr = particles[i].y_next
        
        for i in range(len(particles)):
            particles[i].update_frame(canvas)
        
        canvas.update()
    
    root.mainloop()


if __name__ == "__main__":
    main()

