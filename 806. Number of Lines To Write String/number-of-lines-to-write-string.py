class Solution:
	def numberOfLines(self, widths, S):
		"""
		:type widths: List[int]
		:type S: str
		:rtype: List[int]
		"""
		if len(S) == 0:
			return [0, 0]
			
		ORD_A = ord('a')
		linesNum = 1
		width = 0
		
		for c in S:
			w = widths[ord(c) - ORD_A]
			if w + width > 100:
				width = w
				linesNum += 1
			else:
				width += w
		
		return [linesNum, width]