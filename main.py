import re,json,datetime,requests,os
from multiprocessing import Process
from flask import Flask
from flask import request
import function



app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    main_in = request.json
    try:
        function.main(main_in)
        print("输出成功")
    except:
        print("Errow，main can't run")
    return ''




if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5701,debug=False)
