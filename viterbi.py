import sys
H=0
T=1
U=2
def largest(phi):
    largest = phi[0]
    for i in phi:
        if i > largest:
            largest = i
    return largest
def viterbi(alpha, beta, pi, data):
#initialization
    p_max =[]
    q_list = []
    phi = []
    j=0
    p=0
    stp1 = pi[0]*beta[0][data[0]]
    stp2 = pi[1]*beta[1][data[0]]
    stp3 = pi[2]*beta[2][data[0]]
    stp4 = pi[3]*beta[3][data[0]]
    p_max.append(stp1)
    p_max.append(stp2)
    p_max.append(stp3)
    p_max.append(stp4)
    if p_max[0] == p:
        q_list.append('1')
    if p_max[1] == p:
        q_list.append('2')
    if p_max[2] == p:
        q_list.append('3')
    if p_max[3] == p:
        q_list.append('4')
    p_max.clear()
#induction
    for i in data:
        if j>0:
            #print(stp1,' ',stp2,' ',stp3,' ',stp4)
            phi.append(stp1*alpha[0][0])
            phi.append(stp2*alpha[1][0])
            phi.append(stp3*alpha[2][0])
            phi.append(stp4*alpha[3][0])
            p_max.append(largest(phi))
            p_max[0]=p_max[0]*beta[0][i]
            phi.clear()

            phi.append(stp1*alpha[0][1])
            phi.append(stp2*alpha[1][1])
            phi.append(stp3*alpha[2][1])
            phi.append(stp4*alpha[3][1])
            p_max.append(largest(phi))
            p_max[1]=p_max[1]*beta[1][i]
            phi.clear()

            phi.append(stp1*alpha[0][2])
            phi.append(stp2*alpha[1][2])
            phi.append(stp3*alpha[2][2])
            phi.append(stp4*alpha[3][2])
            p_max.append(largest(phi))
            p_max[2]=p_max[2]*beta[2][i]
            phi.clear()

            phi.append(stp1*alpha[0][3])
            phi.append(stp2*alpha[1][3])
            phi.append(stp3*alpha[2][3])
            phi.append(stp4*alpha[3][3])
            p_max.append(largest(phi))
            p_max[3]=p_max[3]*beta[3][i]
            phi.clear()

            stp1 = p_max[0]
            stp2 = p_max[1]
            stp3 = p_max[2]
            stp4 = p_max[3]
            p = largest(p_max)
            if p_max[0] == p:
                q_list.append('1')
            if p_max[1] == p:
                q_list.append('2')
            if p_max[2] == p:
                q_list.append('3')
            if p_max[3] == p:
                q_list.append('4')
            p_max.clear()
        j=j+1
    #backtracking
    print(p)
    print(q_list)
    return q_list
#driver
pi = [.25,.25,.25,.25]
data = [H,H,U,T,H,U,U,H,H,U,H,H,H]
a = [[.1,.2,.5,.2],
     [.4,.2,.2,.2],
     [.2,.2,.3,.3],
     [.2,.1,.3,.4]]
b = [[.1,.6,.3],
     [.2,.3,.5],
     [.3,.2,.5],
     [.3,.3,.4]]
viterbi(a,b,pi,data)