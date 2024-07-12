import os
from flask import Flask
import pandas as pd

app = Flask(__name__, static_folder = '.')

@app.route('/')
def home():
    string_return = '<h1> Chủ đề: Du lịch - Địa điểm: Thành phố Hồ Chí Minh </h1>'

    string_return += '''<a href= 'https://drive.google.com/drive/folders/19ZNeKPKeb_W8iiffqZqIC5YU6IgdZNYR?fbclid=IwAR34tTaRgkm6mCvJv9uyoRsHG7J3l8XVb4T3BE_KeHTUOuh4f_CocvmLyzA'> LINK DRIVE CỦA NHÓM (CÓ GỬI KÈM TRONG EMAIL NỘP DỰ ÁN) </a><br>'''
    
    string_return += '<h2> Thành viên: </h2>'
    string_return += '<ul><li> 19110183 - Hồ Diệp Thanh Thảo </li>'
    string_return += '<li> 19110281 - Phùng Thị Điệp </li>'
    string_return += '<li> 19110488 - Huỳnh Khoang Trí </li>'
    string_return += '<li> 19110508 - Nguyễn Thị Hà Uyên </li></ul>'
    
    string_return += '<h2> Dữ liệu crawl được:  </h2>'
    string_return += '<h3> Địa điểm tham quan: </h3>'
    string_return += '''<a href= 'http://127.0.0.1:5000/vinpearl_attraction'> vinpearl_attraction </a><br>'''
    string_return += '''<a href= 'http://127.0.0.1:5000/divui'> divui </a>'''
    string_return += '<h3> Địa điểm ăn uống: </h3>'
    string_return += '''<a href= 'http://127.0.0.1:5000/toplist'> toplist </a><br>'''
    string_return += '''<a href= 'http://127.0.0.1:5000/vinpearl_cafe'> vinpearl_cafe </a>'''
    string_return += '<h3> Địa điểm tổ chức sự kiện: </h3>'
    string_return += '''<a href= 'http://127.0.0.1:5000/dulichtoday'> dulichtoday </a><br>'''
    
    return string_return

@app.route('/vinpearl_attraction')
def vinpearl_attraction():
    df = pd.read_csv('Data/vinpearl_attraction/CrawlData_vinpearl_attraction.csv')

    string_return = '''<a href= 'http://127.0.0.1:5000/'> Trang đầu </a><br><br>'''
    string_return += '''<a href= 'http://127.0.0.1:5000/vinpearl_attraction/statistics'> Một số thống kê </a><br><br>'''
    string_return += 'Dữ liệu có được bởi 19110488 - Huỳnh Khoang Trí <br><br>'
    string_return += '''Nguồn: <a href= 'https://vinpearl.com/vi/23-dia-diem-du-lich-sai-gon-nghe-la-muon-xach-balo-len-va-di'> 23 địa điểm tham quan ở Sài Gòn </a><br>'''
    for itr in range(1,len(df)):
        string_return += '<h1> Điểm đến: ' + df.iloc[itr]['Place'] + '</h1>'
        string_return += 'Địa chỉ: ' + df.iloc[itr]['Address'] + '<br>'
        string_return += 'Thời gian: ' + df.iloc[itr]['Time'] + '<br>'
        string_return += 'Phí vào cổng: ' + df.iloc[itr]['Entrance Price'] + '<br>'
        string_return += 'Ảnh minh họa: ' + df.iloc[itr]['Image Source'] + '<br>'
        string_return += 'Mô tả: ' + df.iloc[itr]['Description'] + '<br>'
        string_return += '<br>'

    
    return string_return

