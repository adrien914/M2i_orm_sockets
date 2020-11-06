with open() as f:
    for i in range(1000):
        f.write("%d;Formation %d\n" % (i, i))
