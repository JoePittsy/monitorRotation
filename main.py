import paho.mqtt.client as mqtt
import os

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("monitor/#")

def on_message(client, userdata, msg):
    decoded_msg = str(msg.payload, "utf-8")
    if ("upright" in decoded_msg):
        os.system("xrandr --output eDP --rotate normal")
    elif("left" in decoded_msg):
        os.system("xrandr --output eDP --rotate left")
    elif("right" in decoded_msg):
        os.system("xrandr --output eDP --rotate right")
    elif("upside down" in decoded_msg):
        os.system("xrandr --output eDP --rotate inverted")



def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("192.168.0.12", 1883, 60)

    client.loop_forever()

if __name__ == "__main__":
    main()