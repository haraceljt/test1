import logging
import os
import datetime
class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #创建一个控制台输出流
        # console = logging.StreamHandler()
        # logger.addHandler(console)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, 'logs')
        log_file = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'

        #创建一个输出到文件
        # file_path = os.path.join(os.getcwd(),'logs\\test.log')
        # print(file_path)
        self.file_handle = logging.FileHandler(log_file, 'a', encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(module)s %(lineno)s : %(levelname)s--> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

        self.logger.debug("debug")
        #使用完之后要关闭
        # console.close()
        # logger.removeHandler(console)

    def get_logger(self):
        return self.logger

    def close_handle(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)

if __name__ == '__main__':
    log = UserLog()
    logger = log.get_logger()
    logger.debug("debug log")
    logger.info('info log')
    log.close_handle()
