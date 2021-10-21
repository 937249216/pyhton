import threading
import traceback

def my_func():
    raise BaseException("thread exception")


class ExceptionThread(threading.Thread):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        """
        Redirect exceptions of thread to an exception handler.
        """
        threading.Thread.__init__(self, group, target, name, args, kwargs, verbose)
        if kwargs is None:
            kwargs = {}
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._exc = None

    def run(self):
        try:
            if self._target:
                self._target()
        except BaseException as e:
            import sys
            self._exc = sys.exc_info()
        finally:
            #Avoid a refcycle if the thread is running a function with an argument that has a member that points to the thread.

            del self._target, self._args, self._kwargs

    def join(self):
        threading.Thread.join(self)
        if self._exc:
            msg = "Thread '%s' threw an exception: %s" % (self.getName(), self._exc[1])
            new_exc = Exception(msg)
            raise new_exc.__class__(new_exc).with_traceback(self._exc[2])


t = ExceptionThread(target=my_func, name='my_thread')
t.start()
try:
    t.join()
except:
    traceback.print_exc()
