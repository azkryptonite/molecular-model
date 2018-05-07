# -*- coding: utf-8 -*-
"""
Created on Sun Aug 07 18:09:09 2016

@author: Administrator
"""

import math

R = 9.0055
r = 0.9945
maxNballs=0

a = math.acos(((R+r)**2-2*r**2)/(R+r)**2) # a is the polar angel of every xy plane

a=math.asin(r/(R+r)) # this is easier and more proper
Ntrials=100
for itrial in range(Ntrials) :  # callculate for all offsets to find the optimal packing of balls

    offset=float(itrial)/Ntrials * 2*a

    lista=[] ;
    matrix = [] # a matrix to store the coordinates
    lista = [R + r] 
    i = 0 # i means layer on the xy plane, if i equals zero, then it means the equater 


    # m = math.floor((math.pi / 2)/a ) # m means number of layers between north pole and the equater
    m = math.floor(math.pi / a ) # m means number of layers between north and south pole 

    cita = offset # initial polar angle of the ith layer
    
    while (cita <= math.pi ):  # i means the ith x-z plane
        
        cita = offset + i * a  # the polar angle of the ith layer
        
        #print a, cita, (R+r)* math.sin(cita)

        if ( (R+r)* math.sin(cita)>= r): # if you can put another ball on the ith plane

            lista = [(R+r), cita ] # the radius and the polar of the balls on the plane is fixed


            b = math.acos((((R+r) *math.sin(cita))**2 - 2*r**2)/((r+R) * math.sin(cita))**2) # the angel between two balls in the same plane if connected with each other
            
            #print b

            h = 0

            while (h * b <= 2 * math.pi - b):

                # the hth ball on the ith plane, this  condition is the cnstraints of the balls
                h += 1

            c = 2 * math.pi / h  # the angel between two balls on the same x-y plane

            k = 0

            while (k * c <= 2* math.pi - b  ):


                ph = k * c # the azimuth angle of the jth ball on the ith x-z plane


                lista.append(ph) # add the azimuth angle to the cordinate list 

                matrix.append (lista) # put the coordinates in the matrix 

                lista = [(R+r), cita] # remove the azimuth angle of the jth ball

                k += 1 # to he (j+1)th ball
            lista = [(R+r)] # when finish the ith plane, make both polar and azimuth angle to zero

            i += 1 # to the (i+1)th x-z plane


        else: # just put one ball on the plane where there is no way to put another ball

            citapole=math.pi * round (cita/math.pi)  # find to which pole should we put the ball
            
            lista = [R+r, citapole, 0]
            
            matrix.append(lista)
            lista=[(R+r)]
            i+=1
        i += 1
        
        cita = offset + i * a  # the polar angle of the ith layer: need to define here so that while loop doesn't go to far

    if (len(matrix) >= maxNballs) :   # check if this trial offset is the best
        maxNballs=len(matrix)
        bestmatrix=matrix ;
        bestoffset=offset
        

print(maxNballs)
print(bestoffset)
  
f = open("datafile.xyz", "w")   

f.write(str(len(bestmatrix)) + '\n')
f.write('\n')
for n in range(len(bestmatrix)):
    
    x = bestmatrix[n][0] *math.sin(bestmatrix[n][1])* math.cos(bestmatrix[n][2])
    y = bestmatrix[n][0] *math.sin(bestmatrix[n][1])* math.sin(bestmatrix[n][2])
    z = bestmatrix[n][0] *math.cos(bestmatrix[n][1])
    f.write(str(1)+" "+ str(x) + " " + str(y) + " " + str(z) +" \n")
 

f.close()
