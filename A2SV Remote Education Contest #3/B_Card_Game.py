n_dec = int(input())  # Number of cards
List_ = list(map(int, input().split()))  # List of card values

player = n_dec // 2  # Number of players (integer division)
total = sum(List_)  # Total sum of card values
target_num = total // player  # Target sum for each player (integer division)

left = 0  # Start of the list
right = n_dec - 1  # End of the list (corrected index)

while left < right:
    if List_[left] + List_[right] == target_num:
        # Print 1-based indices
        print(left + 1, right + 1)
        left += 1
        right -= 1
    elif List_[left] + List_[right] < target_num:
        left += 1  # Move left pointer to the right
    else:
        right -= 1  # Move right pointer to the left