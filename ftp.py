from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class ImgDBHandler(FTPHandler):

    def on_connect(self):
        print "%s:%s connected" % (self.remote_ip, self.remote_port)

    def on_disconnect(self):
        print "%s:%s disconnected" % (self.remote_ip, self.remote_port)
        pass

    def on_login(self, username):
        print "%s logged in..." % username
        pass

    def on_logout(self, username):
        print "%s logged out..." % username
        pass

    def on_file_sent(self, file):
        # do something when a file has been sent
        pass

    def on_file_received(self, file):
        print "%s file received..." % file
        pass

    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        pass

    def on_incomplete_file_received(self, file):
        import os
        os.remove(file)


def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('pi', 'raspberry', './ftp', perm='w')

    handler = ImgDBHandler
    handler.authorizer = authorizer
    handler.timeout =

    address = ('', 2121)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()

if __name__ == '__main__':
    main()