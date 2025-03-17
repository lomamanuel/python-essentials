temps = [[0.0 for h in range(24)] for d in range(31)]

# Insert temps for example
temps[0][11]=9.3
temps[1][11]=9.3
temps[2][11]=9.3
temps[3][11]=6.3
temps[4][11]=9.3
temps[5][11]=9.3
temps[6][11]=9.3
temps[7][11]=9.3
temps[8][11]=6.3
temps[9][11]=9.3
temps[10][11]=9.3
temps[11][11]=9.3
temps[12][11]=11.0
temps[13][11]=9.3
temps[14][11]=8.3
temps[15][11]=9.3
temps[16][11]=9.3
temps[17][11]=9.3
temps[18][11]=9.3
temps[19][11]=9.3
temps[20][11]=0.3
temps[21][11]=9.3
temps[22][11]=9.3
temps[23][11]=9.3
temps[24][11]=9.5
temps[25][11]=9.3
temps[26][11]=9.3
temps[27][11]=9.0
temps[28][11]=9.3
temps[29][11]=9.3
temps[30][11]=10.7

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

#############################################################

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("The highest temperature was:", highest)

#############################################################

hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "days were hot.")
