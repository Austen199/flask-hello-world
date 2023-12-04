from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def process_youtube_url():
    # Get the 'url' parameter from the query string
    youtube_url = request.args.get('url')

    if youtube_url:
        try:
            # Construct the command to download comments
            download_command = f"youtube-comment-downloader --url {youtube_url} --pretty --output {youtube_url.split('=')[-1]}.json"
            
            # Run the download command using subprocess
            download_result = subprocess.run(download_command, shell=True, capture_output=True, text=True)

            # Check if the download command was successful
            if download_result.returncode == 0:
                # Construct the command to upload the JSON file using curl
                upload_command = f"curl --upload-file ./{youtube_url.split('=')[-1]}.json https://transfer.sh/{youtube_url.split('=')[-1]}.json"

                # Run the upload command using subprocess
                upload_result = subprocess.run(upload_command, shell=True, capture_output=True, text=True)

                # Check if the upload command was successful
                if upload_result.returncode == 0:
                    response = {"status": "success", "download_output": download_result.stdout, "upload_output": upload_result.stdout}
                else:
                    response = {"status": "error", "message": f"Upload failed: {upload_result.stderr}"}
            else:
                response = {"status": "error", "message": f"Download failed: {download_result.stderr}"}

        except Exception as e:
            response = {"status": "error", "message": str(e)}

    else:
        response = {"status": "error", "message": "No 'url' parameter provided in the query string."}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
