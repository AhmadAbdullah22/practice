# class point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p = point(3, 5)
# print(p.x)
# print(p.y)

from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "My name is Ahmad."