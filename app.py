from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def process_youtube_url():
    # Get the 'url' parameter from the query string
    youtube_url = request.args.get('url')

    if youtube_url:
        try:
            # Construct the modified command based on the provided URL
            command = f"youtube-comment-downloader --url {youtube_url} --pretty --output /dev/stdout"
            
            # Run the command using subprocess
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            # Check if the command was successful
            if result.returncode == 0:
                response = {"status": "success", "output": result.stdout}
            else:
                response = {"status": "error", "output": result.stderr}

        except Exception as e:
            response = {"status": "error", "message": str(e)}

    else:
        response = {"status": "error", "message": "No 'url' parameter provided in the query string."}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
