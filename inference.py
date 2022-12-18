import numpy as np
import scipy.stats
import sys






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




def write_output(genes, edges, filename="output.csv",filetype="csv"):
    ## default is CSV
    
    from operator import itemgetter


    to_write = []

    for i in range(edges.shape[0]):
        for j in range(edges.shape[1]):
            if i != j:
                to_write.append([genes[i],genes[j],edges[i,j]])



    to_write = sorted(to_write, key=itemgetter(2), reverse=True)


    if filetype=="csv":

        with open(filename, "w") as record_file:
            for i in range(len(to_write)):

                record_file.write(f"{to_write[i][0]},{to_write[i][1]},{to_write[i][2]}\n")

    elif filetype=="tsv":

        with open(filename, "w") as record_file:
            for i in range(len(to_write)):

                record_file.write(f"{to_write[i][0]}\t{to_write[i][1]}\t{to_write[i][2]}\n")


    
