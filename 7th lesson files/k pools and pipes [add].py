with open('pipes.txt', 'r') as file:
    lines = file.read().splitlines()

times = []
pipes_started = False
for line in lines:
    if not pipes_started:
        if line.strip():
            times.append(float(line))
        else:
            pipes_started = True
    else:
        pipe_p = list(map(int, line.split()))
        total_p = sum(pipe_p)
        break
total_m = sum(times) * 60
ans = total_m / total_p
with open('time.txt', 'w') as file:
    file.write(str(ans))
