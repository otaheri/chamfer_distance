# Chamfer Distance for pyTorch

This is an installable implementation of the Chamfer Distance as a module for pyTorch from [Christian Diller](https://github.com/chrdiller). It is written as a custom C++/CUDA extension.

As it is using pyTorch's [JIT compilation](https://pytorch.org/tutorials/advanced/cpp_extension.html), there are no additional prerequisite steps that have to be taken. Simply import the module as shown below; CUDA and C++ code will be compiled on the first run.


### Requirements
The only requirement is PyTotch with cuda support:
  * [PyTorch>=1.1.0](https://pytorch.org/get-started/locally/) 
  
### Installation
1. Install PyTorch (>= 1.1.0)
2. To install the package simply run the following line:
```
pip install git+'https://github.com/otaheri/chamfer_distance'

```

### Usage
```python
import torch
from chamfer_distance import ChamferDistance
import time

chamfer_dist = ChamferDistance()

p1 = torch.rand([10,25,3])
p2 = torch.rand([10,15,3])

s = time.time()
dist1, dist2, idx1, idx2 = chamfer_dist(p1,p2)
loss = (torch.mean(dist1)) + (torch.mean(dist2))

torch.cuda.synchronize()
print(f"Time: {time.time() - s} seconds")
print(f"Loss: {loss}")

#...
```

### Integration
This code has been integrated into the [Kaolin](https://github.com/NVIDIAGameWorks/kaolin) library for 3D Deep Learning by NVIDIAGameWorks. You should probably take a look at it if you are working on anything 3D :)
