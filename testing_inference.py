import numpy as np
import inference






### making some fake data to work with
num_genes = 20
num_samps = 100


genes = []
samps = []


for i in range(1,num_genes+1):
    genes.append(f"G{i}")

for i in range(1,num_samps+1):
    samps.append(f"sample{i}")


## expression data, rows are genes and columsn are samples
data = np.random.rand(num_genes,num_samps)









### testing correlation

edges = inference.correlation(data)

print(edges)
print(type(edges))
print(edges.shape)