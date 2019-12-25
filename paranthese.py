class checkbrackets:
	def proper_paranthese(self, str1):
	  stack = [] 
	  pchar =  {"(": ")", "{": "}", "[": "]"}
      for parenthese in str1 :
        if parenthese in pchar:
            stack.append(parenthese)
        elif len(stack) == 0 :
            return False
        return len(stack) == 0
print(checkbrackets().proper_paranthese("(){}[]"))
print(checkbrackets().proper_paranthese("()[{)}"))