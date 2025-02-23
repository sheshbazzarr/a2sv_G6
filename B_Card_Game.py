n_dec = int(input())  # Number of cards
List_ = list(map(int, input().split()))  # List of card values

player = n_dec // 2  # Number of players (integer division)
total = sum(List_)  # Total sum of card values
target_num = total // player  # Target sum for each player (integer division)

output = []  # Store pairs of indices
used = [0] * n_dec  # Track used cards

for i in range(n_dec):
    if not used[i]:  # If the card is not used
        for j in range(i + 1, n_dec):
            if not used[j] and List_[i] + List_[j] == target_num:
                # Add 1-based indices to the output
                output.append([i + 1, j + 1])
                used[i] = 1
                used[j] = 1
                break

# Print the output pairs
for pair in output:
    print(pair[0], pair[1])