class Student :
        #객체에 초기값 설정을 위해 생성자 구현
    def __init__(self,name,schoolNum,semester,subject) :
        self.name = name #이름
        self.schoolNum = schoolNum #학번
        self.semester = semester #학기
        self.subject = subject #과목
   
   #이름을 스스로 입력 받으면 출력되도록 함.
    def print_name(self) :
        print(f'이름은 {self.name}입니다.') 
    
    #학번을 입력 받으면 반환 되도록 함.
    #슬라이싱한 결과를 통해 반환 값을 달리 정해 입력받은 숫자를 정수형이나 실수형이 아닌 문자열로 인식하게 하여 숫자별로 학과를 정함.
    def print_schoolNum(self) :
        if ('1' == self.schoolNum[5:6]) :
            return(f'학번은 {self.schoolNum}로 인문융합자율학부 소속입니다.')
        elif ('2' == self.schoolNum[5:6]) :
            return(f'학번은 {self.schoolNum}로 사회융합자율학부 소속입니다.')
        elif ('3' == self.schoolNum[5:6]) :
            return(f'학번은 {self.schoolNum}로 미디어융합자율학부 소속입니다.')
        elif ('4' == self.schoolNum[5:6]) :
            return(f'학번은 {self.schoolNum}로 it융합자율학부 소속입니다.')
        else :
            return("그 외의 숫자 오류입니다.")
    
    #학기를 입력 받으면 이름과 학기 그리고 전공선택 유무를 출력.
    #if문을 사용해 전공선택 유무를 정함.
    def print_semester(self) :
        if 0< self.semester <= 3 :
            print(f'{self.name}은(는) {self.semester}학기차로 전공 선택 전입니다.')
        elif 4 <= self.semester <= 8  :
            print(f'{self.name}은(는) {self.semester}학기차로 전공 선택을 마쳤습니다.')
        else :
            print("그 외의 숫자 오류입니다.")
    
    #과목을 입력받으면  입력 받은 과목 전체가 보이도록 반환
    def print_subject(self) :
        return(f'{self.subject}를 수강합니다.')
    
#딕셔너리 언패킹을 사용해 딕셔너리의 Key,value를 출력하는 함수 사용.        
def subject_info(**subject_dic) :
    print("자세한 수강목록입니다.")

     #items() 함수를 사용해 딕셔너리에 있는 key와 value를 얻음.      
    for key,value in subject_dic.items() :
        print(f'과목명:{key}/과목명의 길이:{value}')


while True: #종료와 같지 않으면 계속 반복하도록 반복문 사용
        Class_name =input("객체 명을 입력하시오. (단, 영문으로) :") #변수를 사용해 객체명 입력 받도록 함.
        #종료를 입력받으면 끝나도록 if문, break 사용
        if Class_name == '종료' :
            break
        name = input("이름을 입력하시오. (단, 한글로):") # 변수를 사용해 이름을 입력 받음.
        schoolNum = input("학번을 입력하시오:") #변수를 사용해 학번을 입력받음
        semester = int(input("학기을 입력하시오.(단, 숫자로):")) #변수를 사용해 학기를 입력 받음
    
        subject_list=[] #과목을 저장할 리스트를 하나 생성해 줌
        subject_dic = {} #빈 딕셔너리 선언. 입력받은 과목들을 위해 사용
        for i in range (4) : #반복문을 사용해 최소 3개 이상의 과목(4개)을 입력받음
            
            subject = subject_list.append( input("과목을 입력하시오.:"))   #과목명을 입력받음
            for sub in subject_list: 
                subject_dic[sub] =len(sub)                                         
            
            
        instance = Student(name,schoolNum,semester,subject_list) #인스턴스 생성
        print() #한 줄 공백(가독성을 위함)

        instance.print_name()
        print(instance.print_schoolNum())
        instance.print_semester()
        print(instance.print_subject())
        print() #한 줄 공백(가독성을 위함)


        subject_info(**subject_dic)
        print() #한 줄 공백(가독성을 위함)



