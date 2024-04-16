from youtube_transcript_api import YouTubeTranscriptApi

video_id = "v7-YprDdMyw"

results = YouTubeTranscriptApi.get_transcript(video_id)

transcript_text = ""

for i in range(0,len(results)):
    transcript_text = transcript_text + " " + results[i]["text"]

print(transcript_text)
