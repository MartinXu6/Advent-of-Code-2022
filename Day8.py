trees = [i.strip() for i in list(open("Input", "r"))]
visible = 0
scenic_score = 0


def left_and_right():
    row_ = list(map(int, trees[row]))
    if column != 0 and column != len(row_) - 1:
        return True if int(trees[row][column]) > max(row_[:column]) or int(trees[row][column]) > max(
            row_[::-1][:len(trees[row]) - 1 - column]) else False
    else:
        return True


def width_distance():
    row_ = list(map(int, trees[row]))
    left = 0
    right = 0
    for i in row_[:column][::-1]:
        left += 1
        if i >= row_[column]:
            break
    for x in row_[column + 1:]:
        right += 1
        if x >= row_[column]:
            break
    return left * right


def height_distance():
    column_ = column_ = [int(rows[column]) for rows in trees]
    top = 0
    down = 0
    for i in column_[:row][::-1]:
        top += 1
        if i >= column_[row]:
            break
    for x in column_[row + 1:]:
        down += 1
        if x >= column_[row]:
            break
    return top * down


def top_and_down():
    column_ = [int(rows[column]) for rows in trees]
    if row != 0 and row != len(column_) - 1:
        return True if int(trees[row][column]) > max(column_[:row]) or int(trees[row][column]) > max(
            column_[::-1][:len(trees) - 1 - row]) else False
    else:
        return True


max_ = 0
for row in range(len(trees)):
    for column in range(len(trees[0])):
        max_ = max(width_distance() * height_distance(), max_)
        if top_and_down() or left_and_right():
            visible += 1
print(f"p1:{visible}")
print(f"p2:{max_}")
