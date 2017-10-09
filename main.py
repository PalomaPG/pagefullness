# -*- encoding : utf-8 -*-
import sys

from Calculator import Calculator

def main(written_nodes, output_path):
    calc = Calculator(written_nodes, ".node", output_path)
    calc.writeCalc()



if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])