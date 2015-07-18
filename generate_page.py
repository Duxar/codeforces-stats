import requests
import webbrowser, os.path
import json
import pprint
import matplotlib.pyplot as plt

tags_stat = {}
solved_cnt_list = []
indices = 1

def writeToOutput(data):
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(data)

def main():
	with open('contestant.json') as data_file:
	    stats = json.load(data_file)

	for contest in stats:
		for index in stats[contest]:
			if 'solvedCount' in stats[contest][index]:
				solved_cnt_list.append(stats[contest][index]['solvedCount'])
				tags = stats[contest][index]['tags']
				for tag in tags:
					if tag not in tags_stat:
						tags_stat[tag] = 0;
					tags_stat[tag] += 1
	print (len(solved_cnt_list))
	writeToOutput(tags_stat)
	solved_cnt_list.sort(reverse=True)
	plt.plot(solved_cnt_list)
	plt.ylabel('solved count')
	plt.show()


if __name__ == '__main__':
	main()