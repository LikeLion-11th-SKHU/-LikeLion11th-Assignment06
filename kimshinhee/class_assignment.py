class Student: #Student 클래스 생성
    def __init__(self, name, schoolNum, semester, subject): #생성자(객체 생성시마다 매개변수 초기화)
        self.name = name
        self.schoolNum = schoolNum
        self.semester = semester
        self.subject = subject

    def print_name(self): #이름을 출력하는 메서드
        print(f"이름은 {self.name}입니다.")
    
    def print_schoolNum(self): #학번과 학부를 출력하는 메서드
        major = "" #빈 문자열로 변수 초기화
        majorNum = int(self.schoolNum[5:6]) #schoolNum[5:6]의 숫자로 학부 구별하기
        if majorNum in [1,2,3,4]:
            if majorNum == 1: 
                    major = "인문"
            elif majorNum == 2:
                    major = "사회"
            elif majorNum == 3:
                    major = "미디어"
            else:
                    major = "IT"
            print(f"학번은 {self.schoolNum}로 {major}융합자율학부 소속입니다.")
        else:
            print("오류입니다.")
        
        
    def print_semester(self): #몇 학기차인 지 확인 후 전공선택 전인지 후인지 판단하는 메서드
        select="" #빈 문자열로 변수 초기화
        if self.semester in [1,2,3]: #1,2,3학기 차면
            select="전공선택 전"
        elif self.semester in [4, 5, 6, 7, 8]: #4~8학기 차면
            select="전공선택 후"
        else:                   #이외의 숫자를 적었을 경우
            select="오류"
        print(f"{self.name}은(는) {self.semester}학기차로 {select}입니다.")

    def print_subject(self): #수강과목 출력하는 메서드
        print(f'{sub_list}를 수강합니다.')
    
def subject_info(**sub_dict): #딕셔너리 언패킹을 사용한 함수
    print("자세한 수강목록입니다.")
    for subject, sub_len in sub_dict.items(): #딕셔너리의 요소를 반복하여 key, value출력
        print(f'과목명: {subject}/ 과목명의 길이: {sub_len}')

while True: #무한반복
    class_name = input("객체 명을 입력하시오. (단, 영문으로): ") #객체 명 입력받기
    if class_name == "종료": #무한루프를 멈출 조건: "종료"입력
        break
    #객체 속성에 저장할 데이터 입력받기
    name = input("이름을 입력하시오. (단, 한글로): ")
    schoolNum = input("학번을 입력하시오: ")
    semester = int(input("학기를 입력하시오. (단, 숫자로): ")) #숫자로만 입력받을 것이기에 int()로 받기
    sub_list = [] #과목명 담을 리스트
    sub_dict = {} #과목명 담을 딕셔너리
    for _ in range(3): #3번을 반복하는 반복문으로 3개의 과목 입력받기
        subject = input("과목을 입력하시오. : ")
        sub_list.append(subject) #입력받은 과목 sub_list에 추가
        sub_len = len(subject) #과목명의 단어수 sub_len변수에 저장
        sub_dict[subject] = len(subject) #딕셔너리 구성

    #인스턴스 생성해주기
    class_name = Student(name, schoolNum, semester, subject)

    print()

    #매서드 모두 출력
    class_name.print_name()
    class_name.print_schoolNum()
    class_name.print_semester()
    class_name.print_subject()
    print()

    #함수 출력
    subject_info(**sub_dict)
    print()

    