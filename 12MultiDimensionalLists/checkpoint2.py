# TLDR check if the list at matrix i or j has a larger maximum value. if the list maximum at the smaller index is bigger than the bigger index then swap them

# we take the list at matrix[i] and get the max from that list call it i_max
# we take the list at matrix[j] and get the max from that list call it j_max

# if i_max has a bigger max than matrix[j] AND i is less than j then swap
# if j_max has a bigger max than matrix[i] AND j is less than i then swap
