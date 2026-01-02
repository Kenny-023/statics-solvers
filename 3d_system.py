#This is a general solver for 3D Rigid Body Static Equilibrium.It finds unknown forces and reactions on various support types. functionality for finding couples created by suoport will soon be added.
import numpy as np
#Global variables
while True: #Origin loop
    try:
        origin=input('Enter pivot point in the form i,j,k: ')
        origin=tuple(map(float, origin.split(',')))
        origin=np.array([origin])
        break
    except:
        print('Please enter a vector in the correct form. eg: 3, 4.5, 7') #Will be replaced with a loop.
known_moment_list=np.array([])
sun_moment_list=np.array([]) #Semi-unknokwn support moments
un_forces_list=np.array([]) #Unknown support forces
un_moment_list=np.array([]) #Moments due to unknown forces of supports

#Function calls
def moment_about_point(location,force,origin): #Moment function.
    moments=[]
    r=location-origin #r is the moment arm.
    moment=np.cross(r,force)
    return moment

def input_function(): #This function accepts inputs of single or multiple vectors.
    U=[] #list of u inputs
    V=[] #list of v inputs
    w=np.array([3,4,6]) #This array prevents errors. The numbers are arbitrary.
    while True:
        while True:
            try:
                u=input('Enter location of force in the form i,j,k: ')
                v=input('Enter force vector in the form i,j,k: ')     
                u=tuple(map(float, u.split(',')))
                v=tuple(map(float, v.split(',')))
                u=np.array(u)
                test=u*w #This prevents entering [3,2,5,6] error.
                v=np.array(v)
                test=v*w #w is for testing
                break
            except:
                print('Please enter a number. eg: 3, 4.5, 7')
        U.append(u)
        V.append(v)
        esc=input("When done type 'done' to end session. Otherwise click any button to add unknown force.")
        esc=esc.lower()
        if esc=='done': break
        else: continue
    return(U,V) #This returns a LIST of arrays. To change to array, use np.array()

def unknown_force_handler(e,l,origin): #This function takes in existing components of support 'e', location of support 'l' and desired pivot point of system 'origin'
    un_forces=[] #Forces due to unknown force unit vector
    un_moment=[]
    for i in range(len(e)): #This for loop corrects when you enter numbers other than 0 or 1 in the unknown forces
        if e[i]!=0:
            e[i]=1
    arm=l-origin
    unma=np.zeros(9).reshape(3,3)
    unma[0,0],unma[1,1],unma[2,2]=e[0],e[1],e[2]
    for force in unma: #Unknown matrix
        if force[0]==0 and force[1]==0 and force[2]==0: continue
        else: un_forces.append(force)
    for forces in unma: #Unknown matrix
        un_moments=np.cross(arm,forces)
        if forces[0]==0 and forces[1]==0 and forces[2]==0: continue
        else: un_moment.append(un_moments)
    return(np.squeeze(np.array(un_moment)),np.squeeze(np.array(un_forces)))

#Execution part.
print('These are the forces with known magnitude and direction:')
location_list,force_list=input_function()
known_force_list=np.array(force_list)

print('Thes are forces with unknown magnitude but known direction. Enter unit vector of force: ')
sun_location_list,sun_force_list=input_function()
sun_force_list=np.array(sun_force_list)

for location,force in zip(location_list,force_list):
    moment=moment_about_point(location,force,origin)
    known_moment_list=np.append(known_moment_list, moment)

for location,force in zip(sun_location_list,sun_force_list):
    moment=moment_about_point(location,force,origin)
    sun_moment_list=np.append(sun_moment_list, moment)

known_moment_list=known_moment_list.reshape(int(len(known_moment_list)/3),3) #This turns it from a 1D array to a nx3 matrix (vector form).
known_moment_net=np.array([[np.sum(known_moment_list[0:,0]),np.sum(known_moment_list[0:,1]),np.sum(known_moment_list[0:,2])]]) #This sums up all individual components for total moment.
known_force_net=np.array([[np.sum(known_force_list[0:,0]),np.sum(known_force_list[0:,1]),np.sum(known_force_list[0:,2])]]) #This sums up all individual components for total force.

sun_moment_list=sun_moment_list.reshape(int(len(sun_moment_list)/3),3) #This turns it from a 1D array to a nx3 matrix (vectorform).
sun_force_list=np.array(sun_force_list)

#Unknown forces part:
print('These are forces with unknown magnitude and direction. Enter reaction component in the form i,j,k (1 for existing and 0 for no reaction)')
L,E=input_function()     
for e,l in zip(E,L): #'e' are components and 'l' is location.
    un_moment,un_forces=unknown_force_handler(e,l,origin)
    un_moment_list=np.append(un_moment_list, un_moment)
    un_forces_list=np.append(un_forces_list, un_forces)

un_moment_list=un_moment_list.reshape(int(len(un_moment_list)/3),3)
un_forces_list=un_forces_list.reshape(int(len(un_forces_list)/3),3)

#Final boss 6x6 matrix AxB=C: B=A(^-1)@C <matrix inversion>
C=np.append(known_force_net.T,known_moment_net.T,axis=0)
a1=np.append(un_moment_list.T,sun_moment_list.T, axis=1)
a0=np.append(un_forces_list.T,sun_force_list.T, axis=1)
A=np.append(a0,a1, axis=0)
A_inv=np.linalg.pinv(A)

B=A_inv@-C #'B' is the unknown solution matrix

#Output
print('The total moment is: ',known_moment_net)
print('The total force is: ', known_force_net)
print('Semi-unknown moments: ', sun_moment_list)
print('Semi_unknown forces: ',sun_force_list)
print('Solution: ', B)