
# 获取返回报文里需要保留的字段
def getRealDynamicParam(data, dynamicParamsKey):  # dict,str
    if dynamicParamsKey in data.keys():
        dynamicParamsValue = data[dynamicParamsKey]
        return dynamicParamsValue
    for key in data.keys():
        if isinstance(data[key], list):
            for dataValue in data[key]:
                if isinstance(dataValue, dict):
                    for k, v in dataValue.items():
                        if dynamicParamsKey == k:
                            dynamicParamsValue = v
                            return dynamicParamsValue
                        elif isinstance(v, dict):
                            dynamicParamsValue = getRealDynamicParam(v, dynamicParamsKey)
                            if dynamicParamsValue:
                                return dynamicParamsValue
        elif isinstance(data[key], dict):
            dynamicParamsValue = getRealDynamicParam(data[key], dynamicParamsKey)
            if dynamicParamsValue:
                return dynamicParamsValue
