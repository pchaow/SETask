from inginious_container_api import feedback, input, run_student

total_score = 1
score = 0

def checkAnswer(problemId, 
                template="template.py",
                studentfile="student/student.py",
                teacherfile="student/answer.py",
                inputfile=None) :
    
    thecode = input.parse_template(template, studentfile)
    
    
       
    if inputfile == None :
        stdout, stderr, stdretval = run_student.run_student_simple(f"python3 {studentfile}", time_limit=30)
        tchout, tcherr, tchretval = run_student.run_student_simple(f"python3 {teacherfile}", time_limit=30)
    else :
        
        f = open(inputfile)
        text = f.read()
        f.close()
        
        stdout, stderr, stdretval = run_student.run_student_simple(f"python3 {studentfile}",cmd_input=text, time_limit=30)
        tchout, tcherr, tchretval = run_student.run_student_simple(f"python3 {teacherfile}",cmd_input=text, time_limit=30)

        
    print(stdout,stderr)
    print(tchout,tcherr)
    

    if stderr :
        feedback.set_problem_result("failed", problemId)
        feedback.set_problem_feedback(
            f"""{stderr}""", problemId)

    elif stdout != tchout: # Wrong Answer 
        feedback.set_problem_result("failed", problemId)
        feedback.set_problem_feedback(f"Your Output : {stdout} ", problemId)

    else :
        feedback.set_problem_result("success", problemId)
        feedback.set_problem_feedback(f"Your Output : {stdout} ", problemId)
        return 1

    return 0


score += checkAnswer("p1",template="template1.py",studentfile="student/p1.py",teacherfile="student/answer1.py",
                    inputfile="input/input1.txt")


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
