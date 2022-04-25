if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    t = list()
    for item in integer_list:
        t.append(item)
    
    t = tuple(t)
    print(hash(t))
