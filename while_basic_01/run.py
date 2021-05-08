import math
import random
thecode =  parse_template("p1.py","student/student.py")
a = 43*27*6
b = 27*3*101
input_text = f"""{a}
{b}
"""
expected = f"""{math.gcd(a,b)}"""
stdout, stderr, retval = run_student_simple("python3 student/student.py",cmd_input=input_text)

#TEST
if stdout.strip() == expected.strip() :
    set_global_feedback("""ถูกต้องแล้วครับ

    """,append=True)
    set_global_result("success")
    set_grade(100)

else :

    set_global_feedback("""ยังไม่ถูกนะ
    """,append=True)
    set_global_result("failed")


    #CODE
    codefile = open("student/student.py","r")
    thecode = codefile.read()
    codefile.close()

    codeblock = get_codeblock("python", thecode)
    set_global_feedback("""**CODE**""",True)
    set_global_feedback(codeblock, True) # Appends the codeblock to the global feedback

    #INPUT
    inputblock = get_codeblock("raw",input_text)
    set_global_feedback("""**INPUT**""",True)
    set_global_feedback(inputblock, True) # Appends the codeblock to the global feedback


    #OUTPUT
    outputblock = get_codeblock("raw", stdout)
    set_global_feedback("""**OUTPUT**""",True)
    set_global_feedback(outputblock, True) # Appends the codeblock to the global feedback

    #Expected
    expectedblock = get_codeblock("raw", expected)
    set_global_feedback("""**Expected**""",True)
    set_global_feedback(expectedblock, True) # Appends the codeblock to the global feedback

    #ERROR

    if stderr :
        errorblock = get_codeblock("raw", "NO Error" if stderr == "" else stderr)
        set_global_feedback("""**Error**""",True)
        set_global_feedback(errorblock, True) # Appends the codeblock to the global feedback

