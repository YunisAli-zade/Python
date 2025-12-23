def gravity_flip() -> list:
    n = int(input())
    cubes = list(map(int, input().split()))
    cubes = sorted(cubes)
    for col in cubes:
        print(str(col), end=' ')
    return cubes
gravity_flip()