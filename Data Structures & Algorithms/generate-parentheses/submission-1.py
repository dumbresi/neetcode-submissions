class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result:List[str]=[]
        def generate(index:int,n:int,openb:int, close:int, s:str):
            if close==n:
                result.append(s)
                return
            

            if openb<n:
                s+="("
                openb+=1
                generate(index+1,n,openb,close,s)
                s=s[:len(s)-1]
                openb-=1
            
            if close<openb:
                s+=")"
                close+=1
                generate(index+1,n,openb,close,s)
                s=s[:len(s)-1]
                close-=1
        generate(0,n,0,0,"")
        return result

        