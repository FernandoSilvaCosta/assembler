import sys
import os
from parser import Parser, InstructionType
from symbol_table import SymbolTable
from code import Code


def first_pass(filename: str, symbols: SymbolTable):
    """Primeira passagem: registra labels na tabela de símbolos."""
    parser = Parser(filename)
    address = 0

    while parser.has_more_instructions():
        parser.advance()
        itype = parser.instruction_type()

        if itype == InstructionType.LABEL:
            symbols.add_entry(parser.symbol(), address)
        else:
            address += 1


def second_pass(filename: str, symbols: SymbolTable, output_path: str):
    """Segunda passagem: gera o código binário."""
    parser = Parser(filename)

    with open(output_path, 'w') as out:
        while parser.has_more_instructions():
            parser.advance()
            itype = parser.instruction_type()

            if itype == InstructionType.A_INSTRUCTION:
                symbol = parser.symbol()
                if symbol.isdigit():
                    value = int(symbol)
                else:
                    value = symbols.add_variable(symbol)
                binary = '0' + format(value, '015b')
                out.write(binary + '\n')

            elif itype == InstructionType.C_INSTRUCTION:
                binary = (
                    '111' +
                    Code.comp(parser.comp()) +
                    Code.dest(parser.dest()) +
                    Code.jump(parser.jump())
                )
                out.write(binary + '\n')

            # labels são ignorados na segunda passagem


def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo.asm>")
        sys.exit(1)

    input_path = sys.argv[1]

    if not os.path.exists(input_path):
        print(f" Arquivo não encontrado: {input_path}")
        sys.exit(1)

    if not input_path.endswith('.asm'):
        print(" O arquivo deve ter extensão .asm")
        sys.exit(1)

    output_path = input_path.replace('.asm', '.hack')

    symbols = SymbolTable()
    first_pass(input_path, symbols)
    second_pass(input_path, symbols, output_path)

    print(f" Gerado: {output_path}")


if __name__ == '__main__':
    main()

