attiudes = [9,9,9,8,9,9,8,9,9,9]

for attiude in attiudes:
    print(attiudes)
    attiude = attiude + 1

print("참조하는 attiude에 값을 더한것 - attribute: call by value")
print(attiudes)

for i in range(len(attiudes)):
    attiudes[i] = attiudes[i] + 1

print("attiude에 i번째 index에 더한 값을 넣어준 것 - attribute[i]: call by reference")
print(attiudes)