import os
from os.path import exists
import sys
from array import array
import gzip


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} FILE'.format(sys.argv[0]))
        sys.exit(1)

    if not exists(sys.argv[1]):
        print('Error opening file {}'.format(sys.argv[1]))
        sys.exit(1)

    #TODO: Make different actions if input file is .html or .h
    # with open('index_ov2640.html.gz', 'wb') as output_file:
    #     uint8_array = array('B', index_ov2640_html_gz)
    #     uint8_array.tofile(output_file)

    with open(sys.argv[1], 'rb') as input_file:
        gz_data = gzip.compress(input_file.read(), compresslevel=5)
    
    # output_obj_name = sys.argv[1] + '.gz'
    # with open(output_obj_name, 'wb') as output_file:
    #     output_file.write(gz_data)
        
    with open(output_obj_name + '.h', 'w') as output_file:
        print('//File: {}, Size: {}'.format(output_obj_name, len(gz_data)), file=output_file)
        print('#define {} {}'.format(output_obj_name.replace(".", "_" ) + '_len', len(gz_data)), file=output_file)
        print('const uint8_t {}[] = {{'.format(output_obj_name.replace(".", "_" )), file=output_file)
        blocks = len(gz_data) // 16
        tail = len(gz_data) % 16
        for i in range(blocks):
            print('  {},'.format(', '.join('0x{:02X}'.format(x) for x in list(gz_data[i * 16: (i + 1) * 16]))), file=output_file)
        if tail != 0:
            print('  {}'.format(', '.join('0x{:02X}'.format(x) for x in list(gz_data[blocks * 16:]))), file=output_file)
        print('};', file=output_file)
