## 搭建环境

```shell
docker pull nvcr.io/nvidia/pytorch:22.08-py3 
```

从该镜像建立容器后，下载

```shell
pip install tensorflow-gpu==2.7.0
apt-get install ffmpeg
pip install ffmpeg-python 
```

## 下载权重文件

`inference/transnetv2-weights`文件夹中的所有文件需要手动下载。直接`git clone`只能获取指针。

## 推理

```shell
cd inference
```

修改`inference_multi_mp4.py`中的`root_dir`为你的mp4所在文件夹路径，然后运行

```shell
python inference_multi_mp4.py
```

- 在`root_dir`下生成视频名+`.scenes.txt`文件,每一行存储一个片段的起始帧序号和结束帧序号。
- 在`root_dir`下生成视频名+`.predictions.txt`文件,第几行对应第几帧是新片段起始帧的概率。

## 分割视频

修改`seg_videos_by_scene.py`中的参数

```python
    # 指定视频路径
    video_folder = '/cv_project/datasets/src_mp4/'

    # 指定包含场景起始终止信息的文本文件路径
    txt_folder = '/cv_project/datasets/src_txt/'

    # 指定保存分割后的视频片段的目录
    savepath = '/cv_project/datasets/output'
```

运行

```shell
python seg_videos_by_scene.py
```

即可得到按预测的场景片段分割后的视频片段。