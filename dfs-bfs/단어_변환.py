def solution(begin, target, words):
    answer = 0
    queue = [begin, ]

    while True:
        q = []
        for word in queue:
            if word == target:
                return answer

            for next_word_idx in range(len(words) - 1, -1, -1):
                next_word = words[next_word_idx]
                diff = sum([x != y for x, y in zip(word, next_word)])
                if diff == 1:
                    q.append(words.pop(next_word_idx))

        if not q:
            return 0

        queue = q
        answer += 1
