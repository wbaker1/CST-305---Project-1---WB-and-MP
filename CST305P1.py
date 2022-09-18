#CST-305 Project 1 - Matthew Powers and Wesley Baker 
#This project is a first-order differential equation that is modeling GPU temperature cooling down after running an application requiring a lot of performance and it's effect given the room's temperature. Based off of Newton's Law of Cooling.

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# initial condition
y0 = 155

# function that returns dy/dt
def model(y, t, T):
    # k = (1/time waited)*ln((temp at end of time-room Temp)/(start temmp-room temp)) kept 74 as base temp as we were unable to simulate extreme temperatures accuratly
    k = -(1/5)*np.log((107.6-74)/(y0-74))
    dydt = -k*(y-T)
    return dydt


# time points
t = np.linspace(0,60,100)

# solve ODE for y1 with respect to k
T = 99
y1 = odeint(model,y0,t, args=(T,))

# plot result of y1
plt.plot(t,y1,'y-', label='Room Temperature = ' + str(T) + 'ºF')

# solve ODE for y2 with respect to k
T = 74
y2 = odeint(model,y0,t, args=(T,))

# plot result of y2
plt.plot(t,y2,'r-', label='Room Temperature = ' + str(T) + 'ºF')

# solve ODE for y3 with respect to k
T = 37
y3 = odeint(model,y0,t, args=(T,))

# plot result of y3
plt.plot(t,y3,'b-', label='Room Temperature = ' + str(T) + 'ºF')

# solve ODE for y4 with respect to k
T = 27
y4 = odeint(model,y0,t, args=(T,))

# plot result of y4
plt.plot(t,y4,'g-', label='Room Temperature = ' + str(T) + 'ºF')


# label neccessary info on graph
plt.title('GPU cooling based off room temp in ºF')
plt.xlabel('Time (minutes)')
plt.ylabel('Temperature (ºF)')
plt.legend()
# Display the graph
plt.show()
