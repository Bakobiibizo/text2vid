import torch


def check_cuda(device_id=4):
    if torch.cuda.is_available():
        num_devices = torch.cuda.device_count()
        print(f"Number of CUDA devices available: {num_devices}")
        # Now you can set the device ID if it's within the range of available devices
        if device_id < num_devices:
            torch.cuda.set_device(device_id)
            print(f"Set to CUDA device {device_id}")
        else:
            print(f"Invalid device ID {device_id}; using default CUDA device.")
    else:
        print("CUDA is not available. Running on CPU.")


if __name__ == "__main__":
    check_cuda()
