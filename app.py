from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def process_youtube_url():
    # Get the 'url' parameter from the query string
    youtube_url = request.args.get('url')

    if youtube_url:
        try:
            # Construct the command based on the provided URL
            output_file = f"{youtube_url.split('=')[-1]}.json"
            command = f"youtube-comment-downloader --url {youtube_url} --output {output_file}"

            # Run the command using subprocess
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            # Check if the command was successful
            if result.returncode == 0:
                # Read the content of the saved JSON file
                with open(output_file, 'r') as file:
                    json_content = file.read()

                response = {"status": "success", "output": json_content}
            else:
                response = {"status": "error", "output": result.stderr}

        except Exception as e:
            response = {"status": "error", "message": str(e)}

    else:
        response = {"status": "error", "message": "No 'url' parameter provided in the query string."}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
