from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/export/', methods=['GET'])
def process_youtube_url():
    # Get the 'url' parameter from the query string
    youtube_url = request.args.get('url')

    if youtube_url:
        try:
            # Construct the command to download comments
            download_command = f"youtube-comment-downloader --url {youtube_url} --pretty --output /dev/stdout"
            
            # Run the download command using subprocess
            download_result = subprocess.run(download_command, shell=True, capture_output=True, text=True)

            # Check if the download command was successful
            if download_result.returncode == 0:
                json_content = download_result.stdout
                response = {"status": "success", "json_content": json_content}
            else:
                response = {"status": "error", "message": f"Download failed: {download_result.stderr}"}

        except Exception as e:
            response = {"status": "error", "message": str(e)}

    else:
        response = {"status": "error", "message": "No 'url' parameter provided in the query string."}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
