def is_inside_circle(x_b, y_b, x_m, y_m, r):
    return (x_m - x_b) ** 2 + (y_m - y_b) ** 2 <= r ** 2

def main():
    safe_to_sleep = True
    x_b, y_b = map(int, input().split())
    number_of_monsters = int(input())
    for _ in range(number_of_monsters):
        x_m, y_m = map(int, input().split())
        if is_inside_circle(x_b, y_b, x_m, y_m, 8):
            safe_to_sleep = False
            break
    if safe_to_sleep:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
