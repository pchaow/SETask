from inginious_container_api import input,run_student,feedback

input.parse_template("template.py","student/studentcode.py")
input.parse_template('teachercode.py','student/teachercode.py')
student_output , student_err, _ = run_student.run_student_simple("python3 student/studentcode.py")
teacher_output, teacher_err, _ = run_student.run_student_simple("python3 student/teachercode.py")

print(student_output,student_err)
print(teacher_output,teacher_err)


if student_output == teacher_output:
    # The student succeeded
    feedback.set_global_result("success")
    feedback.set_global_feedback("You solved this difficult task!")
else:
    # The student succeeded
    feedback.set_global_result("failed")
    if(student_err) :
        feedback.set_global_feedback("There are Errors" + student_err)
    else :
        feedback.set_global_feedback("Your output is not correct : " + student_output)

