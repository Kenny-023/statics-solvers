#This program solves spring triangles.
import numpy as np
origin=0,0,0
#Input parameters: (origin is 0,0,0)
tita=float(input('Enter an angle.(degrees): '))
k=float(input('Enter spring constant.(N/m): '))
l=float(input('Enter length of unstretched spring.(m): '))
c=float(input('Enter distance of spring attachment from origin of bar.(m): '))
f_point=float(input('Enter distance of force from origin of bar.(m): '))

#Vector input paramesium
    #Add a while loop here
b=input('Enter cordinate of spring origin.(i,j,k): ')
b=tuple(map(float, b.split(',')))
b=np.array(b)
f=input('Enter external force on moving arm in the form i,j,k: ')
f=tuple(map(float, f.split(',')))
f=np.array([f])

#Vector handlers
b_arm=np.linalg.norm(b-origin)
try:
    v_offset=(np.pi/2)-np.arctan(b[1]/b[0])
except:
    f=2
#print(v_offset)
#Solver
tita=np.radians(tita)
    #add guard for tita
L=np.sqrt((c**2)+(b_arm**2)-(2*b_arm*c*np.cos(tita)))
F=k*(L-l)
phy=np.arccos(((L**2)+(b_arm**2)-(c**2))/(2*b_arm*L))
alpha=((np.pi/2)-phy) #90 degrees is pi/4
#F_direction=b-np.array([c*np.cos(alpha),c*np.sin(alpha),0])
F_direction=b-np.array([c*np.sin(v_offset+tita),c*np.cos(v_offset+tita),0])
e_direction=F_direction/np.linalg.norm(F_direction)
F_vector=F*e_direction
r_spring=np.array([c*np.sin(v_offset+tita),c*np.cos(v_offset+tita),0])
spring_moment=np.cross(r_spring,F_vector)

#External force
r_force=np.array([f_point*np.sin(v_offset+tita),f_point*np.cos(v_offset+tita),0])
force_moment=np.cross(r_force,f)

print(spring_moment,force_moment)
