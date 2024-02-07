import torch
from diffusers.schedulers.scheduling_lcm import LCMScheduler
from diffusers.pipelines.auto_pipeline import AutoPipelineForText2Image


def lcm(input_prompt):
    model_id = "Lykon/dreamshaper-7"
    adapter_id = "latent-consistency/lcm-lora-sdv1-5"

    pipe = AutoPipelineForText2Image.from_pretrained(
        model_id, torch_dtype=torch.float16, variant="fp16"
    )
    pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)
    pipe.to("cuda")

    # load and fuse lcm lora
    pipe.load_lora_weights(adapter_id)
    pipe.fuse_lora()

    prompt = input_prompt

    # disable guidance_scale by passing 0
    image = pipe(prompt=prompt, num_inference_steps=4, guidance_scale=0).images[0]

    image.save("generated.png")

    return image
