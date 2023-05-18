
    # 객체명 입력란 추가하기
Class_name=''
while Class_name != '종료' : #종료와 같지 않으면 계속 반복하도록 반복문 사용
        Class_name =input("객체 명을 입력하시오. (단, 영문으로) :") #변수를 사용해 객체명 입력 받도록 함.
        name = input("이름을 입력하시오. (단, 한글로):") # 변수를 사용해 이름을 입력 받음.
        schoolNum = input("학번을 입력하시오:") #변수를 사용해 학번을 입력받음
        semester = int(input("학기를 입력하시오:")) #변수를 사용해 학기를 입력 받음
    
        
        for i in range (4) : #반복문을 사용해 최소 3개 이상의 과목(4개)을 입력받음
            subject=[] #과목을 저장할 리스트를 하나 생성해 줌
            s= subject.append( input("과목을 입력하시오.:")) 
        print(s)


    #객체에 초기값 설정을 위해 생성자 구현
class Student :
        def __init__(self,name,schoolNum,semester,subject) :
            self.name = name
            self.schoolNum = schoolNum
            self.semester = semester
            self.subject = subject
   
        def print_name(self) :
            print(f'이름은{self.name}입니다.')
    
        def print_schoolNum(self) :
            if 1 == self.schoolNum[5:6] :
                return(f'학번은 {self.schoolNum}로 인문융합자율학부 소속입니다.')
            elif 2 == self.schoolNum[5:6] :
                return(f'학번은 {self.schoolNum}로 사회융합자율학부 소속입니다.')
            elif 3 == self.schoolNum[5:6] :
                return(f'학번은 {self.schoolNum}로 미디어융합자율학부 소속입니다.')
            elif 4 == self.schoolNum[5:6] :
                return(f'학번은 {self.schoolNum}로 it융합자율학부 소속입니다.')
            else :
                return("그 외의 숫자 오류입니다.")

        def print_semester(self) :
            if self.semester <= 3 :
                print(f'{self.name}은(는) {self.semester}학기차로 전공 선택 전입니다.')
            elif self.semester >=4 :
                print(f'{self.name}은(는) {self.semester}학기차로 전공 선택을 마쳤습니다.')
            else :
                print("그 외의 숫자 오류입니다.")
    
        def print_subject(self) :
            return(f'[{self.subject}]를 수강합니다.')

        def subject_info() :
            print("자세한 수강목록입니다.")
            subject_dic={}:#빈 딕셔너리 선언. 입력받은 과목들을 위해 사용
            for key,value in subject_dic.items()
            print(f'과목명:{key}/과목명의 길이:{len(value)}')
           
   
Student.print_name()
Student.print_schoolNum()
Student.print_semester()
Student.print_subject()
Student.subject_info()