from fastapi import FastAPI
from pydantic import BaseModel
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

ytt_api = YouTubeTranscriptApi()

class TextResponse(BaseModel):
    text: str

@app.get("/get/{video_id}/transcript/", response_model=TextResponse)
def transcriptGet(video_id: str):
    return TextResponse(text=" ".join([snippet.text for snippet in ytt_api.fetch(video_id, languages=['en'])]))