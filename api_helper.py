from NorenRestApiPy.NorenApi import  NorenApi
from threading import Timer
import pandas as pd
import time


def get_time(time_string):
    data = time.strptime(time_string,'%d-%m-%Y %H:%M:%S')

    return time.mktime(data)


class CubeApiPy(NorenApi):
    def __init__(self):
        NorenApi.__init__(self, host='https://cube.tradejini.com/NorenWClientTP/', websocket='wss://cube.tradejini.com/NorenWSTP/', eodhost='http://cube.tradejini.com/chartApi/getdata/')

    
    