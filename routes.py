import jsonify
from app import app

@app.route('/add_tag/<int:video_id>', methods=['POST'])
def add_tag(video_id):
    # Parse request data and add the tag
    return jsonify({'message': 'Tag added successfully'})

@app.route('/add_cluster', methods=['POST'])
def add_cluster():
    # Parse request data and add the cluster
    return jsonify({'message': 'Cluster added successfully'})

@app.route('/video/<int:video_id>/tags', methods=['GET'])
def get_tags_for_video(video_id):
    # Retrieve tags associated with the video
    return jsonify(tags)

@app.route('/cluster/<int:cluster_id>/tags', methods=['GET'])
def get_tags_in_cluster(cluster_id):
    # Retrieve tags within the cluster
    return jsonify(tags)


@app.route('/')
def index():
    return 'Hello, World!'
