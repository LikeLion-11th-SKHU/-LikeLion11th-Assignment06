class Student:
   
    def __init__(self, name, schoolNum, semester, subject): 
        #init : 객체 생성 자동 호출, 객체 속성 초기화
        #self : 매개변수, 객체의 속성에 접근  
        self.name = name
        self.schoolNum = schoolNum
        self.semester = semester
        self.subject = subject
        # 변수 객체 상태, 정보 저장 
        self.subject_dic = {} # 빈 딕셔너리 생성하여 과목 정보 저장

    def print_name(self):
        print(f'이름은 {self.name}입니다.')

    def print_schoolNum(self):
        if self.schoolNum[5:6] == '1':
            print(f'학번은 {self.schoolNum}로 인문융합자율학부 소속입니다.')
        elif self.schoolNum[5:6] == '2':
            print(f'학번은 {self.schoolNum}로 사회융합자율학부 소속입니다.')
        elif self.schoolNum[5:6] == '3':
            print(f'학번은 {self.schoolNum}로 미디어융합자율학부 소속입니다.')
        elif self.schoolNum[5:6] == '4':
            print(f'학번은 {self.schoolNum}로 아이티융합자율학부 소속입니다.')
        else: 
            print('오류입니다')

    def print_semester(self):
        if 0 < self.semester < 4:
            print(f'{self.name}은(는) {self.semester}학기차로 아직 전공선택 전입니다.')
        elif self.semester >= 4: 
            print(f'{self.name}은(는) {self.semester}학기차로 전공선택을 마쳤습니다.')

    def print_subject(self):
        print(f'{self.subject}를 수강합니다.')

    def subject_info(self):
        print('자세한 수강목록입니다.')
        for subject in self.subject:
            #for문과 in문을 통해 과목 리스트의 요소를 순회하며 반복 작업하기 위해
            subject_len = len(subject)
            self.subject_dic[subject] = subject_len
            #딕셔너리를 통해 키를 사용하여 값을 검색할 수 있도록 
            print(f'과목명: {subject} / 과목명의 길이: {subject_len}')

def main():
    while True:
    #사용자의 입력을 계속해서 받아야하므로 지속적으로 프로그램 실행시키기 위해
        class_name = input('객체 명을 입력하시오. (단, 영문으로) : ')
        if class_name == '종료':
            break

        name = input('이름을 입력하시오. (단, 한글로): ')
        schoolNum = input('학번을 입력하시오. : ')
        while len(schoolNum) != 9:
        # 학번 9자리이기때문에 9자리 학번 입력받을 수 있도록 
            print('9자리로 입력하십시오.')
            schoolNum = input('학번을 입력하시오. : ')
        semester = int(input('학기를 입력하시오. (단, 숫자로): '))
        subject_list = [] #사용자 입력받은 과목 저장
        subject_dic = {} #과목명, 과목길이 저장 
        for i in range(3): #최대 3개 과목 입력받기 위해 
            subject = input('과목을 입력하시오. : ')
            if subject:
                subject_list.append(subject) #리스트에 추가하기 위해
            else:
                break

        class_name = Student(name, schoolNum, semester, subject_list)

        print()

        class_name.print_name()
        class_name.print_schoolNum()
        class_name.print_semester()
        class_name.print_subject()

        print()

        class_name.subject_info() #객체의 메서드 호출하여 수강 과목 정보 자세히 출력

main()