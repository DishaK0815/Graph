VertextData = ['A', 'B', 'C', 'D']
Adjacency_Matrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0]
]

def Print_Adjacency_Matrix(matrix):
    for row in matrix:
        print(row)
        
print("Vertex of Adjacency graph")
Print_Adjacency_Matrix(Adjacency_Matrix)
def print_connections(matrix, vertices):
    print("\nConnections for each vertex:")
    for i in range(len(vertices)):
        print(f"{vertices[i]}: ", end="")
        for j in range(len(vertices)):
            if matrix[i][j]:  # if there is a connection
                print(vertices[j], end=" ")
        print()
print_connections(Adjacency_Matrix, VertextData)