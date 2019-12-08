# Ty Ridings
# CSCI 102 - Section C

def fib():
    fibs = [1, 2]
    Fn = 3
    for i in range(1,100):
        Fn = fibs[i - 1] + fibs[i]
        fibs.append(Fn)

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
