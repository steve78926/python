
class Dict(dict):
        初始化字典

class _LasyConnection(object):
   包括：cursor(), commit(), rollback(), cleanup()

class _DbCtx(threading.local):
    '''
    Thread local object that holds connection info.
    '''
    def __init__(self):
        self.connection = None
        self.transactions = 0

    def is_init(self):
        return not self.connection is None

    def init(self):
        logging.info('open lazy connection...')
        self.connection = _LasyConnection()  #不明白
        self.transactions = 0

    def cleanup(self):
        self.connection.cleanup()
        self.connection = None

    def cursor(self):
        '''
        Return cursor
        '''
        return self.connection.cursor()

# thread-local db context:
_db_ctx = _DbCtx()

def create_engine(user, password, database, host='127.0.0.1', port=3306, **kw):

    params[k] = kw.pop(k, v)       # 不明白: kw， pop(k, v)返回什么
    params.update(kw)              # params是个字典，怎么会有update()


class _ConnectionCtx(object):
    可以with的对象，包括__enter__,  __exit__

class _TransactionCtx(object):

def _select(sql, first, *args):
    if cursor.description:      #cursor 有这个属性吗？ description


2016-12-20 星期二   db.py  328行


