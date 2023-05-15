class Student:
    # 생성자 선언
    def __init__(self, name, schoolNum, semester, subject):
        self.name = name  # 이름 초기화
        self.schoolNum = schoolNum  # 학번 초기화
        self.semester = semester  # 학기 초기화
        self.subject = subject  # 과목 초기화

    def print_name(self):  # 이름 출력
        print(f'이름은 {self.name}입니다.')

    def print_schoolNum(self):  # 학번 및 소속 학부 출력
        major_num = int(self.schoolNum[5:6])  # 학번에서 소속학부를 구분해 주는 6번째 숫자 저장
        if 0 < major_num < 5:  # 해당 번호가 1~4 사이의 번호인지 검사
            if major_num == 1:  # 1이면 인융
                major = '인문'
            elif major_num == 2:  # 2이면 미컨
                major = '미디어컨텐츠'
            elif major_num == 3:  # 3이면 사융
                major = '사회'
            else:  # 4이면 아이티
                major = '아이티'
            print(f'학번은 {self.schoolNum}로 {major}융합자율학부 소속입니다.')
        else:  # 해당하는 범위의 숫자가 아니면 오류메세지 출력
            print('오류입니다.')

    def print_semester(self):  # 학기 출력
        if 0 < self.semester < 4:  # 해당 학기가 1~3학기면 전공 선택 전
            message = '전공선택 전입니다.'
        elif self.semester >= 4:  # 해당 학기가 4학기 이상이면 전공 선택 후
            message = '전공선택을 마쳤습니다.'
        print(f'{self.name}은(는) {self.semester}학기차로 {message}')

    def print_subject(self):  # 수강 중인 과목 리스트 출력
        print(f'{self.subject}를 수강합니다.')


def subject_info(**subject_dict):  # 과목 리스트 자세히 출력. 딕셔너리를 매개변수로 받음
    print('자세한 수강목록입니다.')
    for subject, word_len in subject_dict.items():  # 딕셔너리의 요소를 반복하며 키(과목명), value(과목명의 길이) 출력
        print(f'과목명: {subject} / 과목명의 길이: {word_len}')


def main():  # main 함수
    while True:
        class_name = input('객체명을 입력하시오. (단, 영문으로): ')  # 객체명 입력
        if class_name == '종료':  # 객체명 종료일 경우
            break  # 반복문 탈출
        name = input('이름을 입력하시오. (단, 한글로): ')  # 이름 입력
        schoolNum = input('학번을 입력하시오: ')  # 학번 입력
        while len(schoolNum) != 9:  # 학번 9자리 아닐 경우
            print('9자리로 입력해야 합니다.')  # 오류 메세지 출력
            schoolNum = input('학번을 입력하시오: ')  # 학번 재입력
        semester = int(input('학기를 입력하시오. (단, 숫자로): '))  # 학기 입력
        subject_list = []  # 과목 저장 리스트
        subject_dict = {}  # 과목 저장 딕셔너리
        for _ in range(3):  # 3번 과목 입력받기
            subject = input('과목을 입력하시오: ')  # 과목명 입력
            subject_list.append(subject)  # 리스트에 추가
            subject_dict[subject] = len(subject)  # 딕셔너리에 추가
        class_name = Student(name, schoolNum, semester, subject_list)  # 입력 받은 변수로 해당 객체 생성 및 초기화
        print()
        # 객체 정보 출력
        class_name.print_name()
        class_name.print_schoolNum()
        class_name.print_semester()
        class_name.print_subject()
        print()
        # 과목 정보 출력
        subject_info(**subject_dict)
        print()
    # main 함수 종료
    return None


# main 함수 실행
main()
