

class Student : 
    # Student 클래스 정의

    def __init__(self, name, schoolNum, semester, subject):
        # __init__메서드로 생성자 구현        

        self.name = name
        self.schoolNum = schoolNum
        self.semester = semester
        self.subject = subject
        # 인스턴스(객체) 속성 초기화

    def print_name(self) :
        # print_name 메서드로 생성자 구현     
        print(f'이름은 {self.name}입니다.')
        # 포매팅을 이용해서 이름 출력

    def print_schoolNum(self):
        # print_schoolNum 메서드로 생성자 구현  
            if self.schoolNum[5:6] == "1": # 인덱스 범위 슬라이싱
                print(f"학번은 {self.schoolNum}로 인문융합자율학부 소속입니다.")
            elif self.schoolNum[5:6] == "2": 
                print(f"학번은 {self.schoolNum}로 사회융합자율학부 소속입니다.") 
            elif self.schoolNum[5:6] =="3": 
                print(f"학번은 {self.schoolNum}로 미디어융합자율학부 소속입니다.") 
            elif self.schoolNum[5:6] =="4":
                print(f"학번은 {self.schoolNum}로 IT융합자율학부 소속입니다.") 
            else:
                print(f"오류입니다.")
                # 슬라이싱 된 숫자에 따라 학부 구분, 이외의 숫자일 경우 오류라고 출력함.

    def print_semester(self):
        # print_semester 메서드로 생성자 구현
        if int(0 < self.semester < 4):
            print(f"{self.name}은(는){self.semester}학기차로 전공선택 전입니다.")  # 전공 선택 전
        elif int(3 < self.semester < 9):
            print(f"{self.name}은(는) {self.semester}학기차로 전공선택을 마쳤습니다.")  # 전공 선택 후
        else:
            print("오류입니다.")  # 오류 출력

    def print_subject(self):  # 수강 중인 과목 리스트 출력
        print(f'{self.subject}를 수강합니다.')



def subject_info(**subject_dict) :
    # 가변 인수 subjet_dict를 받아서 딕셔너리 언패킹으로 subject_info에 넣음   
    print('자세한 수강목록 입니다.')
    for key, value in subject_dict.items():
        print(f'과목명: {key} / 과목명의 길이: {value}')
            # 함수 출력, subject_dict를 각각 과목명(key)과 길이(value)에 저장해서 출력함

while True :
    class_name = input('객체명을 입력하시오. (단, 영문으로): ')
    if class_name == '종료' :
        break
            # '종료' 입력 시 while 루프 종료

    name = input('이름을 입력하시오. (단, 한글로):')
    schoolNum = input('학번을 입력하시오:')
    while len(schoolNum) != 9 :  
        print('9자리로 입력해야 합니다.')
        schoolNum = input('학번을 입력하시오:')
        # 학번이랑 이름을 입력하는데, 학번 길이가 9자리가 아니면 오류 메시지가 뜸. 그럴 경우 다시 입력함(while)
    semester = int(input('학기를 입력하시오. (단, 숫자로): '))
        # 학기 입력
    subject_list = []
    subject_dict = {}
    # 과목을 저장하는 list와 과목명, 과목길이를 저장한 딕셔너리
    for _ in range(3) :
        subject = input('과목을 입력하시오: ')
        subject_list.append(subject)
        subject_dict[subject] = len(subject)
            # 과목 3개 반복(for) 입력(range), 과목은 list에 저장하고 글자 길이는 dict에 저장함 

    print()

    class_name = Student(name, schoolNum, semester, subject_list)
    # 객체 초기화
    class_name.print_name()
    class_name.print_schoolNum()
    class_name.print_semester()
    class_name.print_subject()
        # 객체 메서드를 부르고 출력

    print()

    subject_info(**subject_dict)
                # 자세한 수강 목록 출력

    print()
