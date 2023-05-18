class Student:  # Student 클래스 생성
    def __init__(self, name, schoolNum, semester, subject):  # 생성자를 이용한 객체 생성시 초기화
        self.name = name  # 객체 name속성 초기화
        self.schoolNum = schoolNum  # 객체 schoolNum속성 초기화
        self.semester = semester  # 객체 semester속성 초기화
        self.subject = subject  # 객체 subject속성 초기화

    def print_name(self):  # print_name 메서드 생성
        print(f"이름은 {self.name}입니다.")  # 포매팅을 이용해 객체의 이름을 출력

    def print_schoolNum(self):  # print_schoolNum 메서드 생성
        num = self.schoolNum[5:6]  # 학부 분류를 위해 슬라이싱해서 num에 저장
        department = {  # 학부 구분하기 위한 딕셔너리 생성
            "1": "인문융합자율학부",
            "2": "사회융합자율학부",
            "3": "미디어융합자율학부",
            "4": "it융합자율학부",
        }
        if num in department.keys():  # 슬라이싱한 학번을 이용한 딕셔너리의 키값 검사
            print(
                f"학번은 {self.schoolNum}로 {department[num]} 소속입니다."  # 학부 구분에 따른 학번을 포함한 문자열 반환
            )
        else:
            return {f"오류입니다"}  # 오류 출력

    def print_semester(self):  # print_semester 메서드 생성
        if self.semester <= 3:
            print(f"{self.name}은(는){self.semester}학기차로 전공선택 전입니다.")  # 전공 선택 전
        elif self.semester <= 8:
            print(f"{self.name}은(는) {self.semester}학기차로 전공선택을 마쳤습니다.")  # 전공 선택 후
        else:
            print("오류입니다.")  # 오류 출력

    def print_subject(self):  # print_subject 메서드 생성
        print(f"{self.subject}를 수강합니다.")  # 수강과목 반환


def subject_info(subject_dict):  ## 딕셔너리를 매개변수로 받는 subject_info 메서드 생성
    print("자세한 수강목록입니다.")
    for key, value in subject_dict.items():  # 반복문을 통해 딕셔너리 탐색
        print(f"과목명: {key} / 과목명의 길이: {value}")  # 과목 딕셔너리의 key값과 value값 출력


while True:  # while 반복문
    class_name = input("객체명을 입력하시오. (단, 영문으로): ")  # class_name 변수 정의
    if class_name == "종료":  # 종료를 입력할시 종료
        break
    name = input("이름을 입력하시오. (단, 한글로): ")  # name 변수 정의
    schoolNum = input("학번을 입력하시오: ")  # schoolNum 변수 정의
    while len(schoolNum) != 9:  # 학번이 9자리가 아닐 경우
        print("학번은 9자리이어야 합니다.")
        schoolNum = input("학번을 입력하시오: ")
    semester = int(input("학기를 입력하시오. (단, 숫자로): "))  # semester 변수에 정수형 자료형 정의
    subjcet_list = []  # 과목들을 담을 빈 리스트 정의
    subject_dict = {}  # 과목들을 담을 빈 딕셔너리 정의
    for i in range(3):  # 3번의 반복문 회차 돌기
        subject = input("과목을 입력하시오: ")  # 과목 입력받기
        subjcet_list.append(subject)  # 과목리스트에 과목추가
        subject_dict[subject] = len(subject)  # 과목 딕셔너리의 value에 문자열의 길이 저장

    class_name = Student(name, schoolNum, semester, subjcet_list)  # 객체 생성 및 초기화
    print()  # 한 줄 띄어주기

    class_name.print_name()  # 객체의 이름을 출력하는 메서드
    class_name.print_schoolNum()  # 객체의 학번을 출력하는 메서드
    class_name.print_semester()  # 객체의 학기정보를 출력하는 메서드
    class_name.print_subject()  # 객체의 과목을 출력하는 메서드
    print()  # 한 줄 띄어주기

    subject_info(subject_dict)  # 수강중인 과목들의 정보를 출력하는 함수
    print()  # 한 줄 띄어주기
    break  # 출력 완료시 반복문 종료
