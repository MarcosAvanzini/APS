def login():
    from Cryptodome.Cipher import Blowfish
    from Cryptodome import Random
    from struct import pack

    BF = Blowfish.block_size
    Chave = b'Alohomora'
    CDS = Random.new().read(BF)
    cipher = Blowfish.new(Chave, Blowfish.MODE_CBC, CDS)
    plaintext = input('Confirme a sua Senha:')
    plen = BF - divmod(len(plaintext),BF)[1]
    padding = [plen]*plen
    padding = pack('b'*plen, *padding)
    msg = CDS + cipher.encrypt(plaintext.encode() + padding)
    print(repr(msg))
    return(msg)


