from bocadillo import App

import settings


app = App()

@app.route("/")
async def index(req, res):
    title = settings.config.get("Title")
    res.text = f"Site Title: {title}"