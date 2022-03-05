import datetime as dt
import random as rn
from time import sleep


def write_line(text_line, out_file_name='Data_out/way_sim.out'):
    file = open(out_file_name, 'a', encoding='utf-8')
    file.write(text_line + '\n')
    file.close()

def get_rn_start_stop_val(max_len=130):
    tmp_start = ( rn.random() * ( max_len - 20) * 10 ) % max_len
    tmp_stop = ( rn.random() * ( max_len ) * 10 ) % max_len
    if tmp_stop < tmp_start:
        asd = tmp_start
        tmp_start = tmp_stop
        tmp_stop = asd

    if tmp_start - tmp_stop == 0:
        get_rn_start_stop_val()

    return int(tmp_start), int(tmp_stop)

if __name__ == '__main__':
    separator = '|'
    rn.seed()
    out_file_name = 'Data_out/way_sim.out'
    print(f'** Way simulation started ** \n\tcurrent time {dt.datetime.now()}')
    while True:
        sleep( rn.random() * 10 % 3 )
        with open('Data_in/Lorem_ipsum.txt', 'r') as Lorem_descriptor:
            for lorem_line in Lorem_descriptor:
                start_index , stop_index = get_rn_start_stop_val()
                write_line(dt.datetime.now().__str__() + separator + lorem_line[start_index:stop_index], out_file_name)