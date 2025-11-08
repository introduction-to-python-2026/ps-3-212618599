def approximate_pi(n_terms):
    s=0.0
    for i in range(0,n_terms,1):
        s = s +(((-1)**i)/(2*i +1)) 
    pi= 4*s
    return pi
