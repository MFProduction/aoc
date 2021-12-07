state = list(map(int, open("input.txt", "r").readline().split(",")))

def get_state(state, days):
    state_count = [0] * 9
    for fish in state:
        state_count[fish] += 1
    for _ in range(days):
        daily_state = [0] * 9
        for index in range(8,-1,-1):
            if index > 0:
                daily_state[index-1] = state_count[index]
            elif index == 0:
                daily_state[6] += state_count[index]
                daily_state[8] += state_count[index]
        state_count = daily_state
    return(sum(state_count))

print(get_state(state, 80))
print(get_state(state, 256))
