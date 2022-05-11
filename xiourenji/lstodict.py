"""
列表转字典并统计个数
"""


def todict(ls, dict=None):
    if dict is None:
        dict = {}
    for i in ls:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
if __name__ == '__main__':
    ls=[5,5,6,6,7,8,8,9]
    dt=todict(ls)
    print(dt)
