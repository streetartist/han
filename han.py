from redbaron import *
from googletrans import translater

def translate(red):
    for i in range(0,len(red)):
        if isinstance(red[i], StringNode):
            red[i].value = translater(red[i].value)
        elif isinstance(red[i], CommentNode):
            red[i].value = translater(red[i].value)
        elif isinstance(red[i], DefNode):
            translate(red[i].value)
        elif isinstance(red[i], ClassNode):
            translate(red[i].value)
        
def transfile(file, addname =""):
    with open(file, "r") as f:
        red = RedBaron(f.read())
    translate(red)
    
    with open(file + addname, "w") as f:
        f.write(red.dumps())
        
if __name__ = "__main__":
    transfile("demo.py")
