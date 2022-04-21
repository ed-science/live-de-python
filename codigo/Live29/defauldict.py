from collections import defaultdict

def none():
    return None

d = defaultdict(none)

d['css']

d |= {'css':00, 'html':'<body></body>'}

print(d)
