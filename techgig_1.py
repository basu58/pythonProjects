def get_input_array():
    return list(map(int, input().strip().split()))

def get_cost(arr, target):
    return sum(abs(i - target) for i in arr)

if __name__ == "__main__":
    input()
    arr = get_input_array()
    queries = get_input_array()

    ans = ' '.join(str(get_cost(arr, query)) for query in queries)
    print(ans)