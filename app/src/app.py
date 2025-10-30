from flask import Flask, jsonify, request

app = Flask(__name__)

# Traefikで /group1/app を StripPrefix しているので
# バックエンドから見えるパスは "/" になる
@app.get("/")
def root():
    return (
            "<h1>App (Flask)</h1>"
            "<p>Traefik の StripPrefix により, アプリは <code>/</code> に見える.</p>"
            "<p>例: <code>/group1/app/</code> でアクセスしてください.</p>"
    )

@app.get("/healthz")
def healthz():
    return jsonify(status="ok", forwarded_proto=request.headers.get("X-Forwarded-Proto"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
