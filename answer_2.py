def remove_outer_layer(input_string):
    ret = ''
    count = 0
    for i in input_string:
        if i == '(':
            if count > 0:
                ret += i
            count += 1
        elif i == ')':
            if count > 1:
                ret += i
            count -= 1

    return ret

if __name__ == '__main__':
    input_string = input()
    result = remove_outer_layer(input_string)
    print(str(result) + '\n')