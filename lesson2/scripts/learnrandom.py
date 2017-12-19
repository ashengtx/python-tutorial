import random

print(dir(random))

#random.seed(2) # 传入种子，初始化随机数生成器

# random 返回下一个[0.0, 1.0)之间的随机数
print(random.random())

# randint(a, b), 返回一个整数N, a <= N <= b
for i in range(10):
    print("randint: ", random.randint(0,10))

# uniform(a, b), 返回一个实数m, a <= m <= b
for i in range(10):
    print("rand float: ", random.uniform(0,10))

# sample(population, k) 不放回的随机抽样
print("sample without replacement:", random.sample(range(1000), k=10))

# choice(seq) 从一个非空序列中随机取出一个元素
print("random choice: ", random.choice(range(1000)))

# choices(population, weights=None, cum_weights=None, k) 有放回抽样
print("sample with replacement:", random.sample(range(10), k=10))

# shuffle(seq) 打乱顺序
alist = list(range(10))
print(alist)
random.shuffle(alist)
print("after shuffling:", alist)
