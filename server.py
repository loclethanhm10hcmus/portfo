from operator import delitem

from flask import Flask, render_template, url_for, request, redirect
import csv

# Để hiểu hơn về Flask: https://vn.got-it.ai/blog/flask-trong-python-la-gi-ly-do-nen-dung-flask
app = Flask(__name__)  # Flask cho phép tạo một object như là một server đại diện


# rander_template allows us to send the HTML file

# Giống kiểu instructor trong C++, nó sẽ gán biến import_name = __name__ và trả về một Flask Object, object này cho
# phép bạn phát triển các ứng dụng web một cách dễ dàng

# @app.route('/<username>/<int:post_id>')  # flask look at this and say oh, this is something that we can pass
# # into this function
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)

@app.route('/')  # flask look at this and say oh, this is something that we can pass
# into this function
def my_home():
    return render_template('index.html')


# @app.route('/about.html')
# def about_me():
#     return render_template('about.html')
#
#
# @app.route('/works.html')
# def work():
#     return render_template('works.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# => vì sẽ có quá nhiều trang reference được tạo ra, nên ta dùng
# variable rules


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject},{message}')
    # return file


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(email, subject, message)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            # write_to_file(data)
            write_to_csv(data)
            # data: {'email': 'a@gmail.com', 'subject': 'hehe', 'message': 'hoho'}, nhưng tới đây ta để ý rằng,
            # mỗi khi chúng ta tắt server, thì cái thông tin người gửi này lại mất đi, vậy làm nào đó ta phải lưu nó ở
            # một nơi nào đó
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return "something went wrong. Try again!"

# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blogs'


# @app.route('/blog/2020/dogs')
# # Nếu chúng ta sửa lại: @app.route('/blog') thì khi truy cập tới đường dẫn:
# # http://127.0.0.1:5000/blog, nó sẽ lấy cái sau và bỏ qua cái trước
# def blog2():
#     return 'This is my dog'
