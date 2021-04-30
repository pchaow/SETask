#!/bin/python3


from inginious_container_api import feedback, input, run_student
from inginious_container_api.run_student import run_student_simple

studentfile = 'student/student.py'
template = 'template1.py'

thecode = input.parse_template(template, studentfile)
score = 0 
total = 3

# TEST 1
input1 = """3
5
2
"""
output1 = "5"


stdout, stderr, stdretval = run_student_simple(
    f"python3 {studentfile}",
    cmd_input=input1, 
    time_limit=30
    )

stdout = stdout.strip()


if stdout ==output1 :
    score += 1
    feedback.set_global_feedback("""CASE 1 : ถูกครับ
    
    """,append=True)
else :
    feedback.set_global_feedback("""CASE 1 : ผิดครับ

    """,append=True)


# TEST 2

input2 = """10
5
2
"""
output2 = "10"

stdout, stderr, stdretval = run_student_simple(
    f"python3 {studentfile}",
    cmd_input=input2, 
    time_limit=30
    )

stdout = stdout.strip()

if stdout == output2 :
    score += 1
    feedback.set_global_feedback("""CASE 2 : ถูกครับ

    """,append=True)
else :
    feedback.set_global_feedback("""CASE 2 : ผิดครับ

    """,append=True)


# TEST 3

input3 = """10
5
15
"""
output3 = "15"

stdout, stderr, stdretval = run_student_simple(
    f"python3 {studentfile}",
    cmd_input=input3, 
    time_limit=30
    )

stdout = stdout.strip()

if stdout == output3 :
    score += 1
    feedback.set_global_feedback("""CASE 3 : ถูกครับ

    """,append=True)
else :
    feedback.set_global_feedback("""CASE 3 : ผิดครับ

    """,append=True)



if score == total :
    feedback.set_grade(score/total*100)
    feedback.set_global_result("success") 
    feedback.set_global_feedback("""ถูกหมด เยี่ยมมากครับ!!""",append=True)

else :
    feedback.set_grade(score/total*100)
    feedback.set_global_result("failed") 



