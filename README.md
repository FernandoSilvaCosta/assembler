# 🖥️ Assembler Hack — Montador Assembly para Binário

Montador (assembler) que traduz programas em Assembly Hack (.asm) para código de máquina binário (.hack), executável pelo CPU Emulator do Nand2Tetris.

---

## 👥 Integrantes

- FERNANDO DA SILVA COSTA

---

## 📁 Estrutura do Projeto

assembler/
├── parser.py           # Analisador de arquivos .asm
├── symbol_table.py     # Tabela de símbolos
├── code.py             # Gerador de código binário
├── main.py             # Orquestrador em duas passagens
│
├── tests/
│   ├── test_parser.py
│   ├── test_symbol_table.py
│   └── test_code.py
│
├── projects/
│   └── 6/
│       ├── add/
│       │   └── Add.asm
│       ├── max/
│       │   ├── Max.asm
│       │   └── MaxL.asm
│       ├── rect/
│       │   ├── Rect.asm
│       │   └── RectL.asm
│       └── pong/
│           ├── Pong.asm
│           └── PongL.asm
│
├── .gitignore
└── README.md

---

## 🧠 Como Funciona

### Pipeline de Tradução

Assembly Hack → Parser → SymbolTable → Code → Binário .hack

### Tipos de Instrução

| Tipo | Exemplo | Descrição |
|------|---------|-----------|
| A-instruction | @10, @LOOP | Carrega valor ou endereço no registrador A |
| C-instruction | D=A, D;JGT, MD=D+1 | Operação computacional com destino e salto opcional |
| Label | (LOOP) | Declara um rótulo para saltos |

### Formato Binário

| Tipo | Formato | Exemplo |
|------|---------|---------|
| A-instruction | 0vvvvvvvvvvvvvvv | @10 → 0000000000001010 |
| C-instruction | 111accccccdddjjj | D=A → 1110110000010000 |

### Duas Passagens

Primeira passagem — registra labels na tabela de símbolos:
- Percorre o arquivo contando instruções
- Registra cada label com seu endereço correspondente

Segunda passagem — gera o código binário:
- A-instruction com número → converte direto para binário
- A-instruction com símbolo → busca na tabela ou aloca novo endereço
- C-instruction → combina comp, dest e jump em 16 bits
- Labels são ignorados

### Tabela de Símbolos Predefinidos

| Símbolo | Endereço |
|---------|----------|
| R0-R15 | 0-15 |
| SP | 0 |
| LCL | 1 |
| ARG | 2 |
| THIS | 3 |
| THAT | 4 |
| SCREEN | 16384 |
| KBD | 24576 |

Variáveis não predefinidas são alocadas a partir do endereço 16.

### Encoding C-instruction

Campo comp (7 bits):

| comp | Binário |
|------|---------|
| 0 | 0101010 |
| 1 | 0111111 |
| D | 0001100 |
| A | 0110000 |
| M | 1110000 |
| D+A | 0000010 |
| D+M | 1000010 |
| D-A | 0010011 |

Campo dest (3 bits):

| dest | Binário |
|------|---------|
| nenhum | 000 |
| M | 001 |
| D | 010 |
| MD | 011 |
| A | 100 |
| AM | 101 |
| AD | 110 |
| AMD | 111 |

Campo jump (3 bits):

| jump | Binário |
|------|---------|
| nenhum | 000 |
| JGT | 001 |
| JEQ | 010 |
| JGE | 011 |
| JLT | 100 |
| JNE | 101 |
| JLE | 110 |
| JMP | 111 |

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.12+
- pytest

### Instalando o pytest

pip install pytest

### Montando um arquivo .asm

python main.py caminho/arquivo.asm

### Exemplos de uso

python main.py projects/6/add/Add.asm
python main.py projects/6/max/Max.asm
python main.py projects/6/rect/Rect.asm
python main.py projects/6/pong/Pong.asm

Isso irá gerar o arquivo .hack no mesmo diretório do .asm.

### Rodando os Testes

python -m pytest tests/ -v -s

---

## 🧪 Testes

O projeto segue a metodologia TDD (Test Driven Development).

### Parser
- ✅ A-instruction com valor e símbolo
- ✅ Label
- ✅ C-instruction com dest, comp e jump
- ✅ Ignorar comentários de linha e inline
- ✅ has_more_instructions e múltiplas instruções

### SymbolTable
- ✅ Símbolos predefinidos R0-R15, SP, LCL, ARG, THIS, THAT, SCREEN e KBD
- ✅ add_entry para labels
- ✅ add_variable com alocação automática a partir do endereço 16
- ✅ Variável existente não é realocada
- ✅ contains e get_address

### Code
- ✅ comp para 0, 1, D, A, M, D+A, D+M, D-A
- ✅ dest para None, M, D, MD, A e AMD
- ✅ jump para None, JGT, JEQ, JLT e JMP
- ✅ Encoding completo de C-instruction

### Arquivos Oficiais
- ✅ Add.asm → Add.hack
- ✅ Max.asm → Max.hack
- ✅ Rect.asm → Rect.hack
- ✅ Pong.asm → Pong.hack

---

## 📦 Arquivos Principais

### parser.py
Lê o arquivo .asm, remove comentários e classifica cada instrução como A_INSTRUCTION, C_INSTRUCTION ou LABEL. Extrai symbol, dest, comp e jump de cada instrução.

### symbol_table.py
Gerencia o mapeamento entre símbolos e endereços de memória. Inicializa com símbolos predefinidos e aloca variáveis a partir do endereço 16.

### code.py
Traduz os campos dest, comp e jump de C-instructions para código binário usando tabelas de mapeamento.

### main.py
Orquestra a tradução em duas passagens. Na primeira registra labels, na segunda gera o código binário final.

---

## 📚 Referências

- Nand2Tetris: https://www.nand2tetris.org/