@app.route('/vinpearl_attraction/statistics')
def vinpearl_attraction_statistics():
    string_return = '''<a href= 'http://127.0.0.1:5000/'> Trang đầu </a><br><br>'''
    string_return += '''<a href= 'http://127.0.0.1:5000/vinpearl_attraction'> Quay lại trang dữ liệu </a><br><br>'''
    string_return += 'Dữ liệu có được bởi 19110183 - Hồ Diệp Thanh Thảo <br>'
    string_return += 'Dữ liệu có được bởi 19110281 - Phùng Thị Điệp <br>'
    string_return += '<h2> Thống kê theo quận: (Thảo) </h2>'
    string_return += '<img src="https://images2.imgbox.com/ab/78/SZFAkST2_o.jpg" /><br>'
    string_return += '<img src="https://images2.imgbox.com/10/f5/iTj81dXm_o.jpg" /><br>'
    string_return += '<h2> Thống kê theo có phí và không phí: (Thảo) </h2>'
    string_return += '<img src="https://images2.imgbox.com/3f/5a/janLz3AF_o.jpg" /><br>'
    string_return += '<h2> Biểu đồ phí: (Diệp) </h2>'
    string_return += '<img src="https://images2.imgbox.com/1a/b2/708uy7uD_o.jpg" /><br>'
    string_return += '<img src="https://images2.imgbox.com/49/fb/fwEGmq9X_o.jpg" /><br>'
    string_return += '<img src="https://images2.imgbox.com/6c/3f/4BWQEXRD_o.jpg" /><br>'

    return string_return
    
@app.route('/divui')
def divui():
    df = pd.read_csv('Data/divui/CrawlData_divui.csv')

    string_return = '''<a href= 'http://127.0.0.1:5000/'> Trang đầu </a><br><br>'''
    string_return += '''<a href= 'http://127.0.0.1:5000/divui/statistics'> Một số thống kê </a><br><br>'''
    string_return += 'Dữ liệu có được bởi 19110488 - Huỳnh Khoang Trí <br>'
    string_return += '''Nguồn: <a href= 'http://divui.com/blog/72-dia-diem-du-lich-sai-gon-moi-ve-dem-mien-phi-tong-hop-tu-a-z/'> 72 địa điểm tham quan ở Sài Gòn </a><br>'''
    for itr in range(1,len(df)):
        string_return += '<h1> Điểm đến: ' + df.iloc[itr]['Place'] + '</h1>'
        string_return += 'Địa chỉ: ' + df.iloc[itr]['Address'] + '<br>'
        string_return += 'Phân loại: ' + df.iloc[itr]['Type'] + '<br>'
        string_return += 'Phí vào cổng: ' + df.iloc[itr]['Ticket Price'] + '<br>'
        string_return += 'Ảnh minh họa: ' + df.iloc[itr]['Image Source'] + '<br>'
        string_return += 'Mô tả: ' + df.iloc[itr]['Description'] + '<br>'
        string_return += '<br>'
        
    return string_return

@app.route('/divui/statistics')
def divui_statistics():
    string_return = '''<a href= 'http://127.0.0.1:5000/'> Trang đầu </a><br><br>'''
    string_return += '''<a href= 'http://127.0.0.1:5000/divui'> Quay lại trang dữ liệu </a><br><br>'''
    string_return += 'Dữ liệu có được bởi 19110183 - Hồ Diệp Thanh Thảo <br>'
    string_return += '<h2> Thống kê theo quận: </h2>'
    string_return += '<img src="https://images2.imgbox.com/9d/2a/6m442tha_o.jpg" /><br>'
    string_return += '<img src="https://images2.imgbox.com/59/42/kVED5pCq_o.jpg" /><br>'
    string_return += '<img src="https://images2.imgbox.com/42/79/Pen0xvpA_o.jpg" /><br>'
    string_return += '<h2> Thống kê theo có phí và không phí: </h2>'
    string_return += '<img src="https://images2.imgbox.com/1a/a3/FMJUmIqC_o.jpg" /><br>'
    string_return += '<h2> Thống kê theo loại: </h2>'
    string_return += '<img src="https://images2.imgbox.com/84/87/6ZCGdxXz_o.jpg" /><br>'
    string_return += '<img src="https://images2.imgbox.com/f3/1d/neFeE8JB_o.jpg" /><br>'

    return string_return

