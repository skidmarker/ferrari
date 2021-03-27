from collections import defaultdict

def solution(phone_book):
    phone_book.sort()
    
    for p, e in zip(phone_book, phone_book[1:]):
        if e.startswith(p):
            return False

    return True
