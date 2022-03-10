s_list = []

def d(self, n):
    n = str(n)
    global s_list
    for s in n:
        s_list.append(int(s))
    
    n = int(n)
    if n > 10:
        self.result = n + sum(s_list)

    else:
        self.result = n
    return self.result
    # if self.result < 10000:
    #     return d(self.result)

print(d(10))