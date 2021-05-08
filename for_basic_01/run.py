#!/bin/inginious-ipython

try :
    thecode =  parse_template("p1.py","student/student.py")
    result_set = []


    testcases = [
        ('1.in','1.out'),
        ('2.in','2.out')
        ]

    for case in testcases :

        input_file = open(f"testcases/{case[0]}")
        output_file =open(f"testcases/{case[1]}") 

        input_str =  input_file.read().strip()
        output_str = output_file.read().strip()

        stdout, stderr, retval = run_student_simple("python3 student/student.py",cmd_input=input_str)
        stdout = stdout.strip()

        result_set.append( (output_str,stdout) )

        if output_str != stdout :
            #ERROR
            if stderr :
                errorblock = get_codeblock("raw", "NO Error" if stderr == "" else stderr)
                set_global_feedback("""**Error**""",True)
                set_global_feedback(errorblock, True) # Appends the codeblock to the global feedback
                break

            #INPUT
            inputblock = get_codeblock("raw",input_str)
            set_global_feedback("""**INPUT**""",True)
            set_global_feedback(inputblock, True) # Appends the codeblock to the global feedback


            #OUTPUT
            outputblock = get_codeblock("raw", stdout)
            set_global_feedback("""**OUTPUT**""",True)
            set_global_feedback(outputblock, True) # Appends the codeblock to the global feedback

            #Expected
            expectedblock = get_codeblock("raw", output_str)
            set_global_feedback("""**Expected**""",True)
            set_global_feedback(expectedblock, True) # Appends the codeblock to the global feedback



    if all([x[0] == x[1] for x in result_set]) :
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

except Exception as e:
    graderError = get_codeblock("python", e)
    set_global_feedback("""**Grader ERROR**""",True)
    set_global_feedback(graderError, True) # Appends the codeblock to the global feedback
   