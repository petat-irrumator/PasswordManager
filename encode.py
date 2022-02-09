import base64
import os


# any number greater than 40 could cause problems as the file size would become big


def encoder(input_file_name, times_to_encode):
    # getting the file contents and encoding it to bytes
    input_file = open(input_file_name, 'r')
    data_to_encode = input_file.read().encode()
    input_file.close()
    os.remove(input_file_name)
    # encoding the contents in base64 to a certain number of times
    for i in range(times_to_encode):
        data_to_encode = base64.b64encode(data_to_encode)
    # putting the encoded base 64 content to another file
    output_file_name = 'encoded'+'_'+input_file_name
    output_file = open(output_file_name, 'wb')
    output_file.write(data_to_encode)
    output_file.close
    # Result
    print(f'Contents of {input_file_name} are encoded in {output_file_name}')
