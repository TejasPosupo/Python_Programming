def pattern_2(N):
    for i in range(N):
        for j in range(i+1):
            print("*", end=" ")
        print()
def main():
    N = eval(input("enter the number "))
    if (N<=1):
        print("enter a greater value")
    else:
        pattern_2(N)

if __name__ == "__main__":
    main()