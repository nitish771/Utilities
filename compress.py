#!/usr/bin/python3

import shutil
import os



def zip(dir_, save_as=None, comp_sub_dir=False, pwd=None):
	'''Zip a directory
	Params
		dir_: base_dir to zip
		save_as: save name of folder. use absolute dir to save to another location
	'''
	cmd = 'zip '
	folder = dir_
	file_name = os.path.basename(dir_)

	if save_as is None:
		save_as = os.path.dirname(dir_)

	if not pwd and not comp_sub_dir :
		shutil.make_archive(dir_, 'zip', dir_)
		return

	if pwd is not None:
		cmd += '-P ' + pwd


	if comp_sub_dir is True:  # compress directory with sub-directories
		os.chdir(folder)
		if not os.path.exists(save_as):
			os.mkdir(save_as)
		for fold in os.listdir():
			new_fold = folder + '/' + fold
			if os.path.isdir(new_fold):
				sub_cmd = cmd + f' -r "{save_as}/{fold}.zip" "{fold}"'
				os.system(sub_cmd)
				print(sub_cmd)
				sub_cmd = cmd 
	else:  # just single directory
		folder = os.path.dirname(dir_)
		os.chdir(folder)
		cmd += f' -r "{save_as}.zip" "{file_name}"'
		os.system(cmd)
