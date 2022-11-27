import random
import statistics
from scipy.stats.mstats import gmean
import numpy as np

# 分析対象の配列長を定義
length = 100
target = [random.randint(0,100) for i in range(length)]
print(target)
# [96, 77, 75, 41, 28, 96, 2, 68, 11, 57, 32, 73, 75, 28, 31, 11, 62, 2, 67, 84, 70, 92, 45, 40, 13, 26, 10, 57, 43, 19, 72, 96, 3, 98, 100, 18, 13, 40, 54, 5, 74, 9, 11, 19, 86, 43, 86, 45, 48, 24, 10, 40, 30, 47, 10, 22, 1, 46, 76, 4, 58, 44, 89, 7, 57, 95, 57, 76, 26, 98, 12, 19, 81, 94, 87, 39, 78, 15, 85, 54, 52, 38, 83, 26, 60, 5, 65, 42, 10, 35, 12, 54, 5, 97, 7, 24, 88, 90, 24, 87]      

# 平均値
# #相加平均
arithmetic_mean = statistics.mean(target)
print(arithmetic_mean)
# 47.36

# #相乗平均
geometric_mean = gmean(target)
print(geometric_mean)
# 33.008188446952374

# #調和平均
harmonic_mean = statistics.harmonic_mean(target)
print(harmonic_mean)
# 15.885379357540009

# 中央値
median = statistics.median(target)
print(median)
# 44.5

# 最小値
Minimun = min(target)
print(Minimun)
# 1

# 最大値
Max = max(target)
print(Max)
# 100

# 四分位数
quartiles_array = np.percentile(target, q=[0,25,50,75,100])
print(quartiles_array)
# [  1.    19.    44.5   75.25 100.  ]

# 四分位範囲
quartile_range = quartiles_array[3] - quartiles_array[1]
print(quartile_range)
# 56.25

# 最頻値
mode = statistics.mode(target) #最頻地が複数存在する場合，エラーになるらしいので要注意．
print(mode)
# 57

# 平均絶対偏差
mad = statistics.mean([abs(x - arithmetic_mean) for x in target])
print(mad)
# 26.9088

# 分散
Variance = statistics.pvariance(target)
print(Variance)
# 947.6704

# 不偏分散
sample_variance = statistics.variance(target)
print(sample_variance)
# 957.2428282828283

# 標準偏差
std = statistics.pstdev(target)
print(std)
# 30.784255716193627

# 不偏標準偏差
sample_std = statistics.stdev(target)
print(sample_std)
# 30.939341109384156

# 変動係数
coefficient_variation = std / arithmetic_mean
print(coefficient_variation)
# 0.6500053994128722
