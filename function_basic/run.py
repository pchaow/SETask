#!/bin/inginious-ipython

def get_text_from_file(file) :
    f = open(file,"r")
    output = f.read()
    f.close()
    return output

class RunResult :
    student_output : str  = ''
    student_error : str = ''
    input_text : str = ''
    output_text :  str = ''
    is_correct : bool = False

    def __init__(self,input_text,output_text,student_output,student_error) :
        self.input_text = input_text.strip()
        self.output_text = output_text.strip()
        self.student_output = student_output.strip()
        self.student_error = student_error.strip()
        self.is_correct = self.student_error == '' and (self.student_output == self.output_text)

try :
    thecode =  parse_template("p1.py","student/student.py")

    result = []
    testcases = [
        1,2
    ]
    for i in testcases :
        input_text = get_text_from_file(f'testcases/{i}.in')
        output_text = get_text_from_file(f'testcases/{i}.out')
        stdout, stderr, retval = run_student_simple("python3 student/student.py",cmd_input=input_text)
        stdout = stdout.strip()
        result.append(RunResult(input_text,output_text,stdout,stderr))

    if all([ r.is_correct for r in result]) :
        set_global_result('success')
        set_global_feedback("ถูกต้องครับ")
        set_grade(100)
    else :
        set_global_feedback('failed')
        set_global_feedback("ยังมีที่ผิดอยู่นะ")

        correctResult = [r for r in result if r.is_correct == True]
        incorrectResult = [r for r in result if r.is_correct == False]

        set_grade(len(correctResult)/len(result) * 100)

        for r in incorrectResult :

            #INPUT
            inputblock = get_codeblock("raw",r.input_text)
            set_global_feedback("""**INPUT**""",True)
            set_global_feedback(inputblock, True) # Appends the codeblock to the global feedback


            #OUTPUT
            outputblock = get_codeblock("raw", r.student_output)
            set_global_feedback("""**OUTPUT**""",True)
            set_global_feedback(outputblock, True) # Appends the codeblock to the global feedback

            #Expected
            expectedblock = get_codeblock("raw", r.output_text)
            set_global_feedback("""**Expected**""",True)
            set_global_feedback(expectedblock, True) # Appends the codeblock to the global feedback


            #Error 
            stderr = get_codeblock("python", r.student_error)
            set_global_feedback("""**ERROR (Contact Administrator)**""",True)
            set_global_result('failed')
            set_global_feedback(stderr, True) # Appends the codeblock to the global feedback

            break

except Exception as e:
    print(e)
    graderError = get_codeblock("python", e)
    set_global_feedback("""**Grader ERROR (Contact Administrator)**""",True)
    set_global_result('failed')
    set_global_feedback(graderError, True) # Appends the codeblock to the global feedback

