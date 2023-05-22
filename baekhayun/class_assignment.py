#클래스명 Student로 생성하기
class Student:
    def __init__(self, name, schoolNum, semester, subject):
        self.name = name
        self.schoolNum = schoolNum
        self.semester = semester
        self.subject = subject

    def print_name(self):
        print(f'이름은 {self.name}입니다.')

    def print_schoolNum(self):
        print(f'학번은 {self.schoolNum}으로 {result}')
    
    def print_semester(self):
        print(f'{self.name}은(는) {self.semester}학기차로 {result2}')

    def print_subject(self):
        print(f'[{self.subject}]를 수강합니다.')


# While 반복문 사용하기
while True: 
    Class_name = input("객체 명을 입력하시오. (단, 영문으로):")
    # Class_name에 '종료'입력하면 반복문 빠져나오기
    if Class_name == '종료':
        break

    name = input("이름을 입력하시오. (단 한글로):")

    schoolNum = input("학번을 입력하시오.:")
    #입력받은 학번 중 6번째 숫자로 소속학부 판별하기
    a = int(schoolNum[5])
    if a == 1:
        result = '인문융합자율학부 소속입니다.'
    elif a == 2:
        result = '사회융합자율학부 소속입니다.'
    elif a == 3:
        result = '미디어융합자율학부 소속입니다.'
    elif a == 4:
        result = 'it융합자율학부 소속입니다.'
    else:
        result = '오류입니다.'

    semester = int(input("학기를 입력하시오. (단, 숫자로):"))
    if semester < 4 :
        result2 = '전공선택 전입니다.'
    else:
        result2 = '전공선택을 마쳤습니다.'

    subject = input("과목을 입력하시오.: ")

Class_name.print_name()
Class_name.print_schoolNum()
Class_name.print_semester()
Class_name.print_subject()
        
print()

print('자세한 수강목록입니다.')

def subject_info(subjects):
    for key, value in subjects.items():
        print(f"과목명: {key}/ 과목명의 길이: {value}")

        # 빈 딕셔너리 생성
subjects = {}

        # 사용자로부터 과목명 입력 받아 Dict에 저장하여 출력하기
for i in range(3):
    subject = input("과목을 입력하시오.: ")
    length = len(subject)
    subjects[subject] = length