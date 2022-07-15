import time 
import sys
import stomp

class Listener(stomp.ConnectionListener):

    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        print('received a message "%s"' % message)

hosts = [('broker-amq7.apps.rh-lab.sandbox1168.opentlc.com', 80)]

conn = stomp.Connection(host_and_ports=hosts)

conn.set_listener('', Listener()) 

conn.start()
conn.connect('admin', 'admin123', wait=True)

conn.subscribe(destination='/queue/helloworld', id=1, ack='auto')

conn.send(body=' '.join(sys.argv[1:]), destination='/queue/helloworld')

time.sleep(2)
conn.disconnect()
