import csv

#設問1
#監視ログファイルを読み込み、故障状態のサーバアドレスとそのサーバの故障期間を出力するプログラムを作成せよ。
#出力フォーマットは任意でよい。
#なお、pingがタイムアウトした場合を故障とみなし、最初にタイムアウトしたときから、次にpingの応答が返るまでを故障期間とする。

_date="";_ip="";
        
target_file=input("読み込みファイルを入力してください⇒ ")

with open(target_file) as f:
    records = csv.reader(f)
    records = sorted(records, key=lambda x:(x[1],x[0]))
    
    _date="";_ip="";
    
    for record in records:
        #　直前ログでサーバー故障している場合
        if(_ip!=""):
            if(record[1]!=_ip):
                print("故障サーバー:",_ip,", 故障中")
                _date=""
                _ip=""
            else:
                if(record[2]!="-"):
                    print("故障サーバー:",_ip,", 故障期間:",_date,"~",record[0])
                    _date=""
                    _ip=""
        #　直前ログでサーバー故障してない場合
        else:
            if (record[2]=="-"):
                _date=record[0];_ip=record[1];    
    #　直前ログでサーバー故障している場合でログ終了した場合,ログ出力する
    if(_ip!=""):
        print("故障サーバー:",_ip,", 故障中")
                