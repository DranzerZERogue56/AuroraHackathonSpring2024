from youtube_transcript_api import YouTubeTranscriptApi

video_id = "v7-YprDdMyw"

results = YouTubeTranscriptApi.get_transcript(video_id)

print(results)
