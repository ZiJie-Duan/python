import json
import ctypes


class MEMO_RW:

    def __init__(self, memo) -> None:
        self.memo = memo
        self.memo_path = "memo.json"
        self.memo_load()
    
    def __call__(self, key):
        return self.memo[key]
    
    def memo_load(self):
        try:
            temp_data = {}
            with open(self.memo_path,"r") as f:
                temp_data = json.load(f)
            for key, value in temp_data.items():
                self.memo[key] = value
        except:
            pass

    def memo_write(self):
        with open(self.memo_path,"w") as f:
            json.dump(self.memo,f)


class MEMO_MINI:

    def __init__(self):
        self.memo = {}
        self.var_remap = {}
        self.memorw = MEMO_RW(self.memo)

    def add_var_remap(self,key,value):
        self.var_remap[key] = id(value)
    
    def get_obj_value(id_x):
        ptr = ctypes.c_long(id_x)
        obj = ctypes.cast(ptr, ctypes.py_object).value
        return obj
    
    def set_obj_value(self,var,value):
        ptr = ctypes.c_long(id(var))
        a = ctypes.cast(ptr, ctypes.py_object).value
        a = value
        

    def track(self,key,value):
        if key in self.memo.keys():
            self.set_obj_value(value,self.memo[key])
            self.add_var_remap(key,value)
            print(value)
        else:
            self.memo_add(key,value)
    
    def memo_add(self,key,value):
        self.memo[key] = value
        self.add_var_remap(key,value)
        self.memorw.memo_write()

    def memo_del(self,key):
        del self.memo[key]
        del self.var_remap[key]


mm = MEMO_MINI()

name = {1:2}
mm.track("name",name)

print(name)
input()