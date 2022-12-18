import numpy as np
import scipy.stats







def correlation(data, get_p_value=False, signed=1 ):
    # [genes, samples]


    edges = np.zeros(shape=(data.shape[0],data.shape[0]))

    if get_p_value:
        p_values = np.zeros(shape=(data.shape[0],data.shape[0]))


    for i in range(data.shape[0]):
        for j in range(i+1,data.shape[0]):
            cor, p_value = scipy.stats.pearsonr(data[i,:],data[j,:])
            # dot product in numerator, euclidian norm in denomenator


            if signed:
                edges[i,j] = cor
                edges[j,i] = cor
            else:
                edges[i,j] = abs(cor)
                edges[j,i] = abs(cor)

            if get_p_value:
                p_values[i,j] = p_value
                p_values[j,i] = p_value                

    if get_p_value:
        return(edges,p_values)
    else:
        return(edges)

