import logging
class FileLog():
    def __init__(self):
        logging.basicConfig(filename="file.txt",level=logging.WARNING)
    def Operation(self):
        try:
            self.x=int(input("enter the number"))
            self.y=int(input("enter the number"))
            print(self.x/self.y)
        except ZeroDivisionError as msg:
            logging.exception(msg)
        except ValueError as msg:
            logging.exception(msg)
if __name__=='__main__':
    obj=FileLog()
    obj.Operation()

