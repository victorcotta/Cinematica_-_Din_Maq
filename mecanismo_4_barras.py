#####################################################
#Título: MECANISMO DE 4 BARRAS EM CONFIGURAÇÃO ABERTA
#####################################################
#Author: Victor Sidnei Cotta
#####################################################
#Disciplina: Cinemática e Dinâmica das Máquinas
#####################################################
#Professor: Doutor Lúcio Patrício
#####################################################
#Data: 23/09/22
#####################################################


import math as m

#Medidas dos Links:
L1 = 105
L2 = 30
L3 = 80
L4 = 70

#Medida do ângulo THETA 2:
theta_2 = 60.0

#Cálculos realizados:
z = m.sqrt((L1**2) + (L2**2) - (2*L1*L2*m.cos(theta_2*m.pi/180.0)))
alpha = (180*m.acos(((z**2) + (L4**2) - (L3**2))/(2*z*L4))/m.pi)
beta = (180*m.acos(((z**2) + (L1**2) - (L2**2))/(2*z*L1))/m.pi)
gamma = (180*m.acos(((z**2) - (L3**2) - (L4**2))/(-2*L3*L4))/m.pi)
theta_4 = (180 - (alpha + beta))
theta_3 = (180 - (gamma + alpha + beta))

#Valores encontrados no mecanismo:
print ("A valor de Z é  ",round(z, 1,))
print ("O ângulo ALPHA vale ",round(alpha, 1))
print ("O ângulo BETA vale ",round(beta, 1))
print ("O ângulo GAMMA vale ",round(gamma, 1))
print ("O ângulo THETA 2 vale " ,round(theta_2, 1))
print ("O ângulo THETA 3 vale " ,round(theta_3, 1))
print ("O ângulo THETA 4 vale ",round(theta_4, 1))






