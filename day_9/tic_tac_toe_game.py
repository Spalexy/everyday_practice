
play_area = '1|2|3\n4|5|6\n7|8|9'
possible_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def check_if_the_game_is_over():
    is_game_over = input('Это конец игры? (д/н): ')
    if is_game_over.lower() in ('да', 'д', 'yes', 'y'):
        print('Игра окончена')
        return True


while True:
    selected_field_number = input('Введите номер ячейки, на которое хотите поставить свой крестик: ')

    while True:
        if selected_field_number not in possible_moves:
            selected_field_number = input('Неправильный номер ячейки, пожалуйста, введите снова: ')
        else:
            break

    possible_moves.remove(selected_field_number)
    play_area = play_area.replace(selected_field_number, 'X')
    print(play_area)

    if check_if_the_game_is_over():
        break

    computer_move = possible_moves[0]
    possible_moves.remove(computer_move)
    play_area = play_area.replace(computer_move, 'O')
    print(play_area)

    if check_if_the_game_is_over():
        break
