class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        
        for x in s:
            if x=='[' or x=='(' or x=='{':
                stack.append(x)
            else:
                if not stack:
                    return False
                a=stack.pop()
                if((x=='}' and a!='{') or (x==']' and a!='[') or (x==')' and a!='(')):
                    return False
        if not stack :
            return True
        return False
        

            
            