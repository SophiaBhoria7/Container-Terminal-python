def minimum_stacks(container_schedule):
    stacks = []

    for container in container_schedule:
        placed = False
        for stack in stacks:
            if stack[-1] >= container:
                stack.append(container)
                placed = True
                break
        if not placed:
            stacks.append([container])

    return len(stacks)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    N = int(data[0])
    results = []

    for i in range(1, N + 1):
        container_schedule = data[i]
        results.append(minimum_stacks(container_schedule))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
