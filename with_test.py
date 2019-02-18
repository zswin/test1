#coding=utf-8
class MyContextManager(object):
    def __enter__(self):
        print("Entering...")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting...")
        if exc_type is None:
            print("No exceptions!")
            return False
        elif exc_type is ValueError:
            print("Value error!")
            return True
        else:
            print("other error!")
            return True

if __name__ == "__main__":
    with MyContextManager():
        print('test1')
        raise (ValueError)

    with MyContextManager():
        print('test2')