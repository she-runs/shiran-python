
def compare_subjects_within_student(subj1_all_students, subj2_all_students):
	"""
	Compare the two subjects with their students and print out the "preferred"
	subject for each student. Single-subject students shouldn't be printed.
	"""
	for student in subj1_all_students:
		if student in subj2_all_students:
			if max(subj1_all_students[student])> max(subj2_all_students[student]):
				print "%s's better subject is: subject1" % student
			elif max(subj1_all_students[student])< max(subj2_all_students[student]):
				print "%s's better subject is: subject2" % student
			else:
				print "%s have same max grades in subject1 and subject2" % student
	

subj1_all_students= {"Jack": [80, 75], "Dan": [85,90], "Ben": [70,80], "Ran":[90, 100], "Tal":[100,90]}
subj2_all_students= {"Jack": [70, 75], "Dan": [95,90], "Lee": [90,80], "Ben": [75,75], "Tal":[90,100]}

compare_subjects_within_student(subj1_all_students, subj2_all_students)