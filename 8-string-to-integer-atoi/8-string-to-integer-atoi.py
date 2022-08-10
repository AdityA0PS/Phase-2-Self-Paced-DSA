class Solution:
    def myAtoi(self, s: str) -> int:
        res,prev,sign,digitFound=0,'','pos',False
        dict1={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
        
        def func(res):
            return res if -2**31<res<2**31-1 else (2**31-1 if res>=2**31-1 else -2**31)            
        
        for c in s:
            if (digitFound==False and dict1.get(c,'')==''):
                if c not in (' ','-','+'):
                    return 0
            if dict1.get(prev,'')!='' and dict1.get(c,'')=='':                
                return func(res)
            if dict1.get(c,'')=='' and prev in ['-','+']:
                return 0
            if dict1.get(c,'')!='':
                digitFound=True
                res=-1*int(c) if prev=='-' else res*10+(int(c) if sign=='pos' else -1*int(c))
            if c in ['+','-',' ']:
                sign='neg' if prev in (' ','') and c=='-' else 'pos'                     
            prev=c
        return func(res)  