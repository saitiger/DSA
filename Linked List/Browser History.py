class Browser:
    class Node:
        def __init__(self, url):
            self.url = url
            self.next = None
            self.prev = None

    def __init__(self, homepage: str) -> None:
        self.head = self.Node(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        node = self.Node(url)
        self.curr.next = node
        node.prev = self.curr
        self.curr = node

    def back(self, steps: int) -> str:
        while self.curr.prev != None and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while self.curr.next != None and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url
