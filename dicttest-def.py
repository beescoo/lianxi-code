#!/usr/bin/env python3

import sys
output_dict = {}

def handle_date(arg):
    arg_list = arg.split(':')
    arg_tuple = (arg_list[0],arg_list[1])
    key = arg_list[0]#zheli weisha cuo 
    output_dict[key] = arg_list[1]

def print_date(key,output_dict_key_):
    for key,output_dict_key_ in output_dict.items():
        print('ID:{} Name:{}'.format(key,output_dict[key]))

if __name__ =='__main__':

    for arg in sys.argv[1:]:
        handle_date(arg)

    for key in output_dict:
        print_date(key,output_dict[key])