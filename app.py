from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template





app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cluster-search')
def cluster_index():
    return render_template('cluster-index.html')


@app.route('/cluster-query', methods=['POST'])
def cluster_query():
    data = request.form  # تلقي البيانات من الطلب
    query = data['query']  # الاستعلام الذي تم إرساله
    dataset = data['dataset']  # مجموعة البيانات التي تم اختيارها
    print("Received Query:", query)
    print("Received Dataset:", dataset)
    # هنا يمكنك معالجة الاستعلام والقيام بأي عمليات أخرى
    with open('ff.txt', 'a') as file:
        file.write(query + '\n')
    print("Query saved to file successfully!")
    # ارجاع رد على العميل
    response = {
        'status': 'success',
        'message': 'Query received successfully',
        'query': query,
        'dataset': dataset
    }
    return jsonify(response)




if __name__ == '__main__':
    app.run(debug=True)