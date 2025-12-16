#This solver finds unknown forces with known direction supporting a structure.
import numpy as np
w=np.array([3,5,4])#Test initialization
forces=[]
moments=[]
u_location=[] #Unknown force location
u_moments=[] #Moments due to unknown force unit vector
count=np.array([[0,0,0]])
forces.append(count)
moments.append(count)
counter=0

#Origin handler(origin is handled by 'arm'
        
while True:
    while True:
        try:
            #Unknown forces
            e=input('Enter force unit vector in the form i,j,k: ')
            l=input('Enter force location in the form i,j,k: ')
            e=tuple(map(float, e.split(',')))
            l=tuple(map(float, l.split(',')))
            e=np.array(e)
            test=e*w #This prevents entering [3,2,5,6] error.
            l=np.array(l)
            test=l*w #w is for testing
            break
        except:
            print('Please enter a number. eg: 3, 4.5, 7')
    try:
        u_location.append(l)
        arm=l-np.array(u_location)[0]
        u_moment=np.cross(arm,e)
        #if counter>0:
        u_moments.append(u_moment)
        #print(moments)
        counter=counter+1
    except:
        print('Please enter a complete vector. eg: 3, 4.5, 7')

    esc=input("When done type 'done' to end session. Otherwise click any button to add unknown force.")
    esc=esc.lower()
    if esc=='done': break
    else: continue

while True:
    while True:
        try:
            #Known forces:
            u=input('Enter force in the form i,j,k: ')
            r=input('Enter force location in the form i,j,k: ')
            u=tuple(map(float, u.split(',')))
            r=tuple(map(float, r.split(',')))
            u=np.array([u])
            test=u*w #This prevents entering [3,2,5,6] error.
            r=np.array([r])
            test=r*w
            break
        except:
            print('Please enter a number. eg: 3, 4.5, 7')
    try:
        r=r-np.array(u_location)[0]
        moment=np.cross(r,u)
        forces.append(u)
        moments.append(moment)
        #print(moments)
    except:
        print('Please enter a complete vector. eg: 3, 4.5, 7')
    esc=input("When done type 'done' to end session. Otherwise click any button to add force.")
    esc=esc.lower()
    if esc=='done': break
    else: continue

#List to array converter   
forces=np.array(forces)
forces=np.squeeze([forces])
moments=np.array(moments)
moments=np.squeeze(moments)
F_net=np.array([[np.sum(forces[0:,0]),np.sum(forces[0:,1]),np.sum(forces[0:,2])]]).T
M_net=np.array([[np.sum(moments[0:,0]),np.sum(moments[0:,1]),np.sum(moments[0:,2])]]).T
A=np.array(u_moments).T
coun=-1
for col in A:
    coun=coun+1
    if np.sum(col)==0:
        zero=coun
A[zero]=[1,1,1]
B=-M_net
coun=-1
for col in B:
    coun=coun+1
    if np.sum(col)==0:
        zero=coun
B[zero]=np.sum(-F_net)
print('The unknown forces are: \n',np.linalg.solve(A,B))
