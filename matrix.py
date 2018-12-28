class Matrix:

    def __init__(self, rows, cols):
        self.elements = []
        self.rows = rows
        self.cols = cols
        for _ in range(rows): 
            self.elements.append([0] * cols)

    def __repr__(self):
        return '\n'.join([' '.join([str(el) for el in row]) for row in self.elements])

    def __setitem__(self, key, value):
        self.elements[key[0]][key[1]] = value

    def __getitem__(self, key):
        return self.elements[key[0]][key[1]]

    def shape(self): return (self.rows, self.cols)
    
    def T(self):
        T = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                T[i,j] = self[j,i]
        return T

    def __mul__(self, other):
        if isinstance(other, int): print('mul int')
        else: print('no mul')
        return self

m = Matrix(3,3)
m[1,1] = 2
m[0,0] = 1
m[1,0] = 2
m[2,0] = 3
print(m)
print(m.shape())
print(m.T())

m*2