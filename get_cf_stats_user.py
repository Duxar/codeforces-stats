import requests
import webbrowser, os.path
import json
import pprint

solved_problems = {}

def main():
	getSolvedProblems()

def writeToOutput(data):
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(data)

def clearData(problem):
	problem.pop('contestId', 'None')
	problem.pop('index', 'None')
	problem.pop('type', 'None')
	problem.pop('index', 'None')
	return problem

def getSolvedProblems():
	parameters = {'handle': 'Duxar', 'from': 1, 'count': 1000000000}
	user_submissions = requests.get("http://codeforces.com/api/user.status", params=parameters)
	user_submissions = json.loads(user_submissions.text)
	if user_submissions['status'] == 'OK':
		for submission in user_submissions['result']:
			if submission['verdict'] == 'OK':
				problem = submission['problem']

				contestId = problem['contestId']
				if contestId not in solved_problems:
					solved_problems[contestId] = {}

				index = problem['index']
				if index not in solved_problems[contestId]:
					solved_problems[contestId][index] = {}

				problem = clearData(problem)

				solved_problems[contestId][index] =  problem

		getSolvedCount()

def getSolvedCount():
	parameters = {'tags': ''}
	all_problems = requests.get("http://codeforces.com/api/problemset.problems", params=parameters)
	all_problems = json.loads(all_problems.text)
	if all_problems['status'] == 'OK':
		for problem_statistic in all_problems['result']['problemStatistics']:
			contestId = problem_statistic['contestId']
			index = problem_statistic['index']
			solved_count = problem_statistic['solvedCount']

			if contestId in solved_problems:
				if index in solved_problems[contestId]:
					solved_problems[contestId][index]['solvedCount'] = solved_count

	with open('contestant.json', 'w') as outfile:
	    json.dump(solved_problems, outfile)


if __name__ == '__main__':
	main()