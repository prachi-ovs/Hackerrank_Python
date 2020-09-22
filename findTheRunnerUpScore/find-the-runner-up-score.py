if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    arr_set = list(set(arr))
    arr_set.sort(reverse=True)
    print(arr_set[1])