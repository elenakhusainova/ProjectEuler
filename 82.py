# Read matrix from the file:
filename = "p082_matrix.txt"
f = open(filename, "r")
data = [list(map(int, line.split(','))) for line in f]
f.close()

N = len(data)
aux = data[:] # Auxiliary matrix

for col in range(1, N + 1):
    column = [aux[i][-col] for i in range(N)]
    for row in range(N):
        if col != 1:
            temp = aux[row][-col] + aux[row][-col + 1]
            for i in range(N):
                curr = sum(column[min(i, row) : max(i, row) + 1]) + aux[i][-col + 1]
                if (curr <= temp):
                    aux[row][-col] = curr
                    temp = curr

print(min([aux[i][0] for i in range(N)]))
