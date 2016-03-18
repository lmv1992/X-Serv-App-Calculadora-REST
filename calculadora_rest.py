#!/usr/bin/python

"""
API REST

Recurso:
el recurso sera el el operador y los dos numeros que se le pase
despues del /operador/.

Verbo:
GET. 		

Explicacion:
utilizamos mensajes de tipo GET debido no vamos querer que el
 resultado, de cualquier operacion de las que se han propuesto,
 se actualice o se guarde.
"""


import socket
import random


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)
number1 =0 
number2 =0
while True:
    print 'Waiting for connections'
    (recvSocket, address) = mySocket.accept()
    print 'HTTP request received:'
    request= recvSocket.recv(1024)
    print request
    metodo = request.split(' ',1)[0]
    recurso = request.split(' ',2)[1][1:]
    if recurso =='':
        htmlCode ='200 OK'
        htmlBody = '<html><body>'
        htmlBody +='<h1>"OPERACIONES"</h1>'
        htmlBody += '<p>ENVIE DE ESTA FORMA: url/operador/numero1/numero2</p>'
        htmlBody += '<p>Para Sumar escriba "/sum"</p>'
        htmlBody += '<p>Para Restar escriba "/res"</p>'
        htmlBody += '<p>Para Multiplicar escriba "/mul"</p>'
        htmlBody += '<p>Para Dividir escriba "/div"</p>'
        htmlBody +='</ul></body></html>'
    else:# si envia algo de la forma /../../../..
		operador = recurso.split('/')[0]
		if operador =='sum' or operador == 'res' or operador == 'mul' or operador =='div':
			try:
				number1 = int(recurso.split('/')[1])
				number2 = int(recurso.split('/')[2])
			except ValueError:
				htmlCode ='404 Not Found'
				htmlBody = '<html><body>'
				htmlBody +='<p>NUMERO(S) INCORRECTO(S)</p>' 
				htmlBody +='</body></html>'
			except IndexError:
				htmlCode ='404 Not Found'
				htmlBody = '<html><body>'
				htmlBody +='<p>ARGUMENTO(S) INCORRECTO(S)</p>' 
				htmlBody +='</body></html>'
			if operador == 'sum':
				htmlCode ='200 OK'
				htmlBody ='<html><body>'
				htmlBody +='<p>'+str(number1)+'+'+str(number2)+'='+str(number1+number2)+'</p>'
				htmlBody +='</body></html>'
			elif operador == 'res':
				htmlCode ='200 OK'
				htmlBody ='<html><body>'
				htmlBody +='<p>'+str(number1)+'-'+str(number2)+'='+str(number1-number2)+'</p>'
				htmlBody +='</body></html>'
			elif operador == 'mul':
				htmlCode ='200 OK'
				htmlBody ='<html><body>'
				htmlBody +='<p>'+str(number1)+'*'+str(number2)+'='+str(number1*number2)+'</p>'
				htmlBody +='</body></html>'
			else:
				htmlCode ='200 OK'
				htmlBody ='<html><body>'
				htmlBody +='<p>'+str(number1)+'/'+str(number2)+'='+str(number1/number2)+'</p>'
				htmlBody +='</body></html>'				
		else:
			htmlCode ='404 Not Found'
			htmlBody = '<html><body>'
			htmlBody +='<p>EL OPERADOR ENVIADO ES INCORRECTO</p>' 
			htmlBody +='</body></html>'
    recvSocket.send("HTTP/1.1 "+htmlCode+"\r\n\r\n" + htmlBody + "\r\n")
    recvSocket.close()
