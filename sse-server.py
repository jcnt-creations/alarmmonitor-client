from flask import Flask, Response
import time

app = Flask(__name__)

# SSE route that streams data to the client
@app.route('/stream')
def stream():
    def event_stream():
        while True:
            # Here, we are simulating data being streamed every second
            time.sleep(1)
            yield f"data: Server time is {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    return Response(event_stream(), content_type='text/html')

# Root route to load the client HTML
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
      <head>
        <title>SSE Test</title>
      </head>
      <body>
        <h1>Server-Sent Events Demo</h1>
        <div id="events"></div>

        <script>
          // Initialize the EventSource connection
          var eventSource = new EventSource('/stream');

          eventSource.onmessage = function(event) {
            document.getElementById('events').innerHTML += event.data + '<br>';
          };

          eventSource.onerror = function(err) {
            console.error("EventSource failed:", err);
          };
        </script>
      </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=False, threaded=True)
    print("Main server started")
