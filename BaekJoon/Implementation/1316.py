song = []

while True:
    input_data = input()
    
    if input_data == 'stop':
        break
    
    for i in range(len(song)):
        if song[i] == input_data:
            print(input_data + '곡이 있습니다.')
            continue

    song.append(input_data)

print(song)