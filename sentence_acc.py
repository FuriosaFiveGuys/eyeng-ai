def sentence_acc(a, b):
    t = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            t += 1

    return t / len(a)



