import statistics
import math

input = list(map(int, open("input-test.txt", "r").readline().strip().split(",")))

def fuel(input, fuel_rate="low"):
    result = 0
    mean = sum(input) / len(input)
    median = statistics.median(input)
    # Should improve this because it doesn't work every time
    # mean = math.ceil(sum(input) / len(input))
    for number in input:
        if fuel_rate == "low":
            result += abs(number - median)
        else:
            result += (abs(int(number) - int(mean))**2 + abs(int(number) - int(mean)))/2
    return(int(result))

print(fuel(input, "low"))
print(fuel(input, "high"))
