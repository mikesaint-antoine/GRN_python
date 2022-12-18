import numpy as np
import scipy.stats







def correlation(data, get_p_value=False, get_signs=False ):
    # [genes, samples]

    if get_signs:
        edges = np.zeros(shape=(data.shape[0],data.shape[0]))
        signs = np.zeros(shape=(data.shape[0],data.shape[0]))

        # correlation
        for i in range(data.shape[0]):
            for j in range(i+1,data.shape[0]):
                cor, p_value = scipy.stats.pearsonr(data[i,:],data[j,:])
                # dot product in numerator, euclidian norm in denomenator

                if get_p_value:
                    edges[i,j] = p_value
                    edges[j,i] = p_value
                else:
                    edges[i,j] = cor
                    edges[j,i] = cor

                if cor >=0:
                    signs[i,j] = 1
                else:
                    signs[j,i] = -1

        return(edges,signs)
    
    else:
        edges = np.zeros(shape=(data.shape[0],data.shape[0]))

        # correlation
        for i in range(data.shape[0]):
            for j in range(i+1,data.shape[0]):
                cor, p_value = scipy.stats.pearsonr(data[i,:],data[j,:])
                # dot product in numerator, euclidian norm in denomenator

                if get_p_value:
                    edges[i,j] = p_value
                    edges[j,i] = p_value
                else:
                    edges[i,j] = abs(cor)
                    edges[j,i] = abs(cor)

        return(edges)    