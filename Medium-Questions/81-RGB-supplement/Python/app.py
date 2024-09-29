import os

def main():
    x = int(input())
    colors = [input().split("#")[-1] for i in range(x)]
    for color in colors:
        r, g, b = int(color[:2], base=16), int(color[2:4], base=16), int(color[4:6], base=16)
        c = f"#{str(hex(255-r)).replace('0x', '').zfill(2)}{str(hex(255-g)).replace('0x', '').zfill(2)}{str(hex(255-b)).replace('0x', '').zfill(2)}"
        print(c.upper())


if __name__ == '__main__':
    main()