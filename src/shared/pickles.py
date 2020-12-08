import subprocess
from pathlib import Path
import time
import json
import pickle

def get_csv():
	result = subprocess.check_output('ls ../datasets/wheather-dataset/*.csv',shell=True)
	csv_list = result.decode().split('\n')
	csv_list = csv_list[:len(csv_list)-1]
	print(f"{len(csv_list)} Archivos a leer \nCSV: \n{csv_list}")
	return csv_list

def build_path(name_file):
	root = Path('').resolve().as_posix()
	final_path = root + '/' + name_file
	print(final_path)
	return final_path

def get_name_csv(csv):
	parts = csv.split('/')
	name = parts[len(parts)-1]
	return name

def dump_file(data,name):
	with open(name, "wb") as a_file:
		pickle.dump(data, a_file, protocol=pickle.HIGHEST_PROTOCOL)
		a_file.close()

def get_dump(name):

	with open(name, "rb") as a_file:
		output = pickle.load(a_file)
		print(output)
		return output

if __name__ == '__main__':
	"""csv_list = get_csv()
	#print(csv_list)
	csv = [get_name_csv(town) for town in csv_list]
	print(csv)
	dump_file(csv,'csv_towns_names.pickle')"""

	towns = get_dump('csv_towns_names.pickle')
	print(len(towns))