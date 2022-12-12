# Chamfer Distance for pyTorch

This is an installable implementation of the Chamfer Distance as a module for pyTorch from [Christian Diller](https://github.com/chrdiller). It is written as a custom C++/CUDA extension.

As it is using pyTorch's [JIT compilation](https://pytorch.org/tutorials/advanced/cpp_extension.html), there are no additional prerequisite steps that have to be taken. Simply import the module as shown below; CUDA and C++ code will be compiled on the first run.

# Update
**I updated the package to use a wrapper around the Pytorch3D package chamfer distance due to some gradients bugs in the original code. Please update to the new version if you face any issues.**


### Requirements
The only requirements are PyTotch and Pytorch3D with cuda support:
  * [PyTorch>=1.1.0](https://pytorch.org/get-started/locally/) 
  * [PyTorch3D with CUDA support](https://github.com/facebookresearch/pytorch3d/blob/main/INSTALL.md) 

### Installation
1. Install PyTorch (>= 1.1.0)
2. Install PyTorch3d gpu version.
```
pip install "git+https://github.com/facebookresearch/pytorch3d.git@stable"
```
3. To install the package simply run the following line:
```
pip install git+'https://github.com/otaheri/chamfer_distance'

```

### Usage
```python
import torch
from chamfer_distance import ChamferDistance as chamfer_dist
import time

p1 = torch.rand([10,25,3])
p2 = torch.rand([10,15,3])

s = time.time()
chd = chamfer_dist()
dist1, dist2, idx1, idx2 = chd(p1,p2)
loss = (torch.mean(dist1)) + (torch.mean(dist2))

torch.cuda.synchronize()
print(f"Time: {time.time() - s} seconds")
print(f"Loss: {loss}")

#...
```

