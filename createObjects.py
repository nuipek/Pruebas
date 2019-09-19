'''
Created on 29 nov. 2018

@author: saparicio
'''


class OnlyCreatable(object):

    __create_key = object()

    @classmethod
    def create(cls, value):
        return OnlyCreatable(cls.__create_key, value)

    def __init__(self, create_key, value):
        assert(create_key == OnlyCreatable.__create_key), \
            "OnlyCreatable objects not instanciables"
        self.value = value
            
            

if __name__ == '__main__':
    a =  OnlyCreatable.create(-75)
    #b = OnlyCreatable(a,-75)
    print(a._OnlyCreatable__create_key)