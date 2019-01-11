#Iterative

seq = [0,1]
n = 0
for count in range(2,11):
    n = seq[count - 1] + seq[count - 2]
    seq.append(n)
#next count
print(seq[1:])

