# @param {Integer} num
# @return {Integer}
def add_digits(num)
    # O(1)的解法
	return 0 if 0 == num
	return (num % 9) == 0 ? 9 : num % 9
	# 通常解法
    ret = 0
	loop do
		while 0 != num do
			ret += num % 10
			num = (num / 10).to_i
		end
		break if ret < 10
		num = ret
		ret = 0
	end
    return ret
end