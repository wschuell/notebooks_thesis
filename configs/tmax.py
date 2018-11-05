#####classic####
    return 100000

#####medium####
    return 40000

#####test####
    return 1000

#####long####
    return 1000000

#####ultralong####
    return 3000000

#####scaling####
    return max(4.5*{{% N,10 %}}**(1.5)*{{% M,20 %}},20000)

#####scaling_withupperbound####
    return min(max(4.5*{{% N,10 %}}**(1.5)*{{% M,20 %}},20000),1000000)

#####scaling_bigmax####
    return min(max(100*{{% N,10 %}}**(1.5)*{{% M,20 %}},20000),10000000)


#####scaling_100####
    return min(max(5*{{% N,10 %}}**(1.5)*{{% M,20 %}},200),100000)

#####userxp####
    return 50

#####tutorial####
    return 10
