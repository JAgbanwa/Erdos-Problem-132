import math
from collections import defaultdict

header = '{:>4} {:>7} {:>8} {:>18} {:>10} {:>14} {:>16}'.format(
    'k','n','|D|','E=sum m_d^2','E/n^3','E/n^(8/3)','n^3/sqrt(logn)')
print(header)
print('-' * len(header))

for k in [5, 8, 10, 15, 20, 25, 30]:
    A = [(x,y) for x in range(1,k+1) for y in range(1,k+1)]
    n = len(A)
    dist_count = defaultdict(int)
    for i in range(n):
        for j in range(i+1, n):
            dx = A[i][0]-A[j][0]
            dy = A[i][1]-A[j][1]
            d2 = dx*dx + dy*dy
            dist_count[d2] += 1
    E = sum(v*v for v in dist_count.values())
    D = len(dist_count)
    logn = math.log(n)
    ratio1 = E / (n**3)
    ratio2 = E / (n**(8.0/3.0))
    ref = n**3 / math.sqrt(logn)
    row = '{:>4} {:>7} {:>8} {:>18} {:>10.4f} {:>14.4f} {:>16.1f}'.format(
        k, n, D, E, ratio1, ratio2, ref)
    print(row)

# Also compute max m_d and H count for n=900 (k=30)
print()
print("--- Heavy distances (m_d > n) for k=30 grid ---")
k = 30
A = [(x,y) for x in range(1,k+1) for y in range(1,k+1)]
n = len(A)
dist_count = defaultdict(int)
for i in range(n):
    for j in range(i+1, n):
        dx = A[i][0]-A[j][0]
        dy = A[i][1]-A[j][1]
        d2 = dx*dx + dy*dy
        dist_count[d2] += 1
heavy = [(d,m) for d,m in dist_count.items() if m > n]
light = [(d,m) for d,m in dist_count.items() if 1 <= m <= n]
print("n = {}".format(n))
print("|D| = {}".format(len(dist_count)))
print("|H| (m_d > n) = {}".format(len(heavy)))
print("|L| (1 <= m_d <= n) = {}".format(len(light)))
print("max m_d = {}".format(max(dist_count.values())))
print("top-5 multiplicities: {}".format(sorted(dist_count.values(), reverse=True)[:5]))
