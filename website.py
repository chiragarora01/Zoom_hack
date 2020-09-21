from flask import Flask, render_template, session, url_for, request
import csv
import pandas as pd
import os

app = Flask(__name__)


@app.route('/')
def hello_world1():
    os.system("zoom2.py")
    return render_template('index.html')


@app.route('/<string:page_name>')
def hello_world(page_name):
    return render_template(page_name)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
    return render_template('submit.html')


def read():
    df = pd.read_csv('Book3.csv')
    return df.to_html()


def write_to_csv(data):
    with open('Book3.csv', mode='a', newline='') as database:
        Time = data['Time']
        day = data['day']
        url = data['url']
        csv_writer = csv.writer(database, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([Time, day, url])

    # csv_writer.writeheader()
    # csv_writer.writerow({Time: Time, day: day, url: url})
    # def del_to_file():
    #     col_to_remove = [1, 3, 4]  # index of col start with zero
    #     col_to_remove = sorted(col_to_remove, reverse=True)
    #     row_count = 0
    #     with open('Book2.csv', 'r') as source:
    #         reader = csv.writer(source)
    #         with open('Book2.csv', 'w', newline='') as result:
    #             writer = csv.writer(result)
    #             for row in reader:
    #                 row_count += 1
    #                 print('\r{0}'.format(row_count), end='')  # Print rows processed
    #                 for col_index in col_to_remove:
    #                     del row[col_index]
    #                 writer.writerow(row)


# @app.route('/delete', methods=['POST', 'GET'])
# def dele():
#     if request.method == 'POST':
#         data1 = request.form.to_dict()
#         memberName = data1['memberName']
#         imp = open('Book3.csv', 'rb')
#         out = open('Book3.csv', 'wb')
#         writer = csv.writer(out)
#         for row in csv.reader(imp):
#             print(row)
#             if row == memberName:
#                 writer.writerow(row)
#         imp.close()
#         out.close()
#         # return df1.to_html()
#     return render_template('delete.html')

#
@app.route('/read')
def read():
    df = pd.read_csv('Book3.csv')
    return df.to_html()


if __name__ == "__main__":
    app.run(debug=True)
