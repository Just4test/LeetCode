//https://leetcode.com/problems/regular-expression-matching/
package main

import "fmt"

func main() {
	test("aa","a")
	test("aa","aa")
	test("aaa","aa")
	test("aa", "a*")
	test("aa", ".*")
	test("ab", ".*")
	test("aab", "c*a*b")
}

func test(s string, p string){
	fmt.Printf("isMatch(\"%s\",\"%s\") = %t\n", s, p, isMatch(s, p))
}


////////////以下代码粘贴到答案中/////////////////

//定义匹配器
const (
	char = iota	//目标是单个指定字符  'a'
	any				//目标是任意字符 '.'
	many			//目标是任意多个指定字符 'a*'
	manychar			//目标是任意多个相同的任意字符 '.*'
)
type M struct{
	v int32
	Type int8
}

func createM(c int32, lastM *M) *M{
	switch c {
		case '*':
			switch lastM.Type {
				case char:
					lastM.Type = many
					return nil
				case any:
					lastM.Type = manychar
					return nil
			}
		case '.':
			return &M{0, any}
		default:
			return &M{c, char}
	}
	return nil
}

func matchOne(chars []byte, mlist []*M) bool {
	length := len(chars)
	if len(mlist) == 0{
		return length == 0
	}
	if length == 0 {
		for _, m := range(mlist){
			if m.Type != many && m.Type != manychar {
				return false
			}
		}
		return true
	}
	
	
	m := mlist[0]
	
	switch m.Type {
		case char:
			if chars[0] == byte(m.v) && length >= 1 {
				return matchOne(chars[1:], mlist[1:])
			}
			return false
		case any:
			if length < int(m.v) {
				return false
			}
			return matchOne(chars[1:], mlist[1:])
		case many:
			if matchOne(chars, mlist[1:]) {
				return true
			}
			target := byte(m.v)
			for i, c := range chars {
				if target != c {
					break
				}
				if matchOne(chars[i + 1:], mlist[1:]) {
					return true
				}
			}
			return false
		default: //manychar
			if matchOne(chars, mlist[1:]) {
				return true
			}
			for i := 0; i <= length; i++ {
				if matchOne(chars[i:], mlist[1:]) {
					return true
				}
			}
			return false
	}
}

func isMatch(s string, p string) bool {
	mlist := make([]*M,0)
	var lastM *M = &M{0, char}
	
	chars := []byte(s)
	copy(chars[:], s)	
	
	for _, c := range p{
//		fmt.Printf("%v => ", *lastM)
		temp := createM(c, lastM)
//		fmt.Printf("%v \n", *lastM)
		if temp != nil {
			lastM = temp
			mlist = append(mlist, temp)
		}
	}
		
//	fmt.Printf("%&", mlist)
	
	return matchOne(chars, mlist)
}























