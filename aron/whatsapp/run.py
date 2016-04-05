from yowsup.stacks import  YowStackBuilder
from layer import SendLayer
from yowsup.layers.auth import AuthError
from yowsup.layers import YowLayerEvent
from yowsup.layers.auth import YowAuthenticationProtocolLayer
from yowsup.layers.network import YowNetworkLayer


CREDENTIALS = ("917639905993", "RvA9EAe0Io3eUU+A2bJ19KxsYkA=") # replace with your phone and password

if __name__==  "__main__":

    stackBuilder = YowStackBuilder()

    stack = stackBuilder.pushDefaultLayers(True).push(SendLayer).build()
    messages = [
        ("917795704226@s.whatsapp.net" , "Hello yo albin"),
    ]

    stack.setProp(SendLayer.PROP_MESSAGES, messages)
    stack.setProp(YowAuthenticationProtocolLayer.PROP_PASSIVE, True)
    stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)
    # stack.setCredentials(credentials)

    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))   #sending the connect signal

    stack.loop() #this is the program mainloop