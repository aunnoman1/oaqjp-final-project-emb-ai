import requests,json
def emotion_detector(text_to_analyse):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url , json = myobj , headers=headers )
    if response.status_code==400:
        anger=fear=disgust=sadness=joy=dominant=None
        dict={'anger':anger,'disgust':disgust,'fear':fear,'joy':joy,'sadness':sadness , 'dominant_emotion' : dominant}
    else:
        formatted_response=json.loads(response.text)
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        dict={'anger':anger,'disgust':disgust,'fear':fear,'joy':joy,'sadness':sadness}
        dominant = max(zip(dict.values(), dict.keys()))[1]
        dict['dominant_emotion']=dominant
    return dict