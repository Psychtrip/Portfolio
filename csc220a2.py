def flatten(data):
    """

   :param data:
   :return: data
   """
    data = list(data)
    if any(isinstance(sub, list) for sub in data):
        for i in range(len(data)):
            if isinstance(data[i], list):
                if data[i]:
                    data.insert(i, (data[i].pop(0)))
                    return flatten(data)
                else:
                    data = list(filter(None, data))
                    return flatten(data)

    elif any(isinstance(sub, tuple) for sub in data):
        for i in range(len(data)):
            if isinstance(data[i], tuple):
                data[i] = list(data[i])
                return flatten(data)

    else:
        return tuple(data)
