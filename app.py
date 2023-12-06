<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Export Social Media Comments</title>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
	</head>

<style>
    .loader {
        width: 48px;
        height: 48px;
        border: 5px solid;
        border-color: #FF3D00 transparent;
        border-radius: 50%;
        display: inline-block;
        box-sizing: border-box;
        animation: rotation 1s linear infinite;
    }

    @keyframes rotation {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }
</style>

<body>
    <div class="container shadow-lg p-3 mb-5 bg-body-tertiary rounded">
        <div class="row ">
            <div class="col-12 d-flex justify-content-center align-items-center mt-5 mb-2">
                <h1>Export Social Media Comments</h1>
            </div>
        </div>
        <div class="row shadow-lg p-3 mb-5 bg-body-tertiary rounded">
            <div class="col-sm-11 col p-2">
                <form onsubmit="exportComments(event);">
                    <div class="mb-3">
                      <label for="url" class="form-label">YouTube URL</label>
                      <input type="text" class="form-control" id="url" required="true">
                    </div>
                    <div>
                        <button type="submit" class="btn btn-primary m-2">Export Comments</button>
                    </div>
                </form>
                <div id="response" class="mt-3"></div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <script src="app.js"></script>


<script>
    function exportComments(event) {
        event.preventDefault();
        const urlInput = document.getElementById('url');
        const exportButton = event.target.querySelector('.btn.btn-primary.m-2'); // Reference the button using its class
        const responseDiv = document.getElementById('response');

        // Disable the export button
        exportButton.disabled = true;

        // Show spinner instead of input and button
        responseDiv.innerHTML = `<span class="loader"></span>`;

        const apiUrl = `/export/?url=${encodeURIComponent(urlInput.value)}`;

        // You can use fetch or any other AJAX library to make the request
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    // Show success message
                    responseDiv.innerHTML = `<p>Your comments are ready to download:</p>`;

                    // Show download button below the input and button
                    const downloadButton = document.createElement('a');
                    downloadButton.href = data.upload_output;
                    downloadButton.target = '_blank';
                    downloadButton.className = 'btn btn-success m-2';
                    downloadButton.textContent = 'Download Comments';
                    responseDiv.appendChild(downloadButton);

                    // Show export new video comments button
                    const exportNewButton = document.createElement('button');
                    exportNewButton.className = 'btn btn-primary m-2';
                    exportNewButton.textContent = 'Export New Video Comments';
                    exportNewButton.addEventListener('click', () => {
                        // Reload the page to show the initial input and button
                        window.location.reload();
                    });
                    responseDiv.appendChild(exportNewButton);

                    // Hide the input and original export button
                    urlInput.style.display = 'none';
                    exportButton.style.display = 'none';
                } else {
                    // Show error message
                    responseDiv.innerHTML = `<p>Error fetching comments. Please try again.</p>`;
                }
            })
            .catch(error => {
                console.error('Error fetching comments:', error);
                responseDiv.innerHTML = `<p>Error fetching comments. Please try again.</p>`;
            })
            .finally(() => {
                // Re-enable the export button
                exportButton.disabled = false;
            });
    }
</script>



</body>
</html>
