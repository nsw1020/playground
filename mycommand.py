import sys
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration

@Configuration()
class MyCommand(StreamingCommand):
    def stream(self,records):
        for record in records:
            record['hello']='Sungwuk Hello'
            yield record

if __name__== '__main__':
    dispatch(MyCommand, sys.argv, sys.stdin, sys.stdout, __name__)