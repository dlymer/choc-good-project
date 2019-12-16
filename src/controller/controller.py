#choclately goodness controller
#from flask import Flask,jsonify
#from model import model

#build the app and refer it to the flask main
#app = Flask(__name__)

class Controller():

    #test method
    #@app.route('/helloworld', methods='[GET]')
    def renderHelloWorld(self):
        self.conModel = 'Test' #model.getHelloWorld()
        return jsonify(self.conModel)


controller = Controller()

"""if __name__== '__main__':
    app.run()"""
