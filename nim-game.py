#桌面上的石子数是1-3的时候都全部拿走，胜利；
#是4的时候拿多少，对面都成为1-3的局势，失败；
#多于4个时，将石子数对4求余。余数为1-3，则我方必胜。余数为0，则敌人必胜。任意回合中，必败方拿n个，必胜方拿4-n个，可使桌面石子数减少4

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 is not 0
