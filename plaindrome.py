

def isPalindrome(s):
	return s == s[::-1]



s = str(input('ENTER THE WORD : '))
ans = isPalindrome(s)

if ans:
	print("true")
else:
	print("false")