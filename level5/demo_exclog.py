import logging
class DemoFile():
    def __init__(self):
        logging.basicConfig(filename="filelog.txt",level=logging.WARNING)

    def FileOpen(self):
        try:
            f = open("text", "r")
        except FileNotFoundError as msg:
            logging.exception(msg)


if __name__ == ' __main__':
    obj = DemoFile()
    obj.FileOpen()
