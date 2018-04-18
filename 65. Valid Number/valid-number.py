class Token:
	def __init__(self):
		self.s = ''
		self.t = None
		
	def istype(self, t):
		return self.t == t
		
	def __iadd__(self, c):
		self.s += c
		return self
		
	def __eq__(self, other):
		return self.s == other



class Solution:
	def isNumber(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		
		def tokenization(s):
			result = []
			token = Token()
			currentProcessor = None
			
			
			def tokenFinish():
				nonlocal token, currentProcessor
				result.append(token)
				print('add token', token)
				token = Token()
				currentProcessor = None
			
			'''
			定义一系列处理器。
			词法分析器根据第一个字符获取一个处理器，该处理器处理接下来的字符：
			如果接下来的字符属于当前token，则返回True
			如果接下来的字符属于下一个token，则返回False
			如果接下来的字符不应在此位置出现，抛出异常
			'''
			
			processors = {}
			
#			def spaceProcessor(c):
#				if len(token) > 0:
#					return False
#				if c != ' ':
#					return False
#				
#					
#			processors[' '] = spaceProcessor
			
			def numberProcessor(c):
				if token == '':
					token.t = 'number'
					token.hasDot = False
					token.hasNum = False
					token.hasE = False
					
				if c in '+-':
					if token == '' or token.s[-1] == 'e' or token.s[-1] == 'E':
						return True
					else:
						if token.hasNum and token[s][-1] != '.':
							return False
						else:
							raise Exception('Current number "{}" are not intact, should not appear "{}".'.format(token.s, c))
				
				if c in 'eE':
					if token.hasE:
						raise Exception('Current number "{}" already has a e, should not appera another e.'.format(token.s))
					if not token.hasNum:
						raise Exception('Current number "{}" must end in number, should not appera e.'.format(token.s))
					token.hasE = True
					return True
						 
				
				if c == '.':
					if token.hasE:
						raise Exception('Current number "{}" already has a e, should not appera dot.'.format(token.s))
					if token.hasDot:
						raise Exception('Current number "{}" already has a dot, should not appera another dot.'.format(token.s))
					token.hasDot = True
					return True
						
				if c in '1234567890':
					token.hasNum = True
					return True

				#下个token了
				if not token.hasNum:
					raise Exception('Current number "{}" must has number char, should not appera e.'.format(token.s))	
				if token.s[-1] in 'Ee+-' or token == '.':
					raise Exception('Current number "{}" should not end with {}'.format(token.s, c))	
				return False
				
			for c in '1234567890-+.':
				processors[c] = numberProcessor
			
			def wordProcessor(c):
				if token == '':
					token.t = 'word'
				
				if c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
					return True
				return False
				
			for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
				processors[c] = wordProcessor
				
			def unknownProcessor(c):
				if token == '':
					token.t = 'unknown'
					
				if c == ' ' or c == chr(0):
					return False
				return True
					
				
			def getProcessor(c):
				return processors[c] or unknownProcessor
			
			
			for c in s:
				print('char:', c)
				
				if currentProcessor:
					if currentProcessor(c):
						token += c
						continue
					else:
						tokenFinish()
				
				if c == ' ':
					continue
				currentProcessor = getProcessor(c)
				if currentProcessor(c):
					token += c
					continue
				else:
					raise Exception('When process the first char "{}", the processor {} return False.'.format(c, currentProcessor))
					
			if currentProcessor:
				if currentProcessor(chr(0)):
					raise Exception('When string end, the processor can`t process', chr(0))
				else:
					tokenFinish()
					
			return result
			
		print('==== {} ===='.format(s))
		try:
			tokens = tokenization(s)
		except Exception as e:
			print(e)
			return False
		
		print('==========================')
		print(tokens)
		
		if len(tokens) == 1 and tokens[0].istype('number'):
			return True
			
		return False
				





#print(Solution().isNumber('2e0'))








