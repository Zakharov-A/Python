def play_list_dz():
    play_list = ['sound1', 'sound2', 'sound3', 'sound4', 'sound5']
    print(play_list)
    sound_one = play_list.index('sound2')
    sound_two = play_list.index('sound5')
    play_list[sound_one], play_list[sound_two] = play_list[sound_two], play_list[sound_one]
    print(play_list)

play_list_dz()    