from cipher_ens2141 import cipher_ens2141

def test_cipher():
    example = 'LAZY'
    expected = 'iXwv'
    actual = cipher(text = example, shift = 23)
    print(actual, expected)
    assert actual == expected
    print ('Success')