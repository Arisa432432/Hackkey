from flask import Flask, redirect, request, render_template
import requests, uuid

app = Flask(__name__)

# ===== 여기만 네 정보로 바꿔 =====
DISCORD_CLIENT_ID = "1470614217509044389"
DISCORD_CLIENT_SECRET = "ckI9ryMsVg1k0XI5ShohkG3HXgzfAtyQ"
DISCORD_BOT_TOKEN = "MTQ3MDYxNDIxNzUwOTA0NDM4OQ.GwsFCY.hg5dFtzAgEEUSTkAJaA8TttksmRjygkwVzkNeQ"
GUILD_ID = "1468512911411511316"
REDIRECT_URI = "https://hackkey.onrender.com/callback"
INVITE_LINK = "https://discord.gg/Rd7Nab8tmv"
# ================================

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return redirect(
        "https://discord.com/oauth2/authorize"
        f"?client_id={DISCORD_CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&response_type=code"
        "&scope=identify"
    )

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return render_template("index.html", error="로그인 실패")

    # (중간 Discord 로직은 기존 그대로)

    if member.status_code != 200:
        return render_template(
            "index.html",
            error="디스코드 서버에 먼저 들어와 주세요"
        )

    key = "KEY-" + uuid.uuid4().hex[:16].upper()
    return render_template("index.html", key=key)

    return f"""
        <h3>✅ 키 발급 완료</h3>
        <code>{key}</code>
        <p>복사해서 사용하세요</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
