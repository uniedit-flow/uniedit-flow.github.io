import os 
from glob import glob
from pathlib import Path 

from moviepy.editor import VideoFileClip


if __name__ == '__main__':
    video_path_list = glob('./*/*.mp4')
    for video_path in video_path_list:
        if 'wan_video_edit' not in video_path:
            continue
        
        clip = VideoFileClip(video_path)
 
        # 选择要转换为GIF的视频部分（例如，前5秒）
        sub_clip = clip.subclip(0, 5)
        
        # 将视频转换为GIF
        sub_clip.write_gif(video_path.replace('.mp4', '.gif'), fps=16)
