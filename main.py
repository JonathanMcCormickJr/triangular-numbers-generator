def my_function():
    num = 0
    row_size = 0
    
    def generate_triangles():
        row_size += 1
        num += 1
        for i in range(row_size):
            print(num)
        generate_triangles()
        return
    
    return
    # Maybe use recursion

my_function()