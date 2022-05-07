def deduplication(ls):
    l2 = list(set(ls))
    l2.sort(key=ls.index)
    return l2

if __name__ == '__main__':
    ls=[5,9,4,9,3,5,8,9,9,5,8]
    a=deduplication(ls)
    print(ls,a,sep="\n")
