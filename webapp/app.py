import web

urls = (
    '/', 'Index'
)
app = web.application(urls, globals())

class Index:
    def GET(self):
        return 'Hello docker world!'

if __name__ == "__main__":
    app.run()
