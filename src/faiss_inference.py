import faiss
import numpy as np
from faiss.contrib.ondisk import merge_ondisk

from utils import fvecs_read, ivecs_read

print("loading query vectors...")
xq = fvecs_read("../gist/gist_query.fvecs")

index = faiss.read_index("../faiss/populated.index")
index.nprobe = 80
k = 5

print(f"getting nearest neighbors for {xq.shape[0]} vectors...")
distances, indices = index.search(xq, k)

# Simple benchmark of the quality of the search
iqt = ivecs_read("../gist/gist_groundtruth.ivecs")

print("Top1 accuracy on the 1-NN search: ", np.mean(indices[:, 0] == iqt[:, 0]))
