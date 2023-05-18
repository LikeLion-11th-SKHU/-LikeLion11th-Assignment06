class Student :
    # 생성자를 선언해 줍니다. 여기서, self는 매개변수로서 Student에 해당합니다.
    def __init__(self, name, schoolNum, semester, subject):
        self.name = name # 이름을 초기화 합니다. 즉, 매개변수 값을 Student.name 에 저장한 것 입니다.
        self.schoolNum = schoolNum # 학번을 초기화 합니다. 즉, 매개변수 값을 Student.schoolNum 에 저장한 것 입니다.
        self.semester = semester # 학기를 초기화 합니다. 즉, 매개변수 값을 Student.semester 에 저장한 것 입니다.
        self.subject = subject # 과목을 초기화 합니다. 즉, 매개변수 값을 Student.subject 에 저장한 것 입니다.
    
    # 이름을 출력합니다.
    def print_name(self): 
        print(f"이름은 {self.name}입니다.") # 중괄호{} 안에 self.name 넣어서 문자열에 포함시킵니다.

    def print_schoolNum(self): # 학번을 통해 소속학부를 알아내는 입력 방식입니다. 
        if self.schoolNum[5:6] == "1": # 만약에 학번의 6번째 숫자가 1이라면 
            print(f"학번은 {self.schoolNum}로 인문융합자율학부 소속입니다.") 
        elif self.schoolNum[5:6] == "2": #2이라면
            print(f"학번은 {self.schoolNum}로 사회융합자율학부 소속입니다.") 
        elif self.schoolNum[5:6] =="3": # 3이라면
            print(f"학번은 {self.schoolNum}로 미디어융합자율학부 소속입니다.") 
        elif self.schoolNum[5:6] =="4": # 4이라면
            print(f"학번은 {self.schoolNum}로 IT융합자율학부 소속입니다.") 
        else: # 그 외 라면
            return(f"오류입니다.\n") # 오류를 나타냅니다.

    def print_semester(self): # 학기를 출력하는 메소드입니다.
        if self.semester <= 3: # 3학기 이하까지는 
            print(f"{self.semester}학기차인 {self.name}은(는) 아직 전공선택 전입니다.")
        elif self.semester >= 4: # 4학기차 이상부터는
            print(f"{self.name}은(는) {self.semester}학기차로 전공선택을 마쳤습니다.") 
        else: 
            print(f"오류입니다") # 오류를 나타냅니다.
        
    def print_subject(self): # 수강 과목을 출력하는 메소드입니다.
        print(f"{self.subject}를 수강합니다.")

def subject_info(**subject_dict): # 수강 과목 출력합니다.(딕셔녀링 언패킹)
    print("자세한 수강 목록입니다.")
    for subject, length in subject_dict.items(): # 딕셔너리의 요소를 통해 키(과목명)과 value(과목명의 길이) 출력합니다.
        print(f"과목명: {subject} / 과목명의 길이 : {length}") 

while True:  # 반복문(while)입니다.
    class_name = input("객체 명을 입력하시오. (단, 영문으로) : ") # 객체 명을 class_name 에 저장합니다.
    if class_name == "종료": # "종료"일 경우를 명시합니다.
        break  # 반복문을 빠져나가는 것입니다.    

    name = input("이름을 입력하시오. (단, 한글로) : ") # 이름을 name 에 저장합니다.
    schoolNum = input("학번을 입력하시오: ") # 학번은 schoolNum 에 저장합니다.
    while len(schoolNum) != 9: # 학번 길이가 9가 입력되지 않았을 시 반복합니다. 
        print("오류입니다.\n") # 이때, 오류 메세지가 나타나게 합니다.
        schoolNum = input("학번을 입력하시오 : ") # 재입력한 학번을 schoolNum 에 저장합니다.

    semester = int(input("학기를 입력하시오. (단, 숫자로) : ")) # 학기를 입력하고, int 를 작성하여 정수로 인정받습니다.
    subject_list = [] # 과목을 저장할 리스트입니다.
    subject_dict = {} # 과목을 저장할 딕셔너리입니다.

    # 반복문 (for) 을 이용하여 과목을 3가지 입력 받아줍니다.
    for _ in range(3): 
        subject = input("과목을 입력하시오 : ") # 입력 받은 과목을 subject에 저장합니다.
        subject_list.append(subject) # 입력 받은 과목 이름을 subject_list에 저장합니다.
        subject_dict[subject] = len(subject) # 입력 받은 과목들을 subject_dict에 저장합니다.
    print()
    
    class_name = Student(name, schoolNum, semester, subject_list) # Student 객체를 만듭니다.

    # 이름, 학번, 학기, 수강 과목의 Student 객체를 호출합니다.
    class_name.print_name()
    class_name.print_schoolNum() 
    class_name.print_semester() 
    class_name.print_subject()
    print()

    subject_info(**subject_dict) # 과목 정보를 출력합니다.
    print()