import key_gen
import encode
import de_encode

response = input(f'''1)Generate a random passphrase
2)Encode a file 
3)Decode a file\nchoose the corresponding number: ''')

if response == '1':
    while True:
        key_gen.make_random_password()

elif response == '2':
    file_name = input('File to encode (with .txt):')
    times = int(input(
        'Times to encode (any number greater than 40 could cause problems as the file size would become big):'))
    encode.encoder(file_name, times)

elif response == '3':
    file_name = input('File to decode (with .txt):')
    times = int(input(
        'Number of times to decode(should be the same as the number used when encoding the file):'))

    de_encode.de_encoder(file_name, times)

else:
    print('Invaild Response')
