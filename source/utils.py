import re, random

def payload(source: str) -> dict:
    data = {'av': re.search(r'USER_ID":"(\d+)"', source).group(1),'__aaid': '0','__user': re.search(r'USER_ID":"(\d+)"', source).group(1),'__a': '1','__req': '27','__hs': re.search(r'haste_session":"(.*?)"', source).group(1),'dpr': '3','__ccg': 'EXCELLENT','__rev': re.search(r'spin_r":(\d+),', source).group(1),'__s': '','__hsi': re.search(r'hsi":"(\d+)"', source).group(1),'__dyn': '','__csr': '','__hsdp': '','__hblp': '','__comet_req': '15','fb_dtsg': re.search(r'DTSGInitialData",\[\],\{"token":"(.*?)"', source).group(1),'jazoest': re.search(r'jazoest=(\d+)"', source).group(1),'lsd': re.search(r'LSD",\[\],\{"token":"(.*?)"', source).group(1),'__spin_r': re.search(r'spin_r":(\d+),', source).group(1),'__spin_b': 'trunk','__spin_t': re.search(r'__spin_t":(\d+),', source).group(1),'fb_api_caller_class': 'RelayModern','server_timestamps': 'true',}
    return data

def convert_react_type(reaction_type: str) -> str:
    data = {'like': '1635855486666999','love': '1678524932434102','care': '613557422527858','haha': '115940658764963','wow': '478547315650144','sad': '908563459236466','angry': '444813342392137'}
    
    #Mengembalikan reaksi acak jika reaction_type tidak ada yang cocok
    try: reaction_id = data[reaction_type]
    except KeyError: reaction_id = data[random.choice(['like', 'love', 'care', 'haha', 'wow', 'sad', 'angry'])]
    
    return reaction_id

