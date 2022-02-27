class Solution:
	def isPalindrome(self, s: str) -> bool:
		list1 = ["" + char for char in s if char.isalnum()]
		str1 = ""
		for i in list1:
			str1 += i

		if str1.lower() == str1[::-1].lower():
			return True
		else:
			return False