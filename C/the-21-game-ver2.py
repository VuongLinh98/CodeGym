from random import *
print("Chào mừng bạn tới với trò chơi")

while True:
    # Khởi tạo biên đếm
    current_number = 0
    # Khởi tạo người chơi là humain nếu ngẫu nhiên ra 0 và computer nếu ngẫu nhiên ra 1
    current_player = randint(0, 1)
    if current_player == 0 :
        print("Bạn là người bắt đầu")
    else:
        print("Máy tính bắt đầu")
    # Khởi tạo vòng lợp
    while current_number <= 21:
        # In ra tổng số đã nhập từ cả người dùng và máy
        print("Total: ", current_number)
        if current_player == 0:
            player_choice = ""
            # Kiểm tra số có nhập đúng là 1 hoặc 2 hoặc 3 không nếu không thì bắt nhập lại
            while ["1", "2", "3"].__contains__(player_choice) == False:
                print("Input your number:")
                player_choice = input()
                if player_choice != 1 or player_choice != 2 or player_choice != 3 :
                    print("Invalid value, please try again!")

            # In ra số người chơi nhập    
            print("You: ", player_choice)
            # Cộng thêm số vào tổng số hiện tại
            current_number += int(player_choice)
            # Kiểm tra kết quả sau khi cộng
            if current_number >= 21:
                print("You lost!") # In ra bạn thua
                break
            # Gán lại người chơi hiện tại là máy
            current_player = 1
        else:
            # Máy chọn ngẫu nhiên 1 hoặc 2 hoặc 3
            computer_choice = randint(1,3)
            # In ra số mà máy chọn
            print("Computer: ", computer_choice)
            # Cộng thêm số vào tổng số hiện tại
            current_number += computer_choice
            if current_number >= 21:
                print("You win!") # In ra bạn thắng
                break
            # Gán lại người chơi hiện tại là người
            current_player = 0
    # Hỏi xem có chơi tiếp không
    print("Do you want to play agian?")
    play_again = input()
    if play_again.__contains__("y") == False:
        break