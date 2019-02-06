# TODO: Copy the code in
#     m1e_mqtt_receiver.py
# as your starting point, pasting its code here.
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import time

# name1 = input("Enter one name (subscriber): ")
# name2 = input("Enter another name (publisher): ")
#
# mqtt_client = com.MqttClient()
# mqtt_client.connect(name1, name2)
# time.sleep(1)  # Time to allow the MQTT setup.
# print()
#


def window():
    mqtt_client = com.MqttClient()



    root = tkinter.Tk()
    root.title('T chat 1.0')
    frame1 = ttk.Frame(root, padding=30)
    frame1.grid()
    lable1 = ttk.Label(frame1, text="Enter the publisher and subscriber below")
    lable1.grid()
    sub = ttk.Entry(frame1)
    sub.grid()
    pub = ttk.Entry(frame1)
    pub.grid()


    button4 = ttk.Button(frame1, text='confirm')
    button4['command'] = (lambda: mqtt_client.connect(sub.get(), pub.get()))
    button4.grid()


    blank=ttk.Entry(frame1)
    blank.grid()
    button3=ttk.Button(frame1,text='send your message')
    button3['command']=(lambda: sendMessage(mqtt_client, blank))
    button3.grid()



    time.sleep(1)  # Time to allow the MQTT setup.



    root.mainloop()
def rs(x1,x2):
    x1=str(x2)
    return x1
# Then modify the code so that it receives messages from your
#    m2_tkinter_as_mqtt_sender.py
# module and PRINTS them.
def sendMessage(mqtt_client, blank):
    mqtt_client.send_message("say_it", blank.get())
    print("sent")
window()