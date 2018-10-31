import asyncio
import logging


class Logger(object):

    def __init__(self, logname = "log.txt", loglevel = logging.DEBUG, loggername = "logger"):

        self.logger = logging.getLogger(loggername)
        self.logger.setLevel(loglevel)
        
        format = '%(asctime)s %(filename)s: %(levelname)s %(message)s'
        datefmt = '%Y/%m/%d %H:%M:%S'
        formatter = logging.Formatter(format,datefmt)
        
        # log to file
        fh = logging.FileHandler(logname)
        fh.setLevel(loglevel)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        
        # print log
        ch = logging.StreamHandler()
        ch.setLevel(loglevel)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

def main():

    ### init logger
    logger = Logger().logger
    ### print and file log.txt
    logger.info("Info")
    logger.error("error")
    logger.exception('Exception')

if __name__ == '__main__':
    main()


class EchoServerClientProtocol(asyncio.Protocol):
    
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        #print('Data received: {!r}'.format(message))

        #print('Send: {!r}'.format(message))
        #self.transport.write(data)

        #print('Close the client socket')
        #self.transport.close()

    def connection_lost(self, exc):
        self.transport.close()

    def init_log(self):
        logging.getLogger('logger')




loop = asyncio.get_event_loop()
# Each client connection will create a new protocol instance
coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8888)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()