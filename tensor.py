import torch
x = torch.rand(5, 3)
print(x)
print(torch.__version__) 
print(torch.cuda.is_available())