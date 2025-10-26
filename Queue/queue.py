from collections import deque

queue =  deque()

queue.appendleft({'ticker':'NVDA', 'time':'11:30 AM','Price':154.25})
queue.appendleft({'ticker':'NVDA', 'time':'11:31 AM','Price':154.55})
queue.appendleft({'ticker':'NVDA', 'time':'11:32 AM','Price':154.99})
queue.appendleft({'ticker':'NVDA', 'time':'11:33 AM','Price':155.75})

print(queue.pop()) #{'ticker': 'NVDA', 'time': '11:30 AM', 'Price': 154.25}
print(queue.pop()) #{'ticker': 'NVDA', 'time': '11:31 AM', 'Price': 154.55}
print(queue.pop()) #{'ticker': 'NVDA', 'time': '11:32 AM', 'Price': 154.99}


