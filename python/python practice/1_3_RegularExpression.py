import re

db = '''3412    [Bob] 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534'''

# 숫자만 뽑아내기
print(re.findall(r'[0-9]+', db))

# 이름만 뽑아내기
print(re.findall(r'[A-z]+', db))
print(re.findall(r'[A-Za-z]+', db))

# T로 시작하지 않는 이름 찾기
print(re.findall(r'[^T][a-z]+', db))        # ony
print(re.findall(r'[A-SU-Z][a-z]+', db))
print(re.findall(r'(?<!T)[A-SU-Z][a-z]+', db))


# Tip1) 15번줄 [A-z] and [A-Za-z]는 다르다!!! 아스키코드상,
# 91	[,92	\,93	],94	^,95	_,96	`
# 을 포함하기 때문에, 오류가 발생할 수 있다.

# Tip2) r'(?<![ACTQZ])[B-PR-SU-VWXY][a-z]*'
# 여러 단어를 거르려면 직접 다 적어줘야 한다.
