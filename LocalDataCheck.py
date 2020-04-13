#coding=utf-8

import sys
import os
import os.path
import zipfile

def get_file_list(dest_path='.', file_type='.zip'):
	""""""
	files = os.scandir(dest_path)
	file_type_list = []
	for file in files:
		if os.path.splitext(file)[1] == file_type:
			file_type_list.append(file)

	return file_type_list

def unzip_single_file(src_file, dest_dir, password=None):
	""""""
	if password:
		password = password.encode()
	zf = zipfile.ZipFile(src_file)
	try:
		zf.extractall(path=dest_dir, pwd=password)
	except RuntimeError as e:
		print(e)
	zf.close()


def run():
	""""""
	for zip_file in get_file_list():
		unzip_single_file(zip_file, './unzip_dir')

if __name__ == '__main__':
	run()
