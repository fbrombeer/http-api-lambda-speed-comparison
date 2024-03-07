from http_api_lambda import App


app = App()

@app.get("/")
def root():
    return {"message": "Hello World!"}


def handler(event, context):
    return app.handle_request(event, context)