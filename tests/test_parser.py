import os
import tempfile
from parser import Parser, InstructionType


def create_temp_asm(content: str) -> str:
    """Cria um arquivo .asm temporário para testes."""
    tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.asm', delete=False)
    tmp.write(content)
    tmp.close()
    return tmp.name


def test_a_instruction():
    """Testa o reconhecimento de A-instruction."""
    path = create_temp_asm("@10\n")
    parser = Parser(path)
    parser.advance()
    assert parser.instruction_type() == InstructionType.A_INSTRUCTION
    assert parser.symbol() == '10'
    os.unlink(path)
    print(" Teste de A-instruction passou!")


def test_a_instruction_symbol():
    """Testa A-instruction com símbolo."""
    path = create_temp_asm("@LOOP\n")
    parser = Parser(path)
    parser.advance()
    assert parser.instruction_type() == InstructionType.A_INSTRUCTION
    assert parser.symbol() == 'LOOP'
    os.unlink(path)
    print(" Teste de A-instruction com símbolo passou!")


def test_label():
    """Testa o reconhecimento de Label."""
    path = create_temp_asm("(LOOP)\n")
    parser = Parser(path)
    parser.advance()
    assert parser.instruction_type() == InstructionType.LABEL
    assert parser.symbol() == 'LOOP'
    os.unlink(path)
    print(" Teste de Label passou!")


def test_c_instruction_dest_comp():
    """Testa C-instruction com dest e comp."""
    path = create_temp_asm("D=A\n")
    parser = Parser(path)
    parser.advance()
    assert parser.instruction_type() == InstructionType.C_INSTRUCTION
    assert parser.dest() == 'D'
    assert parser.comp() == 'A'
    assert parser.jump() is None
    os.unlink(path)
    print(" Teste de C-instruction dest=comp passou!")


def test_c_instruction_comp_jump():
    """Testa C-instruction com comp e jump."""
    path = create_temp_asm("D;JGT\n")
    parser = Parser(path)
    parser.advance()
    assert parser.instruction_type() == InstructionType.C_INSTRUCTION
    assert parser.dest() is None
    assert parser.comp() == 'D'
    assert parser.jump() == 'JGT'
    os.unlink(path)
    print(" Teste de C-instruction comp;jump passou!")


def test_c_instruction_dest_comp_jump():
    """Testa C-instruction com dest, comp e jump."""
    path = create_temp_asm("MD=D+1;JMP\n")
    parser = Parser(path)
    parser.advance()
    assert parser.instruction_type() == InstructionType.C_INSTRUCTION
    assert parser.dest() == 'MD'
    assert parser.comp() == 'D+1'
    assert parser.jump() == 'JMP'
    os.unlink(path)
    print(" Teste de C-instruction dest=comp;jump passou!")


def test_ignore_comments():
    """Testa se comentários são ignorados."""
    path = create_temp_asm(
        "// comentario\n"
        "@10 // comentario inline\n"
    )
    parser = Parser(path)
    parser.advance()
    assert parser.symbol() == '10'
    os.unlink(path)
    print(" Teste de ignorar comentários passou!")


def test_has_more_instructions():
    """Testa has_more_instructions."""
    path = create_temp_asm("@10\n@20\n")
    parser = Parser(path)
    assert parser.has_more_instructions() == True
    parser.advance()
    assert parser.has_more_instructions() == True
    parser.advance()
    assert parser.has_more_instructions() == False
    os.unlink(path)
    print(" Teste de has_more_instructions passou!")


def test_multiple_instructions():
    """Testa múltiplas instruções."""
    path = create_temp_asm(
        "@10\n"
        "D=A\n"
        "(LOOP)\n"
        "D;JGT\n"
    )
    parser = Parser(path)

    parser.advance()
    assert parser.instruction_type() == InstructionType.A_INSTRUCTION

    parser.advance()
    assert parser.instruction_type() == InstructionType.C_INSTRUCTION

    parser.advance()
    assert parser.instruction_type() == InstructionType.LABEL

    parser.advance()
    assert parser.instruction_type() == InstructionType.C_INSTRUCTION

    os.unlink(path)
    print(" Teste de múltiplas instruções passou!")


