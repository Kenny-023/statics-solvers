import numpy as np
forces=[]
moments=[]
count=np.array([[0,0,0]]) #This is just a guard for origin and moment inputs. Also enables you to bypass np.squeeze and enter only 1 force
forces.append(count)
print('This program simplifies a series of couples and moments into a wrench. Can also be used to find average position of a system of forces')

#Origin handler
while True:
    try:
        o=input('Enter pivot point in the form i,j,k: ')
        o=tuple(map(float, o.split(',')))
        o=np.array([o])
        break
    except:
        print('Please enter a vector in the correct form. eg: 3, 4.5, 7')

#Moment inputs handler#
while True:
        try:
            m=input('Enter moment in the form i,j,k. If there is no included moment enter 0,0,0: ')
            m=tuple(map(float, m.split(',')))
            m=np.array([m])
            m+count
            moments.append(m)
            esc=input("When done type 'done' to stop adding moments. Otherwise click any button to add vector.")
            esc=esc.lower()
            if esc=='done': break
            else: continue
        except:
            print('Please enter a number or vector of correct form. eg: 3, 4.5, 7')

#Main function (force inputs and moment calculations)#
while True:
    while True:
        try:
            u=input('Enter force in the form i,j,k: ')
            r=input('Enter force location in the form i,j,k: ')
            u=tuple(map(float, u.split(',')))
            r=tuple(map(float, r.split(',')))
            u=np.array([u])
            r=np.array([r])
            #c=np.sum(u)
            break
        except:
            print('Please enter a number. eg: 3, 4.5, 7')
    
    #print(c)
    #count=count+1
    #forces.append(u)
    #print(forces)
    try:
        r=r-o
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

#Wrench finder program block#
F_net=np.array([np.sum(forces[0:,0]),np.sum(forces[0:,1]),np.sum(forces[0:,2])])
M_net=np.array([np.sum(moments[0:,0]),np.sum(moments[0:,1]),np.sum(moments[0:,2])])
magnitude=np.sqrt(np.sum(M_net*M_net))
e_m=M_net/magnitude
projection=(np.sum(F_net*e_m))*e_m
M_normal=M_net-projection
arm=np.cross(F_net, M_net)/np.sum(F_net*F_net)

#Final output#
print('Net force: ',F_net)
print('Net moment: ',M_net)
#print(arm)
print('Co-ordinate of net force:', o+arm)

#I need to add origin and moment input functionality then finally a wrench
#converter that tells position of net force from the origin
