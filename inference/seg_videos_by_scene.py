from moviepy.editor import VideoFileClip
import os

def seg_one_video(video_path, txt_path, savepath):
    # 读取文本文件
    with open(txt_path, 'r') as f:
        scenes = f.readlines()

    # 创建视频对象
    video = VideoFileClip(video_path)

    # 获取视频的帧率
    fps = video.fps
    print(f"视频的帧率是: {fps}")

    # 遍历场景
    for i, scene in enumerate(scenes):
        # 去除行尾的换行符并按空格分割
        start_id, end_id = map(int, scene.strip().split(' '))
        start_id, end_id = start_id/fps, end_id/fps # 将帧数转换为秒数
        print(f"start_id: {start_id}, end_id: {end_id}")

        # 分割视频
        clip = video.subclip(start_id, end_id)
        vid_name = os.path.basename(video_path)[:-4]
        print(vid_name)
        # 保存为单独的文件
        clip.write_videofile(os.path.join(savepath, f'{vid_name}_{i}.mp4'))

if __name__ == '__main__':

    # 指定视频路径
    video_folder = '/cv_project/datasets/src_mp4/'

    # 指定包含场景起始终止信息的文本文件路径
    txt_folder = '/cv_project/datasets/src_txt/'

    # 指定保存分割后的视频片段的目录
    savepath = '/cv_project/datasets/output'
    if not os.path.exists(savepath):
        os.makedirs(savepath)

    for video_name in os.listdir(video_folder): 
        if video_name.endswith('.mp4'):
            video_path = os.path.join(video_folder, video_name)
            txt_path = os.path.join(txt_folder, video_name+('.scenes.txt'))
            print(f"Processing video: {video_path}")
            print(f"Processing txt: {txt_path}")
            seg_one_video(video_path, txt_path, savepath)

