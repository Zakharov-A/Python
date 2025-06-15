def func():
    play_list = ['1', '2', 'sound3', 'sound4', 'sound5']
    # play_list = ['1', '2']
    ints = []
    
    try:
        for line in play_list:
            ints.append(int(line))
    except ValueError:
        print('This is not a number! ') 
    except Exception:
        print("What is this? What's wroung wiht you?!")
    else:
        print("Everything is fine!")
    finally:
        print(ints)               

func()