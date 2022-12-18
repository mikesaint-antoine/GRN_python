import numpy as np
import scipy.stats







def correlation(data, get_p_value=False, signed=1 ):
    # data shape: [genes, samples]

    N = data.shape[0]
    # number of genes

    edges = np.zeros(shape=(N,N))

    if get_p_value:
        p_values = np.zeros(shape=(N,N))


    for i in range(N):
        for j in range(i+1,N):
            cor, p_value = scipy.stats.pearsonr(data[i,:],data[j,:])

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






def linear_regression(data, get_p_value=False, get_signs=False ):
    # data shape: [genes, samples]

    from sklearn.linear_model import LinearRegression


    N = data.shape[0]
    # number of genes

    edges = np.zeros(shape=(N,N))


    for i in range(N):
        for j in range(N):
            if i != j:
                x = data[i,:].reshape(-1, 1)
                y = data[j,:]
                model = LinearRegression()
                model.fit(x, y)
                r_sq = model.score(x, y)

                edges[i,j] = r_sq




    return(edges)