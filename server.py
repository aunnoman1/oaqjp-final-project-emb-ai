"""docstring for server.py"""
from flask import Flask,request,render_template
from EmotionDetection.emotion_detection import emotion_detector



app=Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_func():
    """fucntion docstring"""
    text_to_analyze=request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger=response['anger']
    disgust=response['disgust']
    fear=response['fear']
    joy=response['joy']
    sadness=response['sadness']
    dominant=response['dominant_emotion']
    if dominant is None:
        return "Invalid text! Please try again!."
    return f"""For the given statement, the system response is 'anger': {anger},
     'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and
    'sadness': {sadness}. The dominant emotion is {dominant}.
    """


@app.route("/")
def index_page():
    """function docstring"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
