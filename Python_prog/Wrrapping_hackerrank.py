import textwrap


def wrap(string, max_width):
    #return textwrap.wrap(string,max_width)
    return textwrap.fill(string, max_width)



if __name__ == '__main__':
    string, max_width = input(), int(input())
    print(wrap(string, max_width))
    #print(result)