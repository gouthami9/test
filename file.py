def main():

    with open('abc.txt') as f:
        a= f.read().split(' ')
        list=[]
        for i in a:
            h=''.join(e for e in i if e.isalnum())
            h=h.lower()
            list.append(h)


        wordcount = {}

        for word in list:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
        del wordcount['']

    for i in range(3):
        high=max(wordcount.values())
        for k,v in wordcount.iteritems():
            if v==high:
                print (k,'count = {}'.format(v))
                wordcount[k]=0

if __name__=='__main__':
    main()