class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.visited = 0


    def visit(self, url: str) -> None:
        self.visited += 1
        self.history = self.history[:self.visited]
        self.history.append(url)
        


    def back(self, steps: int) -> str:
        self.visited = max(0, self.visited-steps)
        return self.history[self.visited]


    def forward(self, steps: int) -> str:
        self.visited = min(len(self.history)-1, self.visited+steps)
        return self.history[self.visited]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
