def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        
list(chunks(range(10, 75), 10))