#!/usr/bin/python3

import shutil
import os



def zip(dir_, save_as, pwd=None):
	'''Zip a directory
	Params
		dir_: base_dir to zip
		save_as: save name of folder. use absolute dir to save to another location
	'''
	if pwd is not None:
		folder = os.path.dirname(dir_) # .split('/')[-1]
		print(folder)
		os.chdir(folder)
		folder = os.path.basename(dir_) # .split('/')[-1]
		cmd = f'zip -P {pwd} -r {save_as}.zip {folder}'
		os.system(cmd)
		return

	shutil.make_archive(save_as, 'zip', home_dir)
