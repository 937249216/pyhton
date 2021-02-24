def dictFunc(dicParms):
    result={}
    for key,value in dicParms.items():
        if len(value)>2:
            result[key]=value[:2]
            pass
        else:
            result[key]=value
        pass
    pass
    return result
    
  
dictObj={'name':'欧阳下雨','hobby':['唱歌','跳舞','打篮球'],'pro':'中国艺术'}
print(dictFunc(dictObj))