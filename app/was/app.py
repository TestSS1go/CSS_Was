from flask import Flask, jsonify, request, render_template, send_from_directory
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#Aura DB 연결 정보
#향후 추가
db_config = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'Test11!!',
    'db' : 'tet',
    'charset': 'utf8mb4'
}
#데이터베이스 정보 가져오기
def get_data():
    try:
        connection = pymysql.connect(**db_config)

        with connection.cursor() as cursor:
            sql = "select * from cloud where vod_name = '파묘' and vod_num = 1"
            cursor.execute(sql)
            result = cursor.fetchall()

            data = []
            #전송할 데이터 객체, 향후 추가
            data.append({
                'vod_url_s3': result[0][1]
            })
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})
