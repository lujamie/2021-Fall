import ps1
import random
import time
import csv
import math
import matplotlib.pyplot as plt

max = 20

winners = {
    'merge': [],
    'count': [],
    'radix': []
}

count = 0

iterations = 10

for U_p in range(1, max):
    U = 2**U_p
    for n_p in range(1, max):
        n = 2**n_p

        # generate arr
        arr = [(random.randrange(0, U, 1), i) for i in range(n)]

        for i in range(iterations):

            # test on sorting algos
            start_time = time.time()
            ps1.mergeSort(arr)
            mergeTime = time.time() - start_time

            start_time = time.time()
            ps1.countSort2(arr, U)
            countTime = time.time() - start_time

            start_time = time.time()
            ps1.radixSort(arr, n, U)
            radixTime = time.time() - start_time

            if min(mergeTime, countTime, radixTime) == mergeTime:
                winners['merge'].append((n_p, U_p))
            elif countTime < radixTime:
                winners['count'].append((n_p, U_p))
            else:
                winners['radix'].append((n_p, U_p))
            
            count += 1

# with open("winners.csv", "w") as outfile:
#    writer = csv.writer(outfile)
#    writer.writerow(winners.keys())
#    writer.writerows(zip(*winners.values()))
print(winners)
print(count)

# plot graphs
n_m = []
U_m = []
for x, y in winners['merge']:
  n_m.append(x)
  U_m.append(y)
plt.scatter(n_m, U_m, alpha=0.5, color="blue")

n_c = []
U_c = []
for x, y in winners['count']:
  n_c.append(x)
  U_c.append(y)
plt.scatter(n_c, U_c, alpha=0.5, color="red")

n_r = []
U_r = []
for x, y in winners['radix']:
  n_r.append(x)
  U_r.append(y)
plt.scatter(n_r, U_r, alpha=0.5, color="green")

plt.show()