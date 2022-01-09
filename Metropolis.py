# Randomly pick a starting point ~x.
N  = dimension of vector x

# counter for number of sampling 
sample = 0
# add evaluted Q(x) each time
total_Q = 0
historyX = []

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
        xdash[ind] = x[ind] + random number between 0 and 1
    Pxdash = exp(-E(xdash)/KBT)/Z #calculate P(x')

    pacc = 0
    if Pxdash >= Px:
        pacc = 1
    else:
        pacc = Pxdash/Px
        
    # generate a random number between 0 and 1 to decide whether accept the xdash 
    resultx = x
    posibility = random number between 0 and 1 
    if posibility<pacc:
        x = xdash
    
    # evaluate Q(x)
    return Q(x),x


    



# • Repeatedly use the Metropolis algorithm to select a sample point.
# – Make a small trial step/change in the parameters to get ~x0
# .
# – Calculate P(~x0
# ) and P(~x). Accept or reject step using
# pacc =
# 1 if P(~x0
# ) ≥ P(~x)
# P(~x0
# )/P(~x) if P(~x0
# ) < P(~x)
# (11.34)
# If accepted ~x = ~x0
# , else ~x = ~x.
# – Evaluate Q(~x) and add to running total PQ (and PQ2
# if necessary).
# • (Repeat whole process for a series of different starting points.)
# • Divide through by the total number of samples to get hQi.