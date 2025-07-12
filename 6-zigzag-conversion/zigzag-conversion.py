class Solution: 
   def convert(self, s, numRows):
        if numRows==1 or numRows>=len(s):
            return s

        rows=['']*numRows
        Current_row=0
        going_down = False

        for char in s:
            rows[Current_row] += char

            if Current_row==0 or Current_row==numRows-1:
                going_down=not going_down

            Current_row+=1 if going_down else -1

        return ''.join(rows)

        