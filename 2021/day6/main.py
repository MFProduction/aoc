state = open("input.txt", "r").readline().split(",")

def get_state(state, days):
    state_count = [0] * 9
    for fish in state:
        state_count[int(fish)] += 1
    for _ in range(days):
        new_state = [0] * 9
        for index in range(8,-1,-1):
            if index > 0:
                new_state[index-1] = state_count[index]
            elif index == 0:
                new_state[6] += state_count[index]
                new_state[8] += state_count[index]
        state_count = new_state
    return(sum(state_count))

print(get_state(state, 80))
print(get_state(state, 256))
