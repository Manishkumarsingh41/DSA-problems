class Solution:
    def minTimeToVisitAllPoints(self, points):
        i=0
        j=1
        s=0
        t=len(points)
        for k in range(len(points)-1):
           
            if i<t and j<t:
             
                a=points[k][i]
                b=points[k][j]
                c=points[k+1][i]
                d=points[k+1][j]
                e=max(abs(a-c),abs(b-d))
               
                s+=e
              
        return s