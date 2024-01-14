def get_all_differences(list_a,list_b):
    return [[i,a,b] for i,(a,b) in enumerate(zip(list_a,list_b)) if a!=b]
    
    