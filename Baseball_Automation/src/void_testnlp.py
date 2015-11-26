# -*- coding: utf-8 -*-

# File Read and Get Data
article = open("sample.txt", "r")
textline = article.readline()
line_num = 1
Apitcherflag = False
Bpitcherflag = False

A_pitcher_inning = 0
A_pitcher_lost = 0
A_pitcher_name = ''
A_pitcher_k = 0
A_bullpen_inning = 0
A_bullpen_lost = 0
B_pitcher_inning = 0
B_pitcher_lost = 0
B_pitcher_name = ''
B_pitcher_k = 0
B_bullpen_inning = 0
B_bullpen_lost = 0

A_attack = []
A_attack_list = []

B_best_attack_num = ''
B_best_attack_name = ''
B_best_attack_pos = ''
B_best_attack_tan = 0
B_best_attack_anta = 0
B_best_attack_ta = 0
B_best_attack_home = 0

while textline:
	if line_num == 1:
		if textline.split()[4] > textline.split()[5]:
			A_name = textline.split()[1]
			B_name = textline.split()[3]
			A_score = textline.split()[4]
			B_score = textline.split()[5]
		else:
			A_name = textline.split()[3]
			B_name = textline.split()[1]
			A_score = textline.split()[5]
			B_score = textline.split()[4]

	if '투구수' in textline and Apitcherflag == False:		
		line_num = line_num + 1
		textline = article.readline()
		A_pitcher_inning = textline.split()[1]
		A_pitcher_lost = textline.split()[7]
		A_pitcher_name = textline.split()[0]
		A_pitcher_k = textline.split()[6]

		line_num = line_num + 1
		textline = article.readline()
		while 1:
			if '타순' not in textline:
				A_bullpen_inning = A_bullpen_inning + float(textline.split()[1])
				A_bullpen_lost = A_bullpen_lost + float(textline.split()[7])
				line_num = line_num + 1
				textline = article.readline()
			else:
				break

		line_num = line_num + 1
		textline = article.readline()
		while 1:
			if '이닝' not in textline:
				A_attack.append(textline.split()[1])
				A_attack.append(textline.split()[0])
				A_attack.append(textline.split()[2])
				A_attack.append(textline.split()[3])
				A_attack.append(textline.split()[5])
				A_attack.append(textline.split()[6])
				A_attack.append(textline.split()[7])
				A_attack_list.append(tuple(A_attack))
				A_attack = []
				line_num = line_num + 1
				textline = article.readline()
			else:
				break
		"""
		for eleme in A_attack_list:
			print eleme[0]
		"""
		Apitcherflag = True

	elif Bpitcherflag == False and Apitcherflag == True:
		B_pitcher_inning = textline.split()[1]
		B_pitcher_lost = textline.split()[7]
		B_pitcher_name = textline.split()[0]
		B_pitcher_k = textline.split()[6]

		line_num = line_num + 1
		textline = article.readline()
		while 1:
			if '타순' not in textline:
				B_bullpen_inning = B_bullpen_inning + float(textline.split()[1])
				B_bullpen_lost = B_bullpen_lost + float(textline.split()[7])
				line_num = line_num + 1
				textline = article.readline()
			else:
				break


		line_num = line_num + 1
		textline = article.readline()
		
		while 1:
			if 'LineUp' not in textline:
				if float(textline.split()[6]) > float(B_best_attack_ta):
					B_best_attack_num = textline.split()[0]
					B_best_attack_name = textline.split()[1]
					B_best_attack_pos = textline.split()[2]
					B_best_attack_tan = textline.split()[3]
					B_best_attack_anta = textline.split()[5]
					B_best_attack_ta = textline.split()[6]
					B_best_attack_home = textline.split()[7]
				elif float(textline.split()[6]) == float(B_best_attack_ta):
					if float(textline.split()[5])/float(textline.split()[6]) > float(B_best_attack_anta)/float(B_best_attack_anta):
						B_best_attack_num = textline.split()[0]
						B_best_attack_name = textline.split()[1]
						B_best_attack_pos = textline.split()[2]
						B_best_attack_tan = textline.split()[3]
						B_best_attack_anta = textline.split()[5]
						B_best_attack_ta = textline.split()[6]
						B_best_attack_home = textline.split()[7]

				line_num = line_num + 1
				textline = article.readline()
			else:
				break
		Bpitcherflag = True

	line_num = line_num + 1
	textline = article.readline()
#	if '이름'　in textline
"""
print "--"
print A_name
print A_score
print B_name
print B_score
print "--"
print A_pitcher_inning
print A_pitcher_lost
print A_pitcher_name
print A_pitcher_k
print B_pitcher_inning
print B_pitcher_lost
print B_pitcher_name
print B_pitcher_k
print "--"
print A_bullpen_inning
print A_bullpen_lost
print B_bullpen_inning
print B_bullpen_lost

print B_best_attack_name
"""
"""
# Winner Team
A_name
A_score 
a_pitcher_inning =
a_pitcher_lost =
a_pitcher_name =
a_pitcher_k =
A_bullpen_inning =
A_bullpen_lost =
#A_save_inning =

3A_save_lost =

A_team_attack_data_list

# Loser Team
B_name =
B_score =
B_pitcher_name =
B_pitcher_inning =
B_pitcher_lost =
B_pitcher_k =
B_bullpen_inning =
B_bullpen_lost

# Name Of Loser Team
B_team_top_attacker



# Sentence 1 (Team Name + Score + Result)
# Team Name
TeamNameS = ['넥센이', '두산이', 'NC가', '한화가', '삼성이', 'LG가', 'SK가', '롯데가', '기아가', 'kt가']
TeamNameO = ['넥센을', '두산을', 'NC를', '한화를', '삼성을', 'LG를', 'SK를', '롯데를', '기아를', 'kt를']

# Score
Score = ['으로', '로', '로', '으로', '로', '로', '으로', '로', '로', '로']

# Result
Result = ['승리했다.']
"""
