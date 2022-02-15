from flask import Flask,jsonify,render_template
import socket
app = Flask(__name__)

# @app.route("/fetchdetails")
def fetchdetails():
    Host= socket.gethostname()
    IP= socket.gethostbyname(Host)
    print("Hostname: ",Host)
    print("IP :",IP)
    return str(Host),str(IP)


@app.route("/")
def hello_world():
    return "<p> Hello, Alnassaj!</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/web")
def web():
    host,ip = fetchdetails()
    return render_template('hello.html',HostName=host, IPaddress=ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)