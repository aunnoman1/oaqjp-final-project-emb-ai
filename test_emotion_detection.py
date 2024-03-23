from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        result1=emotion_detector("I am glad this happened")
        result2=emotion_detector("I am really mad about this")
        result3=emotion_detector("I feel disgusted just hearing about this")
        result4=emotion_detector("I am so sad about this")
        result5=emotion_detector("I am really afraid that this will happen")
        
        self.assertEqual('joy',result1['dominant_emotion'])
        self.assertEqual('anger',result2['dominant_emotion'])
        self.assertEqual('disgust',result3['dominant_emotion'])
        self.assertEqual('sadness',result4['dominant_emotion'])
        self.assertEqual('fear',result5['dominant_emotion'])

unittest.main()