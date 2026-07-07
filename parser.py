from enum import Enum


class InstructionType(Enum):
    A_INSTRUCTION = "A_INSTRUCTION"
    C_INSTRUCTION = "C_INSTRUCTION"
    LABEL         = "LABEL"


class Parser:
    """Lê e classifica instruções de um arquivo .asm"""

    def __init__(self, filename: str):
        with open(filename, 'r') as f:
            self.instructions = [
                line.split('//')[0].strip()
                for line in f
            ]
            # remove linhas vazias
            self.instructions = [l for l in self.instructions if l]
        self.index = 0
        self.current = None

    def has_more_instructions(self) -> bool:
        """Indica se há mais instruções para processar."""
        return self.index < len(self.instructions)

    def advance(self):
        """Avança para a próxima instrução."""
        self.current = self.instructions[self.index]
        self.index += 1

    def instruction_type(self) -> InstructionType:
        """Retorna o tipo da instrução atual."""
        if self.current.startswith('@'):
            return InstructionType.A_INSTRUCTION
        elif self.current.startswith('(') and self.current.endswith(')'):
            return InstructionType.LABEL
        else:
            return InstructionType.C_INSTRUCTION

    def symbol(self) -> str:
        """Retorna o símbolo de uma A-instruction ou Label."""
        if self.instruction_type() == InstructionType.A_INSTRUCTION:
            return self.current[1:]
        else:
            return self.current[1:-1]

    def dest(self) -> str:
        """Retorna a parte dest de uma C-instruction."""
        if '=' in self.current:
            return self.current.split('=')[0]
        return None

    def comp(self) -> str:
        """Retorna a parte comp de uma C-instruction."""
        instruction = self.current
        if '=' in instruction:
            instruction = instruction.split('=')[1]
        if ';' in instruction:
            instruction = instruction.split(';')[0]
        return instruction

    def jump(self) -> str:
        """Retorna a parte jump de uma C-instruction."""
        if ';' in self.current:
            return self.current.split(';')[1]
        return None

