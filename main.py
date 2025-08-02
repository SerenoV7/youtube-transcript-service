from fastapi import FastAPI
from pydantic import BaseModel
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI(
    title="YouTube Transcript Service",
    description="A service to fetch YouTube video transcripts",
)

ytt_api = YouTubeTranscriptApi()

def getVideoTranscript(video_id: str):
    transcript = ytt_api.fetch(video_id, languages=['en'])
    return " ".join([snippet.text for snippet in transcript.snippets])

class TextResponse(BaseModel):
    text: str

@app.get("/transcript/get/{video_id}", response_model=TextResponse)
def transcriptGet(video_id: str):
    response_text = getVideoTranscript(video_id)
    return TextResponse(text=response_text)