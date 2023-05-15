class Student: # Student 클래스
    def __init__(self, name, schoolNum, semester, subject): # 인스턴스를 만드는 __init__ 메소드로 속성 만듦 = 생성자
                                                            # 매개변수 self는 인스턴스(객체) 자신 을 의미 = Student
                                                            #                관례적으로 파이썬 첫 번째 매개변수 
                                                            #                객체 호출시 객체 자신이 전달 
                                                            # 메소드의 매개변수이면서 클래스 속성값 name, schoolNum, semester, subject
                                                                                                    
        self.name = name # name 매개변수 값을 Student.name 인스턴스 변수에 저장
        self.schoolNum = schoolNum # schoolNum 매개변수 값을 Student.schoolNum 인스턴스 변수에 저장
        self.semester = semester # semester 매개변수 값을 Student.semester 인스턴스 변수에 저장
        self.subject = subject # subject 매개변수 값을 Student.subject 인스턴스 변수에 저장

    def print_name(self): # 이름을 출력하는 메소드
        print(f"이름은 {self.name}입니다.") # 포매팅 사용해서 출력 (중괄호{} 안에 self.name 넣어서 문자열에 포함)

    def print_schoolNum(self): # 학번으로 소속 학부 출력하는 메소드 (슬라이싱 사용으로 반환 결과를 다르게 함)
        if self.schoolNum[5:6] == "1": # 학번 6번째 숫자가 1일 때 
            print(f"학번은 {self.schoolNum}로 인문융합자율학부 소속입니다.") # 포매팅 사용해서 반환
        elif self.schoolNum[5:6] == "2": 
            print(f"학번은 {self.schoolNum}로 사회융합자율학부 소속입니다.") 
        elif self.schoolNum[5:6] =="3": 
            print(f"학번은 {self.schoolNum}로 미디어융합자율학부 소속입니다.") 
        elif self.schoolNum[5:6] =="4":
            print(f"학번은 {self.schoolNum}로 IT융합자율학부 소속입니다.") 
        else: # 그 외
            print(f"오류입니다.\n") # 오류

   def print_semester(self): # 학기를 출력하는 메소드
        if self.semester <= 3: # 3학기차 까지는 (정수로 입력받음) 
            print(f"{self.semester}학기차인 {self.name}은(는) 아직 전공선택 전입니다.")
        elif self.semester >= 4: # 4학기차 이상은
            print(f"{self.name}은(는) {self.semester}학기차로 전공선택을 마쳤습니다.") 
        else: 
            print(f"오류입니다")

    def print_subject(self): # 수강 과목을 출력하는 메소드 (과목 리스트 포함 문자열 반환)
        print(f"{self.subject}를 수강합니다.")

def subject_info(**subject_dict): # 딕셔너리 언패킹으로 수강 과목 출력
    print("자세한 수강 목록입니다.")
    for subject, length in subject_dict.items(): # 과목 이름(key)은 변수 subject, 이름 길이(value)는 변수 length에 저장 
        print(f"과목명: {subject} / 과목명의 길이 : {length}") # 반복문대로 출력

while True:  # while 반복문
    class_name = input("객체 명을 입력하시오. (단, 영문으로) : ") # 입력 받은 객체 명을 class_name 변수에 저장
    if class_name == "종료": # 입력받은 값이 "종료"일 경우
        break  # 반복문 빠져나감    

    name = input("이름을 입력하시오. (단, 한글로) : ") # 입력 받은 이름을 name 변수에 저장
    schoolNum = input("학번을 입력하시오: ") # 입력 받은 학번은 schoolNum 변수에 저장
    while len(schoolNum) != 9: # 학번은 무조건 9자리이므로 입력된 학번 길이가 9가 아닐 때 반복
        print("오류입니다.\n") 
        schoolNum = input("학번을 입력하시오 : ") # 새로 입력 받은 학번을 schoolNum 변수에 저장

    semester = int(input("학기를 입력하시오. (단, 숫자로) : ")) # 정수로 입력받기 위한 int
    subject_list = [] # 과목을 저장할 리스트
    subject_dict = {} # 과목, 과목 이름 길이 저장할 딕셔너리

    for _ in range(3): # 3번 반복하는 for문
        subject = input("과목을 입력하시오 : ") # 입력 받은 과목을 subject 변수에 저장
        subject_list.append(subject) # 입력 받은 과목 이름을 subject_list에 추가
        subject_dict[subject] = len(subject) # 입력 받은 과목들을 key로 하고, 해당 과목의 길이를 value로 해서 subject_list에 추가
    print()

    class_name = Student(name, schoolNum, semester, subject_list) # Student 객체 생성

    # Student 객체의 메소드를 호출(이름, 학번, 학기, 수강 과목)   
    class_name.print_name()  
    class_name.print_schoolNum() 
    class_name.print_semester() 
    class_name.print_subject()
    print()

    subject_info(**subject_dict) # subject_dict를 인자로 전달하고 subject_info 함수 호출(자세한 수강 목록)
    print()
