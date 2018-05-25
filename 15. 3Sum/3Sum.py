from bisect import bisect_left, bisect_right

class Solution:
	case_length = []
	case_index = 0
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		m = {}
		result = []
		for n in nums:
			if n in m:
				m[n] += 1
			else:
				m[n] = 1
		
		if 0 in m and m[0] >=3:
			result.append([0, 0, 0])
			
		keys = list(m.keys())
		keys.sort()
		print(keys)
		keys_num = len(keys)
		
		if keys_num == 0:
			return []
					
		# a<b<c。a一定小于0，c一定大于0
		end = bisect_left(keys, 0) # a < 0
		begin = bisect_left(keys, -keys[-1]*2) # when b == c, a + b + c = a + 2c <= a + 2*max_c;
#		print('a in [{}:{}]'.format(begin, end))
		for i in range(begin, end):
			a = keys[i]
			
			#b == c
			if a != 0 and m[a] >= 2 and -2*a in m:
				result.append([a, a, -2*a])
			
			# b的取值范围
			# -a - b = c <= keys[-1] >>>> b >= -keys[-1] - a
			min_b = -keys[-1] - a
			# b<c >>>> a + 2b < a + b + c = 0 >>>> b < -a/2
			max_b = -a/2
			
			b_begin = max(i + 1, bisect_left(keys, min_b)) # b的最小值
			b_end = bisect_right(keys, max_b) # b的最大值
#			print('a = {}, {} <= b < {}, in [{}:{}]'.format(a, min_b, max_b, b_begin, b_end))
			for j in range(b_begin, b_end):
				b = keys[j]
#				print('key[{}] = {}, key[{}] = {}'.format(i, a, j, b))
				c = -a-b
				if c in m:
					if b > c:
						continue
					if b < c or m[b] >=2:
#						print('========', [a, b, c])
						result.append([a, b, c])
		return result
		
		





s = Solution()
#data_list = [[-1,0,1,2,-1,-4], [-1, 0, 1], [-1,0,1,2,-1,-4], [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]]
#data_list = [[-8,8,5,-2,-8,-9,-10,6,-3,-5,5,-6,-2,-6,5,-5,7,3,-4,0,-5,-2]]
data_list = [[-7,-5,5,-6,-2,1,7,3,-4,-2,-2,-4,-8,-1,8,8,-2,-7,3,2,-7,8,-3,-10,5,2,8,7,7]]
for data in data_list:
	print('>>>>>>>>>>>>>>>>>>>>>>>',data)
	result = s.threeSum(data)
	print(result)