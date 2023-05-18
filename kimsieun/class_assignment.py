# 클래스 메서드 ========
class student: #가이드라인 1번
    def __init__(self, name, schoolNum, semester, subject):  #속성만들기 __init__() 메서드 사용 -> 생성자 구현
        self.name = name  #name으로 self.name초기화 하기
        self.schoolNum = schoolNum #schoolNum으로 self.schoolNum초기화 하기
        self.semester = semester #semester으로 self.semester초기화 하기
        self.subject = subject #subject으로 self.subject초기화 하기
        
        
    def print_name(self): #가이드라인 2번
        print(f'이름은 {self.name} 입니다.') #포맷팅 사용 / 이름 포함 출력


    def print_schoolNum(self): #가이드라인 3번
        num = int(self.schoolNum[5:6]) #문자열 슬라이싱을 이용해서 학부 구별
        if (num == 1): #1이면 인문
            major = '인문융합자율학부'
            print(f'학번은 {self.schoolNum}로 {major} 소속입니다.') #포맷팅 사용 / 학번 포함 출력
        elif (num == 2): #2면 사융
            major = '사회융합자율학부'
            print(f'학번은 {self.schoolNum}로 {major} 소속입니다.') #포맷팅 사용 / 학번 포함 출력
        elif (num == 3): #3이면 미융
            major = '미디어융합자율학부'
            print(f'학번은 {self.schoolNum}로 {major} 소속입니다.') #포맷팅 사용 / 학번 포함 출력
        elif (num == 4): #4면 아이티
            major = 'IT융합자율학부'
            print(f'학번은 {self.schoolNum}로 {major} 소속입니다.') #포맷팅 사용 / 학번 포함 출력
        else:
            print('오류입니다.') #다른 번호는 오류 처리
    
    
    def print_semester(self): #가이드라인 4번
        if (0 < self.semester < 4): #3학기까지는 전공선택 전
            print(f'{self.name}은(는) {self.semester}학기차로 전공선택 전입니다.') #포맷팅 사용 / 학기 포함 출력
        elif (5 < self.semester): #4학기부터는 전공선택 후
            print(f'{self.name}은(는) {self.semester}학기차로 전공선택을 마쳤습니다.') #포맷팅 사용 / 학기 포함 출력
        elif (self.semester == 0):
            return('오류입니다.') #0학기는 없으므로 오류 반환


    def print_subject(self): #가이드라인 5번
        print(f'{self.subject}를 수강합니다.') #포맷팅 사용 / 과목 리스트 포함
    


# 함수 ========
def subject_info(**sub_dict): #과목을 여러개 받아 출력하는 함수
    print('자세한 수강목록입니다.') #첫 줄에 출력
    for key, value in sub_dict.items(): #딕셔너리에서 key, vlaue 사용한 반복문
        print(f'과목명: {key} / 과목명의 길이: {value}') #포맷팅 사용, 딕셔너리 key, value 출력
        


# 터미널 ========
while (True): #반복문 사용
    Class_name = str(input('객체 명을 입력하시오. (단, 영문으로): ')) #Class_name 정의 / 객체 명 문자로 입력 받기
    if (Class_name == '종료'): #종료 입력시 종료
        break
    
    name = input('이름을 입력하시오. (단, 한글로): ') #name = 이름 문자로 입력 받기
    
    schoolNum = str(input('학번을 입력하시오.: ')) #schoolNum = 학번 정수로 입력 받기
    if (len(schoolNum) != 9): #9자리가 아니면
        print('9자리로 입력해주세요.') #오류문자 출력
    
    semester = int(input('학기를 입력하시오. (단, 숫자로): ')) #semester = 학기 정수로 입력 받기
    
    sub_list = [] #가이드라인 4번 
    sub_dict = {} #빈 리스트와 딕셔너리 정의
    
    for a in range(3): #과목 입력 받기 3번 반복하는 반복문
        subject = input('과목을 입력하시오. :') #subject = 과목 입력 받기
        sub_list.append(subject) #리스트에 과목 추가
        sub_dict[subject] = len(subject) #딕셔너리에 문자열 길이 정의
        
    print() #터미널 출력 가이드 (가독성)
    
    Cn = student(name, schoolNum, semester, sub_list) #객체 생성 / 초기화

    Cn.print_name() #객체 이름 출력
    Cn.print_schoolNum() #학번 출력
    Cn.print_semester() #학기 출력
    Cn.print_subject() #과목 출력
    
    print() #터미널 출력 가이드 (가독성)
    
    subject_info(**sub_dict) #함수 출력(자세한 수강목록 함수)
    
    print() #터미널 출력 가이드 (while문 끝)
