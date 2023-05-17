class Student:  # Student라는 이름의 class 생성
    
    def __init__(self, name, schoolNum, semeter, subject):  # __init__을 이용해 생성자를 구현
        self.name = name  # 생성자를 통해 클래스의 인스턴스가 생성될 때 생성자에 전달된 name으로 self.name을 초기화
        self.schoolNum = schoolNum  # 생성자를 통해 클래스의 인스턴스가 생성될 때 생성자에 전달된 schoolNum으로 self.schoolNum을 초기화
        self.semeter = semeter  # 생성자를 통해 클래스의 인스턴스가 생성될 때 생성자에 전달된 semeter으로 self.semeter을 초기화
        self.subject = subject  # 생성자를 통해 클래스의 인스턴스가 생성될 때 생성자에 전달된 subject으로 self.subject을 초기화
    
    def print_name(self):  # print_name라는 이름의 메서드 생성
        print(f"이름은 {self.name}입니다.") # 포매팅을 사용해 이름을 출력
    
    def print_schoolNum(self):  # print_schoolNum이라는 이름의 메서드 생성
        department = self.schoolNum[5:6]  # 전달된 schoolNum의 인덱스 [5,6)범위까지 슬라이싱 해 department라는 변수에 저장
        if(department == '1'):  # department가 1이라면(타입이 str이므로 '1')
            return(f"학번은 {self.schoolNum}로 인문융합자율학부 소속입니다.")  # 포매팅을 사용해 반환
        elif(department == '2'):  # department가 2이라면(타입이 str이므로 '2')
            return(f"학번은 {self.schoolNum}로 사회융합자율학부 소속입니다.")  # 포매팅을 사용해 반환
        elif(department == '3'):  # department가 3이라면(타입이 str이므로 '3')
            return(f"학번은 {self.schoolNum}로 미디어융합자율학부 소속입니다.")  # 포매팅을 사용해 반환
        elif(department == '4'):  # department가 4이라면(타입이 str이므로 '4')
            return(f"학번은 {self.schoolNum}로 아이티융합자율학부 소속입니다.")  # 포매팅을 사용해 반환
        else:  # 위 조건에 맞지 않는다면
            return("오류입니다.")  # 오류라고 반환
        
    def print_semester(self):  # print_semester라는 이름의 메서드 생성
        if(self.semeter <= 3 & self.semeter > 0): # 전달된 semester가 3보다 작거나 같고 0보다 크다면
            print(f"{self.name}은(는){self.semeter}학기차로 전공선택 전입니다.")  # 이름과 학기를 포함한 문자열을 출력
        elif(self.semeter > 3):  #전달된 semester가 3보다 크다면
            print(f"{self.name}은(는) {self.semeter}학기차로 전공선택을 마쳤습니다.")  # 이름과 학기를 포함한 문자열을 출력
        else:  # 위 조건에 맞지 않는다면
            print("오류입니다.")  # 오류라고 반환 
            
    def print_subject(self):  # print_subject라는 이름의 메서드 생성
        return (f"{subject_list}를 수강합니다.")  # subject들이 들어있는 subject_list를 반환
        
    def subject_into(subject_list):  # subject_into라는 함수 생성
        subject_dic = {} # 빈 딕셔너리 생성
        for sub in subject_list: # subject_list의 값들을 하나씩 sub라는 변수에 저장
            subject_dic[sub] = len(sub) # subject_dic라는 빈 딕셔너리에 sub라는 key값과 sub의 길이를 values값으로 저장        
        print("자세한 수강목록입니다.")  # 문자열 출력
        for key, value in subject_dic.items():  # 딕셔너리의 키과 값들을 key와 value에 할당
            print(f"과목명: {key} / 과목명의 길이: {value}")  # key와 value를 포함한 문자열을 출력
       
        


       
while(True):  # while반복문을 이용해 무한루프 생성
    Class_name = str(input("객체 명을 입력하시오. (단, 영문으로) : "))  # 객체 명을 문자열로 입력받아 변수에 저장
    if(Class_name == '종료'):  # 입력받은 객체 명이 종료라면
        break   # 반복문을 빠져나옴

    name = input("이름을 입력하시오. (단, 한글로): ")  # 이름을 입력받아 변수에 저장
    
    schoolNum = str(input("학번을 입력하시오: "))  # 학번을 문자열로 입력받아 변수에 저장
    if(len(schoolNum) != 9):  # 학번의 길이가 9가 아니라면
        print("9자리로 입력해주세요.")  # 9자리로 입력해달라는 문자열 출력
        
    semester = int(input("학기를 입력하시오. (단, 숫자로): "))  # 학기를 정수로 입력받아 변수에 저장
    
    subject_list = []  # 빈 리스트 생성        
    for i in range(3):  # for반복문을 이용해 3번 반복
        subject = input("과목을 입력하시오. : ")  # 과목을 입력 받아 변수에 저장
        subject_list.append(subject)  # 입력받은 변수를 리스트에 추가
            
    print("\n")  # 한 줄 띄우기

   
    s = Student(name, schoolNum, semester, subject)  # 메서드를 출력하기 위해 클래스의 객체 생성
    s.print_name()  # print_name 메소드 호출
    print(s.print_schoolNum())  # print_schoolNum 메소드 출력
    s.print_semester()    # print_semester 메소드 호출
    print(s.print_subject())  # print_subject 메소드 출력
    print("\n")  # 한 줄 띄우기
    Student.subject_into(subject_list)  # subject_into 함수에 subject_list라는 매개변수를 이용해 호출
    print("\n")  # while문의 마지막이므로 한 줄 띄우기
    
    
    