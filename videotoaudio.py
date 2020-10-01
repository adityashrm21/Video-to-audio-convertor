import moviepy.editor
video=moviepy.editor.VideoFileClip(r'C:\Users\ADMIN\OneDrive\Desktop\Camilo - Medialuna.mp4')
audio=video.audio
audio.write_audiofile(r'C:\Users\ADMIN\OneDrive\Desktop\Camilo.mp3')