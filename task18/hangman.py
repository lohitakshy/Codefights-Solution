def hangman(word, letters):
    ckh = []
    count =0
    miss = 0
    ln = len(word)

    for i in letters:
        print(i,count,miss)
        if (i in word) and (i not in ckh):
            count = count+1
            ckh.append(i)
            ln = ln-word.count(i)
            if count >= 6 or ln <= 0 :
                return True
        else:
            miss +=1
            if miss >=6 or len(letters) ==(count+miss):
                return False
