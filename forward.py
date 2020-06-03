import sys
H=0
T=1
U=2
def forward(alpha, beta, pi, data):
#initializtion
    lststp1 = pi[0]*beta[0][data[0]]
    lststp2 = pi[1]*beta[1][data[0]]
    lststp3 = pi[2]*beta[2][data[0]]
    lststp4 = pi[3]*beta[3][data[0]]
    j=0
#induction
    for i in data:
        if j > 0:
            #print(lststp1,' ',lststp2,' ',lststp3,' ',lststp4)
            stp1 = (lststp1*alpha[0][0]+lststp2*alpha[1][0]+lststp3*alpha[2][0]+lststp4*alpha[3][0])*beta[0][data[j]]
            stp2 = (lststp1*alpha[0][1]+lststp2*alpha[1][1]+lststp3*alpha[2][1]+lststp4*alpha[3][1])*beta[1][data[j]]
            stp3 = (lststp1*alpha[0][2]+lststp2*alpha[1][2]+lststp3*alpha[2][2]+lststp4*alpha[3][2])*beta[2][data[j]]
            stp4 = (lststp1*alpha[0][3]+lststp2*alpha[1][3]+lststp3*alpha[2][3]+lststp4*alpha[3][3])*beta[3][data[j]]
            lststp1 = stp1
            lststp2 = stp2
            lststp3 = stp3
            lststp4 = stp4
        j=j+1
    #termination
    print("forward algorithm:")
    print(lststp1+lststp2+lststp3+lststp4)
#driver
pi = [.25,.25,.25,.25]
data=[H,H,U,T,H,U,U,H,H,U,H,H,H]
a = [[.1,.2,.5,.2],
     [.4,.2,.2,.2],
     [.2,.2,.3,.3],
     [.2,.1,.3,.4]]
b = [[.1,.6,.3],
     [.2,.3,.5],
     [.3,.2,.5],
     [.3,.3,.4]]
forward(a,b,pi,data)