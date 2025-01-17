from flask import Flask, request,send_file, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def root():
    return "<h1 style='text-align:center;color:rebeccapurple;'>Image Server!</h1>"


imagesPath = "./Images"
images = [
    {"name": "Android", "logo": "android.svg"},
    {"name": "html", "logo": "html5.svg"},
    {"name": "Bootstrap", "logo": "bootstrap5.svg"},
    {"name": "css", "logo": "css.svg"},
    {"name": "chromium", "logo": "chromium.svg"},
    {"name": "brave", "logo": "brave.svg"},
    {"name": "firefox", "logo": "firefox.svg"},
    {"name": "React", "logo": "reactjs.svg"},
    {"name": "jquery", "logo": "jquery.svg"},
    {"name": "svelte", "logo": "sveltejs.svg"},
    {"name": "javascript", "logo": "javascript.svg"},
    {"name": "kotlin", "logo": "kotlin.svg"},
    {"name": "nodejs", "logo": "nodejs.svg"},
    {"name": "express", "logo": "expressjs-light.svg"},
    {"name": "python", "logo": "python.svg"},
    {"name": "supabase", "logo": "supabase.svg"},
    {"name": "sublime", "logo": "sublime.svg"},
    {"name": "git", "logo": "git.svg"},
    {"name": "github", "logo": "github-light.svg"},
    {"name": "linux", "logo": "linux.svg"},
    {"name": "mongodb", "logo": "mongodb.svg"},
    {"name": "flask", "logo": "flask-light.svg"},
    {"name": "java", "logo": "java.svg"},
    {"name": "c", "logo": "c.svg"},
    {"name": "docker", "logo": "docker.svg"},
    {"name": "prettier", "logo": "prettier.svg"},
    {"name":"Render","logo":"render.svg"},
    {"name":"insomnia","logo":"insomnia.svg"},
    {"name":"vim","logo":"vim.svg"},
    {"name":"vscode","logo":"vscode.svg"},
    {"name":"chatgpt","logo":"chatgpt.svg"},
    {"name":"eslint","logo":"eslint.svg"},
    {"name":"github-copilot","logo":"github-copilot.svg"},
    {"name":"neovim","logo":"neovim.svg"},
    {"name":"npm","logo":"npm.svg"},
    {"name":"postgresql","logo":"postgresql.svg"},
    {"name":"postman","logo":"postman.svg"},
    {"name":"resend","logo":"resend.svg"},
    {"name":"sass","logo":"sass.svg"},
    {"name":"ubuntu","logo":"ubuntu.svg"},
    {"name":"vitest","logo":"vitest,svg"},
    {"name":"webpack","logo":"webpack.svg"},
    {"name":"vitejs","logo":"vitejs.svg"}





    # Add more skills here
]


@app.route("/Images/<name>",methods = ['GET'])
def serve_image(name):
    file_path = f"{imagesPath}/{name}"
    try:
        return send_file(file_path)
    except FileNotFoundError:
        return f"File {name} not found",404
    

@app.route("/serve_all_images")
def image_links():
    base_url = request.host_url + "Images/"
    image_links = [{"name": image["name"], "url": base_url + image["logo"]} for image in images]
    return jsonify(image_links)


if __name__ == "__main__":
    app.run(debug=True)
    