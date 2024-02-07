import torch

from diffusers.pipelines.stable_video_diffusion.pipeline_stable_video_diffusion import (
    StableVideoDiffusionPipeline,
)
from diffusers.utils.loading_utils import load_image
from diffusers.utils.export_utils import export_to_video
from typing import Optional, Tuple


def generate_video(
    image_path: Optional[str] = "data/image.png",
    video_path: Optional[str] = "data/video.mp4",
    fps: Optional[int or float] = 8,
    image_size: Optional[Tuple[int, int]] = (1024, 1024),
    seed: Optional[int] = 42,
    chunk_size: Optional[int] = 4,
    motion_bucket: Optional[int] = 120,
    noise_aug_strength: Optional[float] = 0.1,
):
    pipe = StableVideoDiffusionPipeline.from_pretrained(
        "stabilityai/stable-video-diffusion-img2vid-xt",
        torch_dtype=torch.float16,
        variant="fp16",
    )
    pipe.to("cuda")

    # Load the conditioning image
    image = load_image(image_path)
    image = image.resize(image_size)

    generator = torch.manual_seed(seed)
    frames = pipe(
        image,
        decode_chunk_size=chunk_size,  # type: ignore
        generator=generator,
        motion_bucket_id=motion_bucket,  # type: ignore
        noise_aug_strength=noise_aug_strength,  # type: ignore
    ).frames[
        0
    ]  # type: ignore
    export_to_video(frames, video_path, fps=fps or 60)
