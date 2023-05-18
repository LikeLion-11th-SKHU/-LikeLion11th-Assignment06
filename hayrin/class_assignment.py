class Student: #클래스 명 Student
    def __init__(self, name, schoolNum, semester, subject): # 속성
        self.name = name
        self.schoolNum = schoolNum
        self.semester = semester
        self.subject = subject

    def print_name(self):
        print(f'이름은 {self.name} 입니다.')
    
    def print_schoolNum(self): # schoolNum 슬라이싱한 겨롸를 통해 반환값 다르게 하기
        if self.schoolNum[5:6] == '1':
            print(f'학번은 {self.schoolNum}로 인문융합자율학부 소속입니다.')
        elif self.schoolNum[5:6] == '2':
            print(f'학번은 {self.schoolNum}로 사회융합자율학부 소속입니다.')
        elif self.schoolNum[5:6] == '3':
            print(f'학번은 {self.schoolNum}로 미디어융합자율학부 소속입니다.')
        elif self.schoolNum[5:6] == '4':
            print(f'학번은 {self.schoolNum}로 아이티융합자율학부 소속입니다.')
        else:
            print('오류입니다.')

    def print_semester(self):
        if self.semester <= 3:
            print(f'{self.semester}학기차인 {self.name}은 아직 전공선택 전입니다.')
        elif self.semester > 3:
            print(f'{self.name}은(는) {self.semester}학기차로 전공선택을 마쳤습니다.')


    def print_subject(self):
        print(f'{self.name}은(는) {self.subject}을(를) 수강합니다.')

    def subject_info(self):
        print("자세한 수강목록입니다.")
        for subject in self.subject:
            print(f'과목명: {subject} / 과목명의 길이: {len(subject)}') #딕셔너리 key, value

while True: # 반복문 while 사용
    class_name = input("객체 명을 입력하시오. (단, 영문으로) : ")
    if class_name == "종료":
        break

    name = input("이름을 입력하시오. (단, 한글로) : ")
    schoolNum = input("학번을 입력하시오: ") #무조건 9자리 !!
    while len(schoolNum) != 9:
        schoolNum = input("학번을 입력하시오: ")

    semester = int(input("학기를 입력하시오. (단, 숫자로) :"))

    subject_list=[] # 과목들을 담을 빈 리스트와 딕셔너리
    for i in range(3):
        subject = input("과목을 입력하시오. : ")
        if subject:
            subject_list.append(subject)
        else:
            break
    
    instance = Student(name, schoolNum, semester, subject_list)

    print() #가독성을 위해 한 줄

    instance.print_name()
    instance.print_schoolNum()
    instance.print_semester()
    instance.print_subject()
    print() #가독성을 위해 한 줄

    instance.subject_info()
    print() #가독성을 위해 한 줄
