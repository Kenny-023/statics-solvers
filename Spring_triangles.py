#This program solves spring triangles(2D system). A spring triangle is a system consisting of: Rigid side, movable side pinned to rigid side and a spring connecting the movable side to rigid side making a triangle.
#It calculates moment due to spring an external force when angle between rigid and movable sides are inputed
import numpy as np
origin=0,0,0
#Input parameters: (origin is 0,0,0) and angle measurement starts from +y axis
tita=float(input('Enter an angle.(degrees): ')) #This is angle between fixed and movable side
k=float(input('Enter spring constant.(N/m): '))
l=float(input('Enter length of unstretched spring.(m): '))
c=float(input('Enter distance of spring attachment from origin of bar.(m): ')) #Where spring is hooked to the bar
f_point=float(input('Enter distance of force from origin of bar.(m): ')) #Where force acts on the bar

#Vector input paramesium
    #Add a while loop here
b=input('Enter cordinate of spring origin.(i,j,k): ')
b=tuple(map(float, b.split(',')))
b=np.array(b)
f=input('Enter external force on moving arm in the form i,j,k: ')
f=tuple(map(float, f.split(',')))
f=np.array([f])

#Vector handlers
b_arm=np.linalg.norm(b-origin) #b_arm refers to length of rigid side
try:
    v_offset=(np.pi/2)-np.arctan(b[1]/b[0]) #V offset accounts for deviation of spring origin from vertical.
except:
    f=2 #Honestly cant remember why I did this but it probably does something. Remember to comment on your code so your future self wont be conrfused.
#print("Add this number to your input angle:", v_offset*57.296) #57.296 is conversion factor from radians to degrees
#Solver
tita=np.radians(tita)
    #add guard for tita
L=np.sqrt((c**2)+(b_arm**2)-(2*b_arm*c*np.cos(tita))) #L is length of spring side
F=k*(L-l) #Force due to compression or elongation
phy=np.arccos(((L**2)+(b_arm**2)-(c**2))/(2*b_arm*L)) #Basically angle between rigid and movable side
#alpha=((np.pi/2)-phy) #90 degrees is pi/4 (This line is useless)
#F_direction=b-np.array([c*np.cos(alpha),c*np.sin(alpha),0]) (Useless line as well)
F_direction=b-np.array([c*np.sin(v_offset+tita),c*np.cos(v_offset+tita),0]) #The reason why I measure angles from vertical is to easily derive direction of spring force relative to bar since it changes with angle. The direction is required to find moment.
e_direction=F_direction/np.linalg.norm(F_direction) #Unit vector of F_direction
F_vector=F*e_direction #The force due to spring expressed as a vector
r_spring=np.array([c*np.sin(v_offset+tita),c*np.cos(v_offset+tita),0]) #Moment arm of spring force
spring_moment=np.cross(r_spring,F_vector)

#External force (This part can be modified to accept more forces but im lazy so you do it.)
r_force=np.array([f_point*np.sin(v_offset+tita),f_point*np.cos(v_offset+tita),0]) #The sine and cosines are basically unit vector for moment arm of force.
force_moment=np.cross(r_force,f)

print("Spring's moment: ",spring_moment,'\n',"Moment due to force: ",force_moment,'\n', "actual angle: ",(tita*57.296)+(v_offset*57.296) )
