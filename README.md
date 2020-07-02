# Chamfer Distance for pyTorch

This is an implementation of the Chamfer Distance as a module for pyTorch. It is written as a custom C++/CUDA extension.

As it is using pyTorch's [JIT compilation](https://pytorch.org/tutorials/advanced/cpp_extension.html), there are no additional prerequisite steps that have to be taken. Simply import the module as shown below; CUDA and C++ code will be compiled on the first run.


### Requirements
The only requirement is:
  * [Pytorch>=1.1.0](https://pytorch.org/get-started/locally/) 
  
### Installation
To install the package simply run the following line:
```
pip install git+'https://github.com/OmidThr/chamfer_distance'

```

### Usage
```python
import torch
from chamfer_distance import ChamferDistance
chamfer_dist = ChamferDistance()

p1 = torch.rand([10,25,3])
p2 = torch.rand([10,15,3])

dist1, dist2, idx1, idx2 = chamfer_dist(p1,p2)
loss = (torch.mean(dist1)) + (torch.mean(dist2))

#...
```

### Integration
This code has been integrated into the [Kaolin](https://github.com/NVIDIAGameWorks/kaolin) library for 3D Deep Learning by NVIDIAGameWorks. You should probably take a look at it if you are working on anything 3D :)
