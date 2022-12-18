import numpy as np
import inference
import sys





### making some fake data to work with
num_genes = 20
num_samps = 100


genes = []
samps = []


for i in range(1,num_genes+1):
    genes.append(f"G{i}")

for i in range(1,num_samps+1):
    samps.append(f"sample{i}")


## expression data, rows are genes and columns are samples
data = np.random.rand(num_genes,num_samps)









### testing correlation

# edges = inference.correlation(data)
# print(edges)
# print(edges.shape)

# edges = inference.correlation(data,signed=0)
# print(edges)
# print(edges.shape)

# [edges,p_values] = inference.correlation(data,get_p_value=True)
# print(p_values)
# print(p_values.shape)


### testing linear regression

# edges = inference.linear_regression(data)
# print(edges)
# print(edges.shape)




## testing output writing
edges = inference.linear_regression(data)
inference.write_output(genes,edges,filename="test_output/test.csv")
inference.write_output(genes,edges,filename="test_output/test.tsv",filetype="tsv")