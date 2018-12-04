import datetime
import re

RE = re.compile(r'Guard #(?P<id>\d+) begins shift')
RE2 = re.compile(r'\[(?P<date_time>.*)\] (?P<instruction>.*)')
SCHEDULE = {}

with open('day-4-input') as f:
	data = f.readlines()

for row in data:
	match = re.match(RE2, row)
	if match:
		date_time = match.groups('date_time')
		SCHEDULE[date_time] = match.group('instruction')

SCHEDULE = sorted(SCHEDULE)
SLEEPS = {}
curr_id = None
start_minute = None
end_minute = None
guards = {}
for row in SCHEDULE:
	time = row[0]
	instruction = row[1]

	if '#' in instruction:
		curr_id = re.match(RE, instruction).group('id')
		SLEEPS[curr_id] = SLEEPS.get(curr_id) or 0
		guards[curr_id] = guards.get(curr_id) or '' 

	elif 'falls asleep' in instruction:
		start_minute = int(time[-2:])

	elif 'wakes up' in instruction:
		end_minute = int(time[-2:])

	if start_minute is not None and end_minute is not None:
		sleep_time = (end_minute - start_minute)
		SLEEPS[curr_id] += sleep_time
		guards[curr_id] += f'{start_minute}-{end_minute} '
		start_minute = end_minute = None
		print(f'#{curr_id} slept for {SLEEPS[curr_id]} between the mins of {guards[curr_id]}')

print(SLEEPS)

import operator
sleepiest_guard = max(SLEEPS.items(), key=operator.itemgetter(1))[0]
print(sleepiest_guard)
print(guards[sleepiest_guard])

minutes_map = [0] * 60

for times in guards[sleepiest_guard].split():
	mins = times.split('-')
	for m in range(int(mins[0]),int(mins[1])):
		minutes_map[m] += 1

print(minutes_map)
sleepiest_minute = minutes_map.index(max(minutes_map))

print(f"answer: {int(sleepiest_guard) * sleepiest_minute}")

sleepiest_minute = 0
saved_guard = None
for guard in guards:
	minutes_map = [0]*60
	for times in guards[guard].split():
		mins = times.split('-')
		for m in range(int(mins[0]),int(mins[1])):
			minutes_map[m] += 1
	print(guard, minutes_map)
	highest_minute_amount = max(minutes_map)
	print('-->', highest_minute_amount)
	if highest_minute_amount > sleepiest_minute:
		sleepiest_minute = highest_minute_amount
		saved_minute = minutes_map.index(highest_minute_amount)
		saved_guard = guard

ans = int(saved_guard) * int(saved_minute)
print(f'Guard {saved_guard} spent minute {saved_minute} asleep more often')
print(ans)

