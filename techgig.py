from typing import List

def min_energy(n: int, x: int, arr: List[int]) -> int:
    arr.sort(reverse=True)
    return arr[x-1] if x==n else -1 if arr[x-1]==arr[x] else arr[x-1]

def main():
    N, X = list(map(int, input().strip().split(' ')))
    arr = list(map(int, input().strip().split(' ')))
    print(min_energy(N, X, arr))

if __name__=='__main__':
    main()