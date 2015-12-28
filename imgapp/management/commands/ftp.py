import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from django.core.management.base import BaseCommand
from imgapp.models import UnprocessedImg, ProcessedImg


class ImgDBHandler(FTPHandler):

    def on_connect(self):
        print "%s:%s connected" % (self.remote_ip, self.remote_port)

    def on_disconnect(self):
        print "%s:%s disconnected" % (self.remote_ip, self.remote_port)

    def on_login(self, username):
        print "%s logged in..." % username

    def on_logout(self, username):
        print "%s logged out..." % username

    def on_file_sent(self, path):
        print "%s file sent..." % path

    def on_file_received(self, path):
        print "%s file received..." % path
        fn = os.path.basename(path)
        base = os.path.dirname(path)
        serial, ext = os.path.splitext(fn)
        nf = UnprocessedImg.objects.create(ext=ext, serial=serial, base=base)
        nf.save()
        os.rename(path, nf.get_path())

    def on_incomplete_file_sent(self, fn):
        # do something when a file is partially sent
        pass

    def on_incomplete_file_received(self, fn):
        os.remove(fn)


class Command(BaseCommand):
    help = "Start FTP server"

    def handle(self, *args, **options):
        if not os.path.exists(os.path.join(os.getcwd(), "ftp", "unprocessed")):
            os.makedirs(os.path.join(os.getcwd(), "ftp", "unprocessed"))

        if not os.path.exists(os.path.join(os.getcwd(), "ftp", "processed")):
            os.makedirs(os.path.join(os.getcwd(), "ftp", "processed"))

        authorizer = DummyAuthorizer()
        authorizer.add_user('pi', 'raspberry', './ftp/unprocessed', perm='w')
        authorizer.add_user('printer', 'spool', './ftp/processed', perm='r')

        handler = ImgDBHandler
        handler.authorizer = authorizer

        address = ('', 2121)
        server = FTPServer(address, handler)

        server.max_cons = 256
        server.max_cons_per_ip = 5

        server.serve_forever()
