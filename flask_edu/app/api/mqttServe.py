from flask_mqtt import Mqtt



class stack_edu_mqtt(object):
    def __init__(self,app):
        self.mymqtt = Mqtt(app)
        print("init mqtt successfully!")
        self.mymqtt.publish('home/mytopic', 'this is my message')

        self.mymqtt.subscribe('home/mytopic')
        self.mymqtt.subscribe('v1/device/answer')
        self.mymqtt.subscribe('v1/device/regist')



        @self.mymqtt.on_message()
        def handle_mqtt_message(client, userdata, message):
            print("recieve successfully")
            print(message.topic)
            print(message.payload)
            self.mymqtt.publish('v1/server/question/'+'imei', "question")
            


    
    def send_question(self,imei,question):
        self.mymqtt.publish('v1/server/question/'+imei, question)

