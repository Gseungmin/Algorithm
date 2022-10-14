up, down, tree_height = map(int,input().split())
if (tree_height - up) % (up-down) == 0:
    i = (tree_height - up) // (up-down)
else:
    i = ((tree_height - up) // (up-down)) + 1 
i += 1
print(i)