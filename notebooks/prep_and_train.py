import json
import os
import string
import unicodedata
import utils

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "--gpu",
        default="0,1",
        type=str,
        help="The GPUs to use."
    )
    
    args = parser.parse_args()

    import subprocess
    
    command = 'ls -l'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print("output:")
    print(output)
    print("error:")
    print(error)

    command = 'git clone https://github.com/salesforce/WikiSQL'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print("output:")
    print(output)
    print("error:")
    print(error)

    command_list = ['bash', '-c', 'cd WikiSQL; tar xvjf data.tar.bz2']
    process = subprocess.Popen(command_list, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print("output:")
    print(output)
    print("error:")
    print(error)
    
    command_list = ['bash', '-c', 'mkdir data; cd data; mv ../WikiSQL/data wikisql']
    process = subprocess.Popen(command_list, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print("output:")
    print(output)
    print("error:")
    print(error)

    command = 'ls -l data'
    process = subprocess.Popen(command.split())
    exit_code = process.wait()
    print("exit_code:")
    print(exit_code)

    print("args.gpu:")
    print(args.gpu)
                
    command = 'python wikisql_gendata.py'
    process = subprocess.Popen(command.split())
    exit_code = process.wait()
    print("exit_code:")
    print(exit_code)

    command = 'python main.py train --conf conf/wikisql.conf --gpu ' + args.gpu + ' --note "ND40rs_v2"'
    print("command:")
    print(command)
    process = subprocess.Popen(command.split())
    exit_code = process.wait()
    print("exit_code:")
    print(exit_code)
