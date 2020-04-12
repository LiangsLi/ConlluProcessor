# -*- coding: utf-8 -*-
# Created by li huayong on 2020/4/10
import pathlib
import sys
sys.path.append('..')
from conlluprocessor import semeval16_to_conllu, conllu_to_semeval16


def main():
    data_dir = '/home/liangs/MyCodes/doing_codes/CSDP_Biaffine_Parser_lhy/CSDP_Biaffine_Parser_lhy/dataset/SemEval-2016-master/test'
    data_dir = pathlib.Path(data_dir)
    for file in data_dir.glob('*.conll'):
        semeval16_to_conllu(str(file), f'{str(data_dir / (str(file.name) + ".conllu"))}')


if __name__ == '__main__':
    main()