@app.route('/toplist')
def toplist():
    df = pd.read_csv('Data/toplist/CrawlData_toplist.csv')

    string_return = '''<a href= 'http://127.0.0.1:5000/'> Trang đầu </a><br><br>'''
    string_return += '''<a href= 'http://127.0.0.1:5000/toplist/statistics'> Một số thống kê </a><br><br>'''
    string_return += 'Dữ liệu có được bởi 19110488 - Huỳnh Khoang Trí <br><br>'
    string_return += '''Nguồn: <a href= 'https://toplist.vn/top-list/quan-an-uong-tren-cao-view-dep-nhat-sai-gon-12068.htm'> Một vài địa điểm ăn uống view đẹp </a><br>'''
    for itr in range(1,len(df)):
        string_return += '<h1> Điểm đến: ' + df.iloc[itr]['Place'] + '</h1>'
        string_return += 'Địa chỉ: ' + df.iloc[itr]['Address'] + '<br>'
        string_return += 'Hotline: ' + df.iloc[itr]['Hotline'] + '<br>'
        string_return += 'Fanpage: ' + df.iloc[itr]['Fanpage'] + '<br>'
        string_return += 'Website: ' + df.iloc[itr]['Website'] + '<br>'
        string_return += 'Thời gian: ' + df.iloc[itr]['Time'] + '<br>'
        string_return += 'Giá tiền: ' + df.iloc[itr]['Price'] + '<br>'
        string_return += 'Ảnh minh họa: ' + df.iloc[itr]['Image Source'] + '<br>'
        string_return += 'Mô tả: ' + df.iloc[itr]['Description'] + '<br>'
        string_return += '<br>'
        
    return string_return

@app.route('/toplist/statistics')
def toplist_statistics():
    string_return = '''<a href= 'http://127.0.0.1:5000/'> Trang đầu </a><br><br>'''
    string_return += '''<a href= 'http://127.0.0.1:5000/toplist'> Quay lại trang dữ liệu </a><br><br>'''
    string_return += 'Dữ liệu có được bởi 19110281 - Phùng Thị Điệp <br>'
    string_return += '<h2> Thống kê theo giá tiền: </h2>'
    string_return += '<img src="https://images2.imgbox.com/10/04/v7810Adg_o.jpg" /><br>'
    string_return += '<img src="https://images2.imgbox.com/d2/f1/Q2RFIK59_o.jpg" /><br>'
    string_return += '<h2> Biểu đồ giá tiền: </h2>'
    string_return += '<img src="https://images2.imgbox.com/16/46/kL1jXj0J_o.jpg" /><br>'

    return string_return

@app.route('/vinpearl_cafe')
def vinpearl_cafe():
    df = pd.read_csv('Data/vinpearl_cafe/CrawlData_vinpearl_cafe.csv')

    string_return = '''<a href= 'http://127.0.0.1:5000/'> Trang đầu </a><br><br>'''
    string_return += '''<a href= 'http://127.0.0.1:5000/vinpearl_cafe/statistics'> Một số thống kê </a><br><br>'''
    string_return += 'Dữ liệu có được bởi 19110488 - Huỳnh Khoang Trí <br><br>'
    string_return += '''Nguồn: <a href= 'https://vinpearl.com/vi/top-20-quan-cafe-dep-o-sai-gon-nen-ghe-du-chi-mot-lan'> 20 quán cafe đẹp ở Sài Gòn </a><br>'''
    for itr in range(1,len(df)):
        string_return += '<h1> Điểm đến: ' + df.iloc[itr]['Place'] + '</h1>'
        string_return += 'Địa chỉ: ' + df.iloc[itr]['Address'] + '<br>'
        string_return += 'Thời gian: ' + df.iloc[itr]['Time'] + '<br>'
        string_return += 'Ảnh minh họa: ' + df.iloc[itr]['Image Source'] + '<br>'
        string_return += 'Mô tả: ' + df.iloc[itr]['Description'] + '<br>'
        string_return += '<br>'
        
    return string_return

@app.route('/vinpearl_cafe/statistics')
def vinpearl_cafe_statistics():
    string_return = '''<a href= 'http://127.0.0.1:5000/'> Trang đầu </a><br><br>'''
    string_return += '''<a href= 'http://127.0.0.1:5000/vinpearl_cafe'> Quay lại trang dữ liệu </a><br><br>'''
    string_return += 'Dữ liệu có được bởi 19110183 - Hồ Diệp Thanh Thảo <br>'
    string_return += 'Dữ liệu có được bởi 19110281 - Phùng Thị Điệp <br>'
    string_return += '<h2> Thống kê theo quận: (Thảo) </h2>'
    string_return += '<img src="https://images2.imgbox.com/e6/59/oajYJ3at_o.jpg" /><br>'
    string_return += '<img src="https://images2.imgbox.com/63/64/OFPxp4my_o.jpg" /><br>'
    string_return += '<h2> Thống kê theo khung giờ: (Diệp) </h2>'
    string_return += '<img src="https://images2.imgbox.com/2f/0f/epIMPR2E_o.jpg" /><br>'

    return string_return

