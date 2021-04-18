def solution(number, k):
    stack = []
    
    for i in range(len(number)):
        if not stack:
            stack.append(number[i])
            continue
        
        is_remove = False
        
        while stack and int(stack[-1]) < int(number[i]):
            stack.pop()
            k -= 1
            if not k:
                is_remove = True
                stack += number[i:]
                break
        
        if is_remove:
            break
        
        stack.append(number[i])

    return "".join(stack[:len(number) - k]) if k else "".join(stack)
  
