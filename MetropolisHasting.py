# Randomly pick a starting point ~x.
N  = dimension of vector x

# counter for number of sampling 
sample = 0
# add evaluted Q(x) each time
total_Q = 0
historyX = []
####
proposal_density = g # a probability density function used as  proposal density that could be chosed according to the question 
sigma = standard diviation of g
####

# choose a new starting point of x when the x is stable
for counter = 0,...,10:
    for i= 0,...,N-1:
        x[i] = random number 
    while True:
        total_Q, updated_x+= metropolis(x)
        historyX.append(updated_x)
        x = updated_x
        sample += 1
        if (historyX[-4]+historyX[-3]+historyX[-2]) - historyX[-1] < 0.01:
            break 

averaged_Q = total_Q/sample

def metropolis(x):
    Px = exp(-(E(x)/KBT))/Z #calculate P(x)
    x_dash = array with dimension N
    for ind = 0,...,N-1:
        # xdash[ind] = x[ind] + random number between 0 and 1
        xdash[ind] = a random point in g with mean = x and standard diviation sigma  # choose the new point by using the proposal density 
    Pxdash = exp(-E(xdash)/KBT)/Z #calculate P(x')

####
    A = (Pxdash/probability of choosing xdash given last point is x )/(Px/probability of choosing x given last point is xdash )
    # the probability is calculated by using the probability density function g with the mean  = the previous point
####

    pacc = 0
    if A >= 1:
        pacc = 1
    else:
        pacc = A
        
    # generate a random number between 0 and 1 to decide whether accept the xdash 
    resultx = x
    posibility = random number between 0 and 1 
    if posibility<pacc:
        x = xdash
    
    # evaluate Q(x)
    return Q(x),x
