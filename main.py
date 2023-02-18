def generate_triangular(n):
    """
    Generates triangular numbers up to n.
    """
    current_num = 1
    row = 1
    max_spaces = n + 1
    while current_num <= n:
        row_items = []
        for i in range(row):
            row_items.append(current_num)
            current_num += 1
            if current_num > n:
                break
        for num in row_items:
            space = " " * (max_spaces - len(str(num)))
            row_str = space.join([str(num)])
        print(row_str + "\n")
        row += 1

generate_triangular(666)
