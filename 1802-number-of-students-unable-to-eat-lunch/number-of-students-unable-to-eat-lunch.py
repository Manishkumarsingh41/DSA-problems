class Solution(object):
    def countStudents(self, students, sandwiches):
        rem = len(students)
        cnt = {0: 0, 1: 0}

        for s in students:
            cnt[s] += 1

        for s in sandwiches:
            if cnt[s] > 0:
                rem -= 1
                cnt[s] -= 1
            else:
                return rem
        return rem