@app.route('/dulichtoday')
def dulichtoday():
    df = pd.read_csv('Data/dulichtoday/CrawlData_dulichtoday.csv')

    string_return = '''<a href= 'http://127.0.0.1:5000/'> Trang đầu </a><br><br>'''
    string_return += '''<a href= 'http://127.0.0.1:5000/dulichtoday/statistics'> Một số thống kê </a><br><br>'''
    string_return += 'Dữ liệu có được bởi 19110488 - Huỳnh Khoang Trí <br><br>'
    string_return += '''Nguồn: <a href= 'https://dulichtoday.vn/kham-pha-sai-gon/dia-diem-sai-gon/dia-diem-to-chuc-su-kien-sai-gon.html'> 14 địa điểm tổ chức sự kiện ở Sài Gòn </a><br>'''
    for itr in range(1,len(df)):
        string_return += '<h1> Điểm đến: ' + df.iloc[itr]['Place'] + '</h1>'
        string_return += 'Địa chỉ: ' + df.iloc[itr]['Address'] + '<br>'
        string_return += 'Giá thuê: ' + df.iloc[itr]['Price'] + '<br>'
        string_return += 'Sức chứa: ' + df.iloc[itr]['Size'] + '<br>'
        string_return += 'Website: ' + df.iloc[itr]['Website'] + '<br>'
        string_return += 'Điểm nổi bật: ' + df.iloc[itr]['Pros'] + '<br>'
        string_return += 'Điểm lưu ý: ' + df.iloc[itr]['Cons'] + '<br>'
        string_return += 'Ảnh minh họa: ' + df.iloc[itr]['Image Source'] + '<br>'
        string_return += 'Mô tả: ' + df.iloc[itr]['Description'] + '<br>'
        string_return += '<br>'
        
    return string_return

@app.route('/dulichtoday/statistics')
def dulichtoday_statistics():
    string_return = '''<a href= 'http://127.0.0.1:5000/'> Trang đầu </a><br><br>'''
    string_return += '''<a href= 'http://127.0.0.1:5000/dulichtoday'> Quay lại trang dữ liệu </a><br><br>'''
    string_return += 'Dữ liệu có được bởi 19110183 - Hồ Diệp Thanh Thảo <br>'
    string_return += 'Dữ liệu có được bởi 19110281 - Phùng Thị Điệp <br>'
    string_return += '<h2> Thống kê theo quận: (Thảo) </h2>'
    string_return += '<img src="https://images2.imgbox.com/c6/7f/TlDBhdUK_o.jpg" /><br>'
    string_return += '<img src="https://images2.imgbox.com/d6/43/8wPwv6QM_o.jpg" /><br>'
    string_return += '<h2> Thống kê theo sức chứa: (Thảo) </h2>'
    string_return += '<img src="https://images2.imgbox.com/59/ac/pK1cHMnu_o.jpg" /><br>'
    string_return += '<h2> Biểu đồ sức chứa: (Diệp) </h2>'
    string_return += '<img src="https://images2.imgbox.com/15/98/pQl5Z5i1_o.jpg" /><br>'
    string_return += '<img src="https://images2.imgbox.com/6b/74/9qT7t0LG_o.jpg" /><br>'
    string_return += '<img src="https://images2.imgbox.com/5c/e5/RYLF2sCu_o.jpg" /><br>'
    string_return += '<img src="https://images2.imgbox.com/5f/79/Hnv6uwkv_o.jpg" /><br>'
    string_return += '<h2> Biểu đồ giá tiền: (Diệp) </h2>'
    string_return += '<img src="https://images2.imgbox.com/5b/2d/rH87zvKB_o.jpg" /><br>'
    string_return += '<img src="https://images2.imgbox.com/7b/f1/yOdJhz09_o.jpg" /><br>'
    string_return += '<img src="https://images2.imgbox.com/45/ed/KXtgP2im_o.jpg" /><br>'
    string_return += '<img src="https://images2.imgbox.com/72/66/fpyUufkl_o.jpg" /><br>'

    return string_return
    
#app.run(port=8888, debug=True)
