import datetime as dt
import random as rn
import sys
from time import sleep
import time
import shutil


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

def generate_new_name(base_part = 'way_sim'):
    new_name = base_part + '_' + dt.date.today().year.__str__()

    if dt.date.today().month < 10:
        tmp = new_name + '0' + dt.date.today().month.__str__()
    else:
        tmp = new_name + dt.date.today().month.__str__()

    if dt.date.today().day < 10:
        new_name = new_name + '0' + dt.date.today().day.__str__()
    else:
        new_name = new_name + dt.date.today().day.__str__()

    random_name_part =  int(rn.random() * 100000).__str__()
    new_name += random_name_part + '.out'
    return new_name

if __name__ == '__main__':
    separator = '|'
    log_line_sleep_interval = 3
    change_interval = 1.0
    current_file_name = 'Data_out/way_sim'

    rn.seed()
    print(f'** Way simulation started ** \n\tcurrent time {dt.datetime.now()}')

    while True:
        last_name_change = time.time() + change_interval
        sleep( rn.random() * 10 % log_line_sleep_interval )
        if time.time() > last_name_change:
            shutil.move(current_file_name, generate_new_name(current_file_name))
            print(f'\t-> File name changed: {dt.datetime.now()}')

        with open('Data_in/Lorem_ipsum.txt', 'r') as Lorem_descriptor:
            for lorem_line in Lorem_descriptor:
                start_index , stop_index = get_rn_start_stop_val()
                write_line(dt.datetime.now().__str__() + separator + lorem_line[start_index:stop_index], out_file_name = current_file_name)