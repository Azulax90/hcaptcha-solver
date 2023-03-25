import datetime, json, re, requests, time, tls_client, os , threading, random, math, base64, hashlib
from os.path import exists
os.system("cls && title No more qin2dm :)")

class Client:
    def __init__(self,client_id="chrome_109", proxies=None, headers=None) -> None:
        self.headers = headers 
        self.proxies = proxies 
        self.client = tls_client.Session(client_identifier=client_id,random_tls_extension_order=True)
        
    def post(self, url, json=None, data=None, params=None):
        res = self.client.post(url,params=params,headers=self.headers, json=json, data=data, proxy=self.proxies)
        return res 
    def get(self, url=None):
        res = self.client.get(url,headers=self.headers, proxy=self.proxies)
        return res 

class Solver:
    def __init__(self,host="discord.com", proxy=None, site_key="4c672d35-0701-42b2-88c3-78380b0db560") -> None:
        
        self.v = 'a0e2c1c'
        self.site_key = site_key
        self.host = host 

        self.client = Client(proxies=f"http://{proxy}", headers={'authority': 'hcaptcha.com','accept': 'application/json','accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','content-type': 'text/plain','origin': 'https://newassets.hcaptcha.com','referer': 'https://newassets.hcaptcha.com/','sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site',})
        
        self.client.headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    def hsw(self, req):
        x = "0123456789/:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        req = req.split(".")

        req = {
            "header": json.loads(
                base64.b64decode(
                    req[0] +
                    "=======").decode("utf-8")),
            "payload": json.loads(
                base64.b64decode(
                    req[1] +
                    "=======").decode("utf-8")),
            "raw": {
                "header": req[0],
                "payload": req[1],
                "signature": req[2]}}

        def a(r):
            for t in range(len(r) - 1, -1, -1):
                if r[t] < len(x) - 1:
                    r[t] += 1
                    return True
                r[t] = 0
            return False

        def ix(r):
            t = ""
            for n in range(len(r)):
                t += x[r[n]]
            return t

        def o(r, e):
            n = e
            hashed = hashlib.sha1(e.encode())
            o = hashed.hexdigest()
            t = hashed.digest()
            e = None
            n = -1
            o = []
            for n in range(n + 1, 8 * len(t)):
                e = t[math.floor(n / 8)] >> n % 8 & 1
                o.append(e)
            a = o[:r]

            def index2(x, y):
                if y in x:
                    return x.index(y)
                return -1
            return 0 == a[0] and index2(a, 1) >= r - 1 or -1 == index2(a, 1)

        def get():
            for e in range(25):
                n = [0 for i in range(e)]
                while a(n):
                    u = req["payload"]["d"] + "::" + ix(n)
                    if o(req["payload"]["s"], u):
                        return ix(n)

        result = get()
        hsl = ":".join([
            "1",
            str(req["payload"]["s"]),
            datetime.datetime.now().isoformat()[:19]
            .replace("T", "")
            .replace("-", "")
            .replace(":", ""),
            req["payload"]["d"],
            "",
            result
        ])
        return hsl
    def label_c(self, lab: str):
            if "containing" in lab:
                th = re.split(r"containing", lab)[-1][1:].strip()
                lab = th[2:].strip() if th.startswith("a") else th
            if "select all" in lab:
                    lab = re.split(r"all (.*) images", lab)[1].strip()
            return lab
                
    def get_captcha(self):
        try:
            start = time.time()
            params = {
                        'v': self.v,
                        'host':self.host,
                        'sitekey': self.site_key,
                        'sc': '1',
                        'swa': '1',
                    }

            checksite = self.client.post('https://hcaptcha.com/checksiteconfig', params=params)
            self.client.headers["content-type"] = 'application/x-www-form-urlencoded'
            
            data = {
                'v': self.v ,
                'sitekey': self.site_key,
                'host': self.host,
                'hl': 'en',
                'motionData': '{"st":1677342868814,"mm":[[72,2,1677342870092],[66,9,1677342870116],[64,12,1677342870132],[64,15,1677342870156],[64,16,1677342870195],[63,20,1677342870229],[60,23,1677342870250],[60,23,1677342870318]],"mm-mp":16.142857142857142,"md":[[63,20,1677342870229]],"md-mp":0,"mu":[[60,23,1677342870314]],"mu-mp":0,"v":1,"topLevel":{"inv":false,"st":1677342868336,"sc":{"availWidth":1536,"availHeight":816,"width":1536,"height":864,"colorDepth":24,"pixelDepth":24,"availLeft":0,"availTop":0,"onchange":null,"isExtended":false},"nv":{"vendorSub":"","productSub":"20030107","vendor":"Google Inc.","maxTouchPoints":0,"scheduling":{},"userActivation":{},"doNotTrack":null,"geolocation":{},"connection":{},"pdfViewerEnabled":true,"webkitTemporaryStorage":{},"hardwareConcurrency":8,"cookieEnabled":true,"appCodeName":"Mozilla","appName":"Netscape","appVersion":"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36","platform":"Win32","product":"Gecko","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36","language":"fr-FR","languages":["fr-FR"],"onLine":true,"webdriver":false,"bluetooth":{},"clipboard":{},"credentials":{},"keyboard":{},"managed":{},"mediaDevices":{},"storage":{},"serviceWorker":{},"virtualKeyboard":{},"wakeLock":{},"deviceMemory":8,"ink":{},"hid":{},"locks":{},"mediaCapabilities":{},"mediaSession":{},"permissions":{},"presentation":{},"serial":{},"usb":{},"windowControlsOverlay":{},"xr":{},"userAgentData":{"brands":[{"brand":"Chromium","version":"110"},{"brand":"Not A(Brand","version":"24"},{"brand":"Google Chrome","version":"110"}],"mobile":false,"platform":"Windows"},"plugins":["internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer"]},"dr":"","exec":false,"wn":[[1536,714,1.25,1677342868339],[686,714,1.25,1677342868750]],"wn-mp":411,"xy":[[0,0,1,1677342868339]],"xy-mp":0,"mm":[[265,92,1677342869621],[226,91,1677342869642],[208,97,1677342869659],[195,105,1677342869675],[185,113,1677342869692],[176,123,1677342869708],[165,138,1677342869732],[158,149,1677342869748],[151,165,1677342869772],[146,177,1677342869795],[145,180,1677342869812],[145,183,1677342869835],[145,185,1677342869851],[145,186,1677342869867],[145,189,1677342869883],[144,193,1677342869899],[142,197,1677342869915],[139,201,1677342869931],[134,209,1677342869955],[129,214,1677342869971],[124,221,1677342869987],[121,225,1677342870003],[119,232,1677342870019],[117,237,1677342870036],[113,247,1677342870060],[108,256,1677342870084]],"mm-mp":8.12280701754386},"session":[],"widgetList":["0k7ihraqm4si"],"widgetId":"0k7ihraqm4si","href":"https://accounts.hcaptcha.com/demo?sitekey=4c672d35-0701-42b2-88c3-78380b0db560","prev":{"escaped":false,"passed":false,"expiredChallenge":false,"expiredResponse":false}}',
                'n': self.hsw(checksite.json()["c"]["req"]),
                'c': "{\"type\":\"" + "hsl" + "\",\"req\":\"" +checksite.json()["c"]["req"] + "\"}"
            }
        
            getcaptcha = self.client.post(f"https://hcaptcha.com/getcaptcha/{self.site_key}", data=data).json()
            
            
            
            ta = getcaptcha["tasklist"]
            rere = getcaptcha["c"]["req"]
            label = getcaptcha['requester_question']['en']
            label = self.label_c(label)
            if exists(f"data/{label}"):
                pass 
            else:
                print(f"[TRAIN] {label}")
                return 
            print(f"[LABEL] {label}")
            
            answ = {}
            th = []
            for u in ta:
                url = str(u["datapoint_uri"])
                image = requests.get(url, stream=True).content
                md5_hash = hashlib.md5(image).hexdigest()
                task = u["task_key"]
                def no_ai(md5_hash, tas):
                    try:
                        mmp = open(f"data/{label}/{md5_hash}.jpg", "rb")
                        mmp.close()
                        a = "true"
                    except:
                        a = "false"
                    answ[tas] = a
                    #print(f'[INFO] {tas} | {a}')
                
                f = threading.Thread(target=no_ai, args=(md5_hash, task,))
                f.start()
                th.append(f)
            
            for m in th:
                m.join()
                
            #answ = json.dumps(answ)
            key= getcaptcha["key"]
            answ = answ
            json_data = {
                'v': self.v,
                'job_mode': 'image_label_binary',
                'answers': answ,
                'serverdomain': self.host,
                'sitekey':self.site_key,
                'motionData': "{\"st\":1677342870974,\"dct\":1677342870974,\"mm\":[[1,273,1677342871171],[1,271,1677342871195],[2,271,1677342871220],[3,271,1677342871252],[4,270,1677342871284],[6,269,1677342871324],[7,268,1677342871396],[8,267,1677342871420],[10,266,1677342871452],[11,265,1677342871468],[15,263,1677342871507],[16,262,1677342871523],[19,261,1677342871539],[22,260,1677342871555],[27,259,1677342871571],[30,257,1677342871587],[32,256,1677342871603],[35,255,1677342871620],[39,254,1677342871636],[45,253,1677342871660],[51,253,1677342871691],[58,252,1677342871707],[62,251,1677342871731],[64,251,1677342871747],[71,251,1677342871771],[75,251,1677342871788],[80,251,1677342871804],[84,251,1677342871867],[85,251,1677342871899],[88,253,1677342871915],[91,254,1677342871931],[96,255,1677342871948],[102,257,1677342871964],[111,261,1677342871988],[119,264,1677342872011],[123,267,1677342872027],[128,270,1677342872043],[132,273,1677342872060],[138,276,1677342872076],[143,279,1677342872092],[149,284,1677342872115],[155,288,1677342872132],[162,294,1677342872148],[167,299,1677342872164],[175,305,1677342872188],[182,310,1677342872213],[187,314,1677342872235],[189,316,1677342872251],[191,317,1677342872267],[192,319,1677342872284],[192,319,1677342872308],[195,322,1677342872332],[195,323,1677342872348],[196,325,1677342872364],[197,325,1677342872506],[201,324,1677342872531],[205,322,1677342872547],[210,320,1677342872563],[212,319,1677342872579],[215,315,1677342872595],[220,314,1677342872611],[225,310,1677342872627],[232,305,1677342872643],[239,303,1677342872660],[248,299,1677342872684],[259,295,1677342872708],[267,294,1677342872724],[271,293,1677342872740],[273,292,1677342872780],[275,292,1677342872796],[281,292,1677342872819],[287,292,1677342872835],[293,292,1677342872851],[296,292,1677342872867],[298,292,1677342872883],[299,292,1677342872915],[302,292,1677342872931],[307,292,1677342872947],[311,294,1677342872964],[311,295,1677342873076],[310,295,1677342873220],[308,295,1677342873236],[303,295,1677342873259],[299,295,1677342873275],[292,295,1677342873291],[286,297,1677342873307],[279,299,1677342873324],[275,299,1677342873340],[265,301,1677342873363],[261,303,1677342873379],[258,306,1677342873395],[253,309,1677342873411],[249,313,1677342873427],[245,318,1677342873443],[242,323,1677342873460],[240,327,1677342873476],[238,332,1677342873492],[238,339,1677342873508],[238,351,1677342873531],[238,359,1677342873547],[236,369,1677342873563],[236,375,1677342873579],[236,383,1677342873595],[236,391,1677342873611],[236,402,1677342873628],[236,410,1677342873644],[237,422,1677342873667],[239,427,1677342873684],[240,430,1677342873700],[242,432,1677342873716],[244,433,1677342873924],[251,435,1677342873940],[259,439,1677342873956],[279,447,1677342873980],[303,457,1677342874004],[318,463,1677342874020],[329,467,1677342874036],[341,472,1677342874052],[354,481,1677342874075],[362,485,1677342874092],[367,490,1677342874108],[375,495,1677342874131],[379,503,1677342874147],[387,510,1677342874163],[393,518,1677342874179],[398,550,1677342874355],[391,551,1677342874372],[385,553,1677342874388],[381,554,1677342874411],[379,554,1677342874427],[378,554,1677342874444]],\"mm-mp\":12.193308550185872,\"md\":[[196,325,1677342872412],[309,293,1677342872956],[242,432,1677342873724],[377,554,1677342874468]],\"md-mp\":685.3333333333334,\"mu\":[[196,325,1677342872491],[311,295,1677342873075],[242,432,1677342873818],[377,554,1677342874587]],\"mu-mp\":698.6666666666666,\"topLevel\":{\"inv\":false,\"st\":1677342868336,\"sc\":{\"availWidth\":1536,\"availHeight\":816,\"width\":1536,\"height\":864,\"colorDepth\":24,\"pixelDepth\":24,\"availLeft\":0,\"availTop\":0,\"onchange\":null,\"isExtended\":false},\"nv\":{\"vendorSub\":\"\",\"productSub\":\"20030107\",\"vendor\":\"Google Inc.\",\"maxTouchPoints\":0,\"scheduling\":{},\"userActivation\":{},\"doNotTrack\":null,\"geolocation\":{},\"connection\":{},\"pdfViewerEnabled\":true,\"webkitTemporaryStorage\":{},\"hardwareConcurrency\":8,\"cookieEnabled\":true,\"appCodeName\":\"Mozilla\",\"appName\":\"Netscape\",\"appVersion\":\"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36\",\"platform\":\"Win32\",\"product\":\"Gecko\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36\",\"language\":\"fr-FR\",\"languages\":[\"fr-FR\"],\"onLine\":true,\"webdriver\":false,\"bluetooth\":{},\"clipboard\":{},\"credentials\":{},\"keyboard\":{},\"managed\":{},\"mediaDevices\":{},\"storage\":{},\"serviceWorker\":{},\"virtualKeyboard\":{},\"wakeLock\":{},\"deviceMemory\":8,\"ink\":{},\"hid\":{},\"locks\":{},\"mediaCapabilities\":{},\"mediaSession\":{},\"permissions\":{},\"presentation\":{},\"serial\":{},\"usb\":{},\"windowControlsOverlay\":{},\"xr\":{},\"userAgentData\":{\"brands\":[{\"brand\":\"Chromium\",\"version\":\"110\"},{\"brand\":\"Not A(Brand\",\"version\":\"24\"},{\"brand\":\"Google Chrome\",\"version\":\"110\"}],\"mobile\":false,\"platform\":\"Windows\"},\"plugins\":[\"internal-pdf-viewer\",\"internal-pdf-viewer\",\"internal-pdf-viewer\",\"internal-pdf-viewer\",\"internal-pdf-viewer\"]},\"dr\":\"\",\"exec\":false,\"wn\":[[1536,714,1.25,1677342868339],[686,714,1.25,1677342868750]],\"wn-mp\":411,\"xy\":[[0,0,1,1677342868339]],\"xy-mp\":0,\"mm\":[[265,92,1677342869621],[226,91,1677342869642],[208,97,1677342869659],[195,105,1677342869675],[185,113,1677342869692],[176,123,1677342869708],[165,138,1677342869732],[158,149,1677342869748],[151,165,1677342869772],[146,177,1677342869795],[145,180,1677342869812],[145,183,1677342869835],[145,185,1677342869851],[145,186,1677342869867],[145,189,1677342869883],[144,193,1677342869899],[142,197,1677342869915],[139,201,1677342869931],[134,209,1677342869955],[129,214,1677342869971],[124,221,1677342869987],[121,225,1677342870003],[119,232,1677342870019],[117,237,1677342870036],[113,247,1677342870060],[108,256,1677342870084],[78,289,1677342871044],[88,285,1677342871152],[490,537,1677342874195],[495,544,1677342874211],[498,549,1677342874227],[500,552,1677342874244],[500,553,1677342874260],[500,554,1677342874308],[496,557,1677342874333]],\"mm-mp\":65.65277777777777},\"v\":1}",
                'n': self.hsw(rere),
                'c': "{\"type\":\"" + "hsl" + "\",\"req\":\"" +getcaptcha["c"]["req"] + "\"}",
    }
            self.client.headers["content-type"] = 'application/json'
            time.sleep(4)
            uuid = self.client.post(f"https://hcaptcha.com/checkcaptcha/{self.site_key}/{key}", json=json_data)
            data = uuid.json()
            
            try:
                key = data["generated_pass_UUID"]
                too = round(end-start, 2)
                print(f"[DEBUG] KEY : {key[:40]} | {too}s")
            except:
                return "No key babe"
        except Exception as ex: 
            print(ex)
            #print("[DEBUG] No Cap Key Here Daddy azulax... im sorry...")
            #print(uuid.json())
ESEX = open("prx.txt", "r").readlines()

def rp():
    return random.choice(ESEX).replace("\n", "")

for i in range(5):
    s = Solver(proxy=rp())
    threading.Thread(target=s.get_captcha).start()