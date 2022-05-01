from models import *

def json_response(data, message, code):
    if data and message:
        result = {'data': data, 'message': message}
    elif data and not message:
        result = {'data': data}
    else:
        result = {'message': message}
    
    return make_response(jsonify(result), code)


@app.route('/api/uploads/<filename>', methods=['GET'])
def index(filename):
    return send_from_directory('uploads', filename)


@app.route('/api/articles', methods=['GET'])
def get_articles():
    return json_response(Article.get_all_article(), None, 200)

@app.route('/api/articles/<int:id>', methods=['GET'])
def get_detail_article(id):
    try:
        return json_response(Article.get_article(id), None, 200)
    except:
        return json_response(None, 'Maaf artikel dengan id ' + str(id) + ' tidak ditemukan', 400)


@app.route('/api/articles/<int:id>', methods=['DELETE'])
def delete_article(id):
    try:
        Article.get_article(id)
        Article.delete_article(id)

        return json_response(None, 'Artikel berhasil di hapus', 200)
    except:
        return json_response(None, 'Maaf artikel dengan id ' + str(id) + ' tidak ditemukan', 400)


@app.route('/api/articles', methods=['POST'])
def add_article():
    request_data = request.form

    try:
        thumbnail = upload_image(request.files['thumbnail'])
    except KeyError as e:
        thumbnail = None

    Article.add_article(
        request_data['title'], 
        request_data['description'], 
        request_data['author'], 
        request_data['content'], 
        thumbnail
    )

    return json_response(None, 'Artikel berhasil dibuat', 201)

@app.route('/api/articles/<int:id>', methods=['PUT'])
def update_article(id):
    request_data = request.form

    try:
        Article.get_article(id)
    except:
        return json_response(None, 'Maaf artikel dengan id ' + str(id) + ' tidak ditemukan', 400)

    try:
        thumbnail = upload_image(request.files['thumbnail'])
    except KeyError as e:
        thumbnail = None

    Article.update_article(
        id, 
        request_data['title'], 
        request_data['description'], 
        request_data['author'], 
        request_data['content'], 
        thumbnail
    )

    return json_response(None, 'Artikel berhasil diedit', 200)


if __name__ == '__main__':
    app.run(debug=True)