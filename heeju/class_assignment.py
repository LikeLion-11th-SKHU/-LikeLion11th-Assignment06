class Student:
    # 생성자로 변수들을 초기화함
    def __init__(self, name, schoolNum, semester, subject):
        self.name=name
        self.schoolNum=schoolNum
        self.semester=semester
        self.subject=subject
    
    # 사용자의 이름을 출력하는 메서드
    def print_name(self):
        print(f'이름은 {self.name}입니다.')
    
    # 학부 소속을 출력하는 메서드
    def print_schoolNum(self):
        departmentNum=int(self.schoolNum[5:6])
        if departmentNum==1:
            print(f'학번은 {self.schoolNum}로 인문융합자율학부 소속입니다.')
        elif departmentNum==2:
            print(f'학번은 {self.schoolNum}로 사회융합자율학부 소속입니다. ')
        elif departmentNum==3:
            print(f'학번은 {self.schoolNum}로 미디어융합자율학부 소속입니다. ')
        elif departmentNum==4:
            print(f'학번은 {self.schoolNum}로 IT융합자율학부 소속입니다. ')
        else:
            print('오류입니다.')
    
    # 진입학기에 따른 전공선택 여부를 출력하는 메서드
    def print_semester(self):
        if self.semester<4:
            print(f'{self.name}은(는) {self.semester}학기차로 아직 전공선택 전입니다.')
        elif self.semester>=4 and self.semester<=8:
            print(f'{self.name}은(는) {self.semester}학기차로 전공선택을 마쳤습니다.')

    # 수강하는 과목의 리스트를 출력하는 메서드
    def print_subject(self):
            print(f'{self.subject}를 수강합니다.')
    
# 자세한 수강과목들의 과목명과 과목명의 길이를 출력하는 메서드    
def subject_info(**subjectDic):
    print('자세한 수강목록입니다.')
    for subItem,subItemLen in subjectDic.items():
        print(f'과목명: {subItem} / 과목명의 길이: {subItemLen}')

subject=[]      #과목명을 저장할 리스트
subjectDic={}   #과목명과 길이를 저장할 딕셔너리

#메인을 실행할 메인함수
def main():
    # 무한루프를 통해 여러번 입력받을 수 있도록 함.
    while(True):
        print('객체 명을 입력하시오. (단, 영문으로): ',end='')
        ClassInput=input()
        #만약 사용자가 종료라고 입력했으면,전체적인 반복문을 종료하도록 함.
        if ClassInput=='종료':
            break
        # 사용자가 종료를 안 눌렀으면 객체명으로 입력한 값을 저장함.
        Class_name=ClassInput

        print('이름을 입력하시오. (단, 한글로): ',end='')
        name=input()
        
        # 작은 while루프를 통해서 학번을 제대로 9자리 입력될때까지 반복시킴.
        while(True):
            print('학번을 입력하시오: ',end='')
            schoolNum=input()
            if len(schoolNum)==9:
                break
            else:
                print('오류입니다.')
                pass
                
        # 학기를 입력받음
        print('학기를 입력하시오. (단, 숫자로): ',end='')
        semester=int(input())
        
        # while무한루프를 통해 여러 과목을 입력받을 수 있도록 함.
        while(True):
            print('과목을 입력하시오. : ',end='')
            sub=input()
            #만일 사용자가 종료라고 누르면 더 이상 과목을 입력받지 않고, 무한루프를 빠져나옴.
            if sub=='종료':
                break

            #과목명을 리스트와, 딕셔너리에 각각 추가함.
            subject.append(sub)
            subjectDic[sub]=len(sub)
    
    # 객체를 선언함.
    Class_name=Student(name,schoolNum,semester,subject)
    print()

    # 이름, 학번, 소속, 전공선택, 과목명을 차례대로 메소드 호출하여 출력함.
    Class_name.print_name()
    Class_name.print_schoolNum()
    Class_name.print_semester()
    Class_name.print_subject()
    print()

    # 과목명 상세목록을 출력하는 메소드를 호출함.
    subject_info(**subjectDic)




main()


    