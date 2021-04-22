#!/bin/python3

"""
ตัวอย่างสำหรับ task ที่มี subproblem == 1 
และมีโปรแกรมเฉลย

"""
import os
from inginious_container_api import feedback, input, run_student

input_dir = 'input'
output_dir = 'output'
template = 'template1.py'
studentfile = 'student/student.py'
teacherfile = 'student/answer1.py'
feedback_msg = """"""
problemiId = 'p1' #ยังไม่ได้ใช้เนื่องจากมี problemId เพียง 1 อัน


inputfiles = [f for f in os.listdir(input_dir) if f.endswith('.in')]
inputfiles.sort(key=lambda x : int(x.replace(".in","")))

score = 0
total_score = len(inputfiles)
all_correct = True



thecode = input.parse_template(template, studentfile)

for i in range(len(inputfiles)) :
    inputfile = inputfiles[i]
    file_input = open(f"{input_dir}/{inputfile}")
    input_text = file_input.read()
    file_input.close()


    stdout, stderr, stdretval = run_student.run_student_simple(f"python3 {studentfile}",cmd_input=input_text, time_limit=30)
    teacherOut, stderr, stdretval = run_student.run_student_simple(f"python3 {teacherfile}",cmd_input=input_text, time_limit=30)

    stdout = stdout.strip()
    output_text = teacherOut.strip()

    print(stdout)
    print(output_text)
    
    if stdout == output_text :
        feedback_msg += f"""CASE {i+1} : correct
        
        """
    else :
        all_correct = False
        feedback_msg += f"""CASE {i+1} : incorrect
        
        """

if all_correct :
    feedback.set_grade(100)
    feedback.set_global_result("success") 
    feedback.set_global_feedback("""All Correct. Well done!""")
else :
    feedback.set_grade(score/total_score*100)
    feedback.set_global_result("failed") 
    feedback.set_global_feedback(feedback_msg)
