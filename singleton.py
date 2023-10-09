# import datetime as d1
# import datetime as d2

# print(id(d1))
# print(id(d2))


# class A:
#     _instance = None
    
#     def __init__(self):
#         raise RuntimeError('call get_instance() instead ')
        
#     @classmethod
#     def get_instance(cls):
#         if cls._instance is None:
#             cls._instance = cls.__new__(cls)
#         return cls._instance

# a = A.get_instance()
# b = A.get_instance()

# print(id(a))
# print(id(b))


# class Singlaton(type):
#     _instances = None
    
#     def __call__(self, *args, **kwargs):
#         if self._instances is None:
#             self._instances = super().__call__
#         return self._instances
    
# class Singleton(metaclass=Singlaton):
#     pass


# a1 = Singleton()
# a2 = Singleton()
# print(id(a1))
# print(id(a2))



