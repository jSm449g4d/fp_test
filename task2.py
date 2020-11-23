import csv

#設問2
#ネットワークの状態によっては、一時的にpingがタイムアウトしても、一定期間するとpingの応答が復活することがあり、
#そのような場合はサーバの故障とみなさないようにしたい。
#N回以上連続してタイムアウトした場合にのみ故障とみなすように、設問1のプログラムを拡張せよ。
#Nはプログラムのパラメータとして与えられるようにすること。

target_file=input("読み込みファイルを入力してください⇒ ")
target_N=int(input("故障判定回数Nを入力してください⇒ "))

with open(target_file) as f:
    records = csv.reader(f)
    records = sorted(records, key=lambda x:(x[1],x[0]))
    
    _ip="";_fail_date="";_N=0;
    
    for record in records:
        # 別のサーバーのレコードを読み始めたときの初期化処理
        if(record[1]!=_ip):
            if(target_N<=_N):
                print("故障サーバー:",_ip,", 故障中:",_fail_date,"~")
            _over_date=""
            _fail_date=""
            _ip=record[1]
            _N=0
            _pngs=[]
            
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
    if(target_N<=_N):
        print("故障サーバー:",_ip,", 故障中",_fail_date,"~")
            
            