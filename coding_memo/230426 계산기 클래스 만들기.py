# 계산기 만들기
# 기능 : 두 정수의 사칙연산 (+,-,*,/)
# add(), sub(), mul(), div() 함수 정의
# input() 함수를 활용하여 정수 2개, 사칙연산 선택을 입력받은 후 계산 결과를 print한다.
# 계산식과 결과를 calculator_result.txt.파일에 기록한다.
# 사용 자가 'q' 를 입력하면 종료한다.

class ResultNumber:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print("계산기 생성")
    def add(self):
        print(f"계산 완료 : {self.num1} + {self.num2} = {self.num1 + self.num2}")
    def sub(self):
        print(f"계산 완료 : {self.num1} - {self.num2} = {self.num1 - self.num2}")
    def mul(self):
        print(f"계산 완료 : {self.num1} * {self.num2} = {self.num1 * self.num2}")
    def div(self):
        print(f"계산 완료 : {self.num1} / {self.num2} = {self.num1 / self.num2}")

        
is_back_numbers = ''
while True:
    print(f"""계산기 생성 ----
    1. +
    2. -
    3. *
    4. /{is_back_numbers}
    q. exit""")
    operator = input()
    if operator == 'q':
        break

    if int(operator) < 5:
        num1 = int(input("계산할 첫 번째 수를 입력 : "))
        num2 = int(input("계산할 두 번째 수를 입력 : "))
        result_number = ResultNumber(num1, num2)
        is_back_numbers = f'\n  5. 이전 값 사용 {num1}, {num2}'
    else:
        print("""
        1. +
        2. -
        3. *
        4. /""")
        operator = input("계산할 방법을 선택하세요 : ")
    
    if operator == '1':
        result_number.add()
    elif operator == '2':
        result_number.sub()
    elif operator == '3':
        result_number.mul()
    elif operator == '4':
        result_number.div()