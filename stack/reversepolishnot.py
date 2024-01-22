class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr=[]
        l=len(tokens)
        for i in range(l):
            if tokens[i] == '+':
                a=arr.pop()
                b=arr.pop()
                arr.append(a+b)

            elif tokens[i] == '-':
                a=arr.pop()
                b=arr.pop()
                arr.append(b-a)
            elif tokens[i] == '*':
                a=arr.pop()
                b=arr.pop()
                arr.append(b*a)
            elif tokens[i] == '/': 
                a=arr.pop()
                b=arr.pop()
                if abs(b)< abs(a):
                    arr.append(0)
                elif b<=0 or a<= 0:
                     arr.append(math.ceil(b/a))

                else:
                    arr.append(math.floor(b/a))
                    print(math.floor(b/a))
            else:
                arr.append(int(tokens[i]))
        return arr[0]




        