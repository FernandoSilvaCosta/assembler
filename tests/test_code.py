from code import Code


def test_comp_zero():
    """Testa comp para 0."""
    assert Code.comp('0') == '0101010'
    print(" Teste de comp 0 passou!")


def test_comp_one():
    """Testa comp para 1."""
    assert Code.comp('1') == '0111111'
    print(" Teste de comp 1 passou!")


def test_comp_d():
    """Testa comp para D."""
    assert Code.comp('D') == '0001100'
    print(" Teste de comp D passou!")


def test_comp_a():
    """Testa comp para A."""
    assert Code.comp('A') == '0110000'
    print(" Teste de comp A passou!")


def test_comp_m():
    """Testa comp para M (a=1)."""
    assert Code.comp('M') == '1110000'
    print(" Teste de comp M passou!")


def test_comp_d_plus_a():
    """Testa comp para D+A."""
    assert Code.comp('D+A') == '0000010'
    print(" Teste de comp D+A passou!")


def test_comp_d_plus_m():
    """Testa comp para D+M."""
    assert Code.comp('D+M') == '1000010'
    print(" Teste de comp D+M passou!")


def test_comp_d_minus_a():
    """Testa comp para D-A."""
    assert Code.comp('D-A') == '0010011'
    print(" Teste de comp D-A passou!")


def test_dest_none():
    """Testa dest para None."""
    assert Code.dest(None) == '000'
    print(" Teste de dest None passou!")


def test_dest_m():
    """Testa dest para M."""
    assert Code.dest('M') == '001'
    print(" Teste de dest M passou!")


def test_dest_d():
    """Testa dest para D."""
    assert Code.dest('D') == '010'
    print(" Teste de dest D passou!")


def test_dest_md():
    """Testa dest para MD."""
    assert Code.dest('MD') == '011'
    print(" Teste de dest MD passou!")


def test_dest_a():
    """Testa dest para A."""
    assert Code.dest('A') == '100'
    print(" Teste de dest A passou!")


def test_dest_amd():
    """Testa dest para AMD."""
    assert Code.dest('AMD') == '111'
    print(" Teste de dest AMD passou!")


def test_jump_none():
    """Testa jump para None."""
    assert Code.jump(None) == '000'
    print(" Teste de jump None passou!")


def test_jump_jgt():
    """Testa jump para JGT."""
    assert Code.jump('JGT') == '001'
    print(" Teste de jump JGT passou!")


def test_jump_jeq():
    """Testa jump para JEQ."""
    assert Code.jump('JEQ') == '010'
    print(" Teste de jump JEQ passou!")


def test_jump_jlt():
    """Testa jump para JLT."""
    assert Code.jump('JLT') == '100'
    print(" Teste de jump JLT passou!")


def test_jump_jmp():
    """Testa jump para JMP."""
    assert Code.jump('JMP') == '111'
    print(" Teste de jump JMP passou!")


def test_c_instruction_encoding():
    """Testa o encoding completo de uma C-instruction."""
    # D=A → 111 + comp(A) + dest(D) + jump(None)
    binary = '111' + Code.comp('A') + Code.dest('D') + Code.jump(None)
    assert binary == '1110110000010000'
    print(" Teste de encoding completo passou!")

