# -*- encoding : utf-8 -*-

from Calculator import Calculator

def main():
    calc = Calculator("/my/path/to/heaven/", "b", ".node")
    stats = calc.sumRatios()
    print(stats)


if __name__ == "__main__":
    main()