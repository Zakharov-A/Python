def main() -> None:

    # play_list = ["sound1", "sound2", "sound3", "sound4", "sound5"]
    # print(play_list)

    # s1 = play_list[1]
    # # print(s1)
    # s2 = play_list[3]
    # # print(s2)
    # # play_list[1] = s2
    # # play_list[3] = s1

    # play_list[1], play_list[3] = s2, s1

    # print(play_list)


    # def func():
    #     my_list_2 = [1, 2, 3, 4]
    #     a, b, *c = my_list_2
    #     print(my_list_2)

    #     a, *b = my_list_2
    #     print(my_list_2)

    # func()  .


    play_list = ["sound1", "sound2", "sound3", "sound4", "sound5"]
    print(play_list)
    sound_one = play_list.index('sound2')
    sound_two = play_list.index('sound5')
    play_list[sound_one], play_list[sound_two] = play_list[sound_two], play_list[sound_one]
    print(play_list)

    



main()    