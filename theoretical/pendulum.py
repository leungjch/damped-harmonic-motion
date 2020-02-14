import pygame
import math
class Pendulum:
    def __init__(self, initx, inity, mass, k, myC, myP, myA, STEPS):

        # CONSTANTS FOR DRAG FORCE
        self.C = myC    # Drag coefficient. For a flat perpendicular plate, we use ~1.28.
        self.p = myP    # Air density.
        self.A = myA    # Cross sectional area.

        # position
        self.x = initx
        self.y = inity
        self.mass = mass

        # acceleration
        self.a_x = 0
        self.a_y = 0
        
        # velocity
        self.v_x = 0
        self.v_y = 0
        
        # Tension force
        self.T_x = 0
        self.T_y = 0 
        self.k = k

        # Net force
        self.Fnet_x = 0
        self.Fnet_y = 0

        # For Euler integration
        self.steps = STEPS;
        self.delta = 1/STEPS

        # Misc
        self.lastColour = (0,0,0) # Colour of the last magnet it was pulled into
        self.xlist = []
        self.ylist = []

    def update(self, WIDTH, HEIGHT, isStationary):

        #width, height = pygame.display.get_surface().get_size() # Get screen heigth and width
        #width, height = pygame.display.get_surface().get_size() # Get screen heigth and width
        width = WIDTH
        height = HEIGHT
        # Calculate tension (Hookes law: F_T = kx where x is distance from center)
        self.T_x = 0
        self.T_y = self.k * (height/2-self.y)

        # Calculate drag force
        self.D_x = 0
        self.D_y = ((1.0/2.0)*self.C*self.p*self.A*pow(self.v_y,2))*math.copysign(1,self.v_y)*(-1)
        #print(self.v_y)
        # Calculate gravitational force
        self.G_x = 0
        self.G_y = 9.81 * self.mass
        
        # Calculate net force
        self.Fnet_x = self.T_x + self.G_x + self.D_x
        self.Fnet_y = self.T_y + self.G_y + self.D_y
        # Calculate acceleration (Fnet=ma)
        self.a_x = self.Fnet_x/self.mass
        self.a_y = self.Fnet_y/self.mass
        self.E_k = (1/2)*self.mass*pow(self.v_y,2)
        self.E_p = self.G_y*(abs(height/2-self.y))

        # Euler integration
        #for i in range(self.steps):
        self.v_x += self.a_x*self.delta       
        self.v_y += self.a_y*self.delta
        

        
        self.x += self.v_x *self.delta 
        self.y += self.v_y *self.delta 
            
  
        # Calculate kinetic and potential energy
        ##print("Kinetic:", self.E_k)
        ##print("Potential:", self.E_p)
        ##print("Total:", self.E_k+self.E_p)
        
        #print("v" + str(self.v_x))
        #print("Fnet" + str(self.Fnet_x))
        #print("T" + str(self.T_x))
        #print("M" + str(self.M_x))
        #print("A" + str(self.a_x))
        #print("S" + str(self.x))
        #print(self.x)
        #if abs(self.Fnet_x) > 1:
        #    print("here")
        #self.xlist.append(self.x)
        #self.ylist.append(self.y)
        return isStationary
        #for i in range(len(self.xlist)):
        #    screen.set_at((int(self.xlist[i]), int(self.ylist[i])), (0,0,0))

    
