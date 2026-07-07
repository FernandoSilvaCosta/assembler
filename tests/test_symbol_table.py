from symbol_table import SymbolTable


def test_predefined_symbols():
    """Testa os símbolos predefinidos."""
    table = SymbolTable()
    assert table.get_address('R0') == 0
    assert table.get_address('R15') == 15
    assert table.get_address('SP') == 0
    assert table.get_address('LCL') == 1
    assert table.get_address('ARG') == 2
    assert table.get_address('THIS') == 3
    assert table.get_address('THAT') == 4
    assert table.get_address('SCREEN') == 16384
    assert table.get_address('KBD') == 24576
    print("✅ Teste de símbolos predefinidos passou!")


def test_add_entry():
    """Testa a adição de um label."""
    table = SymbolTable()
    table.add_entry('LOOP', 10)
    assert table.get_address('LOOP') == 10
    assert table.contains('LOOP') == True
    print("✅ Teste de add_entry passou!")


def test_add_variable():
    """Testa a adição de variáveis."""
    table = SymbolTable()
    addr1 = table.add_variable('contador')
    addr2 = table.add_variable('soma')
    assert addr1 == 16
    assert addr2 == 17
    print("✅ Teste de add_variable passou!")


def test_add_variable_already_exists():
    """Testa que variável existente não é realocada."""
    table = SymbolTable()
    addr1 = table.add_variable('contador')
    addr2 = table.add_variable('contador')
    assert addr1 == addr2 == 16
    print("✅ Teste de add_variable existente passou!")


def test_contains():
    """Testa o método contains."""
    table = SymbolTable()
    assert table.contains('R0') == True
    assert table.contains('LOOP') == False
    table.add_entry('LOOP', 10)
    assert table.contains('LOOP') == True
    print("✅ Teste de contains passou!")


def test_get_address_not_found():
    """Testa get_address para símbolo inexistente."""
    table = SymbolTable()
    assert table.get_address('NAO_EXISTE') is None
    print("✅ Teste de get_address não encontrado passou!")


def test_variable_allocation_sequence():
    """Testa a sequência de alocação de variáveis."""
    table = SymbolTable()
    for i in range(5):
        addr = table.add_variable(f'var{i}')
        assert addr == 16 + i
    print("✅ Teste de sequência de alocação passou!")
