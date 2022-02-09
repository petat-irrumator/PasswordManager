import base64
import os


def de_encoder(input_file_name, times_to_dencode):
    # getting the file contents and encoding it to bytes
    input_file = open(input_file_name, 'r')
    data_to_dencode = input_file.read().encode()
    input_file.close()
    os.remove(input_file_name)
    # decoding the contents in base64 to a certain number of times
    for i in range(times_to_dencode):
        data_to_dencode = base64.b64decode(data_to_dencode)
    # putting the decoded base 64 content to another file
    output_file_name = input_file_name[8:]
    output_file = open(output_file_name, 'wb')
    output_file.write(data_to_dencode)
    output_file.close()
    # Result
    print(f'Contents of {input_file_name} are decoded in {output_file_name}')
