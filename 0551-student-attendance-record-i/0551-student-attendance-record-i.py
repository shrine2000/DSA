class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        late_count = 0

        for record in s:
            if record == "A":
                absent_count += 1
                late_count = 0
                if absent_count > 1:
                    return False
            elif record == "L":
                late_count += 1
                if late_count > 2:
                    return False
            else:
                late_count = 0

        return True
