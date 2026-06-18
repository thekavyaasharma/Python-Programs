# 1344. Angle Between Hands of a Clock - MEDIUM 

class Solution:
    def angleClock(self, hour : int , minutes : int ) -> float:
        minuteAngle = 6 * minutes
        hourAngle = 30.0 * (hour % 12) + 0.5 * minutes

        diff = abs(minuteAngle - hourAngle)

        return min(diff, 360 - diff)