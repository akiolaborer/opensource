# GPUにデータを転送するプログラム
 
# PyCudaのインポート
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
# numpy配列用
import numpy
 
m = 1000
n = 1000
# m x nの乱数のnumpy配列を作成
a = numpy.random.randn(m,n)
 
# nVidiaデバイス（GPU）は単精度のみサポート→変換
a = a.astype(numpy.float32)
 
# GPU上に送信データ用のメモリを割り当てる
a_gpu = cuda.mem_alloc(a.nbytes)
 
# GPUにデータを転送
cuda.memcpy_htod(a_gpu, a)