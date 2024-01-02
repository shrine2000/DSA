class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        if mainTank < 5:
            return mainTank * 10

        ans = 0

        while mainTank > 0:
            if mainTank >= 5:
                ans += 50
                mainTank -= 5
                if additionalTank > 0:
                    mainTank += 1
                    additionalTank -= 1
                    continue
            ans += mainTank * 10
            mainTank = 0
        return ans
