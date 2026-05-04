def read_for_trees(s: str):
    if s[:4]=="tree":
        return True
    else:
        return False


def main():
    s = input()
    index = -1
    for i in range(len(s) - 3):
        if read_for_trees(s[i:]):
            index = i
            break
    if index == -1:
        print("No trees here")
    else:
        print(index)

if __name__ == "__main__":
    main()