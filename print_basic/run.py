from inginious_container_api import feedback, input, run_student

total_score = 2
score = 0

#Problem 1
thecode = input.parse_template("template.py", "student/student.py")
stdout, stderr, stdretval = run_student.run_student_simple("python3 student/student.py", time_limit=30)
tchout, tcherr, tchretval = run_student.run_student_simple("python3 student/teacher.py", time_limit=30)

#Check Error
if stderr :
    feedback.set_problem_result("failed", "p1")
    feedback.set_problem_feedback(
        f"""{stderr}""", "p1")

elif stdout != tchout: # Wrong Answer 
    feedback.set_problem_result("failed", "p1")
    feedback.set_problem_feedback(f"Your Output : {stdout} ", "p1")

else :
    feedback.set_problem_result("success", "p1")
    feedback.set_problem_feedback(f"Your Output : {stdout} ", "p1")
    score += 1

#Problem 2

#Parse Problem p1
thecode = input.parse_template("template2.py", "student/student2.py")
stdout, stderr, stdretval = run_student.run_student_simple("python3 student/student2.py", time_limit=30)
tchout, tcherr, tchretval = run_student.run_student_simple("python3 student/teacher2.py", time_limit=30)

#Check Error
if stderr :
    feedback.set_problem_result("failed", "p2")
    feedback.set_problem_feedback(
        f"""{stderr}""", "p2")

elif stdout != tchout: # Wrong Answer 
    feedback.set_problem_result("failed", "p2")
    feedback.set_problem_feedback(f"Your Output : {stdout} ", "p2")

else :
    feedback.set_problem_result("success", "p2")
    feedback.set_problem_feedback(f"Your Output : {stdout} ", "p2")
    score += 1


#calculate total score
if score == total_score :
    feedback.set_grade(100)
    feedback.set_global_result("success") 
    feedback.set_global_feedback("""All Correct. Well done!""")
    
else :
    feedback.set_grade(score/total_score*100)
    feedback.set_global_result("failed") 
    
    feedback.set_global_feedback(
    """There are something wrong.
    Try again!!.""")


