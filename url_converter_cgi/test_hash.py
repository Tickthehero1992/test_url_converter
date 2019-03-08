def converter_long_to_short(url_to_convert):
    h0= 0x33529301
    b= bytes('hui', 'utf-8')
    b=binascii.hexlify(b)
    b+=b'\x01'
    num=len(url_to_convert)
    b+=h0
    output=str(b)
    return output

url_out=str(converter_long_to_short("http://rambler.ru"))

print(url_out)