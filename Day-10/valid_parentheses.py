# Day - 10 -> Valid Parentheses

s = input("Enter brackets: ")

stack = []

pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
}

for i in s:
    if i in pairs:
        if not stack or stack[-1] != pairs[i]:
            print("False")
            break
        stack.pop()
    else:
        stack.append(i)
else:
    print(len(stack) == 0)