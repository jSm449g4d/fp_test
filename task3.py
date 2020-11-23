import csv
from statistics import mean

#設問3
#サーバが返すpingの応答時間が長くなる場合、サーバが過負荷状態になっていると考えられる。
#そこで、直近m回の平均応答時間がtミリ秒を超えた場合は、サーバが過負荷状態になっているとみなそう。
#設問2のプログラムを拡張して、各サーバの過負荷状態となっている期間を出力できるようにせよ。mとtはプログラムのパラメータとして与えられるようにすること。

target_file=input("読み込みファイルを入力してください⇒ ")
target_N=int(input("故障判定回数Nを入力してください⇒ "))
target_M=int(input("過負荷判定回数Mを入力してください⇒ "))
target_T=float(input("過負荷判定時間Tを入力してください⇒ "))

with open(target_file) as f:
    records = csv.reader(f)
    records = sorted(records, key=lambda x:(x[1],x[0]))
    
    _ip="";_fail_date="";_over_date="";_N=0;_pngs=[]
    
    for record in records:
        # 別のサーバーのレコードを読み始めたときの初期化処理
        if(record[1]!=_ip):
            if(_over_date!=""):
                print("過負荷サーバー:",_ip,", 過負荷中:",_over_date,"~")
            if(target_N<=_N):
                print("故障サーバー:",_ip,", 故障中:",_fail_date,"~")
            _over_date=""
            _fail_date=""
            _ip=record[1]
            _N=0
            _pngs=[]
        
        # サーバー過負荷
        if(record[2]!="-"):
            _pngs.append(float(record[2]))
        else:
            _pngs.append(float(0.0))
        #　直前ログでサーバー過負荷してない場合
        if(_over_date==""):
            if (target_T<mean(_pngs[-target_M:])):
                _over_date=record[0]
        #　直前ログでサーバー過負荷している場合
        else:
            if ((target_T<mean(_pngs[-target_M:]))==False):
                print("過負荷サーバー:",_ip,", 過負荷期間:",_over_date,"~",record[0])
                _over_date=""
            
        # サーバー落ち
        #　直前ログでサーバー故障してない場合
        if(_fail_date==""):
            if (record[2]=="-"):
                _server_failflag=True
                _fail_date=record[0]
                _N=1
        #　直前ログでサーバー故障している場合
        else:
            if(record[2]=="-"):
                _N+=1
            if(record[2]!="-"):
                if(target_N<=_N):
                    print("故障サーバー:",_ip,", 故障期間:",_fail_date,"~",record[0])
                _fail_date=""
                _N=0
                
                
    #　直前ログでサーバー故障している場合でログ終了した場合,ログ出力する
    if(_over_date!=""):
        print("過負荷サーバー:",_ip,", 過負荷中:",_over_date,"~")
    if(target_N<=_N):
        print("故障サーバー:",_ip,", 故障中",_fail_date,"~")
            
            