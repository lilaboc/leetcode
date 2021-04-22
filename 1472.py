# https://leetcode.com/problems/design-browser-history/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.back_history = []
        self.forward_history = []
        self.current = homepage
        

    def visit(self, url: str) -> None:
        if self.current:
            self.back_history.append(self.current)
        self.forward_history.clear()
        self.current = url

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if len(self.back_history) > 0:
                url = self.back_history.pop()
                if self.current:
                    self.forward_history.append(self.current)
                self.current = url
            else:
                break
        return self.current
        

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if len(self.forward_history) > 0:
                url = self.forward_history.pop()
                if self.current:
                    self.back_history.append(self.current)
                self.current = url
            else:
                break
        return self.current
    


b = BrowserHistory('monm.com')
print(b.visit('bx.com'))
print(b.visit('bjyfmln.com'))
print(b.back(3))
print(b.visit('ijtrqk.com'))
print(b.visit('dft.com'))
print(b.back(10))
print(b.forward(10))
print(b.visit('yc.com'))
print(b.visit('yhl.com'))
print(b.visit('xynxvix.com'))
print(b.visit('izfscdv.com'))
print(b.visit('cdenhm.com'))
print(b.visit('ocgcjz.com'))
print(b.forward(5))
print(b.forward(5))
print(b.visit('gtd.com'))
print(b.back(9))
print(b.visit('hfeour.com'))
print(b.visit('ghmh.com'))
print(b.visit('nnm.com'))
print(b.visit('knm.com'))
print(b.forward(4))
print(b.visit('cbtg.com'))
print(b.visit('acywod.com'))
print(b.visit('mydr.com'))
