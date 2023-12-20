def index():
    with open('/Users/ajzanylsabdanbekova/Desktop/python/sockets/socket/templates/index.html') as template:
        return template.read()
    

def blog():
    with open('/Users/ajzanylsabdanbekova/Desktop/python/sockets/socket/templates/blog.html') as template:
        return template.read()