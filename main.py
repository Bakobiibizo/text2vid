from src.image import generate_image
from src.stable_video_xt import generate_video
from src.transient import transient_tracker
from src.mp4_to_gif import convert_mp4_to_gif
from typing import Optional
import argparse
from uuid import uuid4


def main(
    prompt: Optional[
        str
    ] = "crystal city, space civilization, structures made of crystals, bright saturated colors, award winning illustration, highly detailed, bold linework",
    image_file: Optional[str] = None,
):

    #    tempo = transient_tracker(filename=audio_file)
    fps = 120 // 60 * 4
    if not prompt:
        raise ValueError("No prompt provided")

    filename = str(uuid4())
    image_file = f"data/{filename}.png"
    video_file = f"data/{filename}.mp4"
    gif_file = f"data/{filename}.gif"
    image = generate_image(prompt)

    image.save(image_file)

    generate_video(
        image_path=image_file,
        video_path=video_file,
        fps=fps,
    )
    convert_mp4_to_gif(
        input_video_path=video_file,
        output_gif_path=gif_file,
    )
    return filename


def arg_parse():
    args = argparse.ArgumentParser()
    args.add_argument(
        "--prompt",
        type=str,
        help="prompt for seed image generation",
    )
    args.add_argument(
        "--image_file",
        type=str,
        help="temp path to save generated image",
    )
    args.add_argument(
        "--audio_file",
        type=str,
        help="temp path for reference audio file",
    )
    args.add_argument(
        "--video_file",
        type=str,
        help="temp path to save generated video",
    )
    return args.parse_args()


if __name__ == "__main__":
    prompt_input: Optional[str] = None
    image_path: Optional[str] = None
    audio_path: Optional[str] = None
    video_path: Optional[str] = None
    arguments = arg_parse()
    if arguments.prompt:
        prompt_input = arguments.prompt
    if arguments.image_file:
        image_path = arguments.image_file
    if arguments.audio_file:
        audio_path = arguments.audio_file
    if arguments.video_file:
        video_path = arguments.video_file
    main(prompt=prompt_input)
