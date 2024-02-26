from random import *
print("Chào mừng bạn^^")
while True :
    #Khai báo biến tổng số đếm:
    current_number = 0
    #Lựa chọn người chơi:
    current_player = randint(0,1)
    
    #Vòng lặp số đếm:
    while current_player == 0 or current_player == 1:
        #kiểm tra lượt chơi:
        if current_player == 0 :
            print("Lượt chơi của bạn")
            print("Tổng số hiện tại là: ", current_number)
            player_choice = int(input("Nhập một số bất kỳ từ 1-3: "))
            if player_choice == 1 or player_choice == 2 or player_choice ==3:
                current_number += player_choice
                current_player = 1
                if current_number >= 21 :
                    print("Tổng số hiện tại là: ", current_number)
                    print("Bạn đã thua, vui lòng thử lại!")
                    break
            else:
                print("Giá trị không hợp lệ, vui lòng thử lại!")
                current_player = 0
        if current_player == 1 :
            print("Lượt chơi của máy")
            print("Tổng số hiện tại là: ", current_number)
            computer_choice = int(randint(1,3))
            if computer_choice == 1 or computer_choice == 2 or computer_choice == 3 :
                current_number += computer_choice
                current_player = 0
                if current_number >= 21 :
                    print("Tổng số hiện tại là: ", current_number)
                    print("Chúc mừng, bạn đã chiến thắng!")
                    break
    
    if current_number >= 21 :
        play_again = input("Bạn có muốn chơi lại không - Yes or No?")
        if play_again == "Yes" or play_again == "yes" : 
            continue
        else:
            break
