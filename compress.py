#!/usr/bin/python3

import shutil
import os
from os import system
from os.path import join, basename, dirname


def zip(dir_, save_as=None, comp_sub_dir=False, pwd=None, delete=False):
	'''Zip a directory
	Params
		dir_: base_dir to zip
		save_as: save name of folder. use absolute dir to save to another location
		comp_sub_dir: compresss subdirectories(instead of main folder)
		pwd: encrypt with password
		delete: Delete [sub]folder after its compressed
	'''
	cmd = 'zip '
	folder = dir_
	file_name = basename(dir_)

	if save_as is None:
		save_as = dirname(dir_)

	if not pwd and not comp_sub_dir :
		shutil.make_archive(dir_, 'zip', dir_)
		return

	if pwd is not None:
		cmd += '-P ' + pwd

	new_relative_path = join(save_as, file_name)

	if comp_sub_dir is True:  # compress directory with sub-directories
		os.chdir(folder)
		files = []
		if not os.path.exists(new_relative_path):
			os.mkdir(new_relative_path)
		for fold in os.listdir():
			new_fold = join(folder, fold)  # absolute path of subdirectory
			if os.path.isdir(new_fold):
				sub_cmd = cmd + f' -r "{new_relative_path}/{fold}.zip" "{fold}"'
				system(sub_cmd)
				shutil.rmtree(fold)
				# print(sub_cmd)
				sub_cmd = cmd 
			else:
				files.append(new_fold)
		# compress the files
		cmd = '{cmd} "{name}" '.format(cmd=cmd, name=join(new_relative_path,file_name)+'_files.zip')
		# print(cmd)

		for file in files:
			cmd += f' "{file}" '
		system(cmd)
		shutil.rmtree(dir_)

	elif save_as == dir_:  # just single directory
		folder = dirname(dir_)
		os.chdir(folder)
		cmd += f' -r "{save_as}.zip" "{file_name}"'
		system(cmd)

	else:
		folder = dirname(dir_)
		os.chdir(folder)
		cmd += f' -r "{save_as}/{file_name}.zip" "{file_name}"'
		system(cmd)
