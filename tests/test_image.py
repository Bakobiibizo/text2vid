import unittest
from diffusers.pipelines.pipeline_utils import DiffusionPipeline
from PIL import Image
from ..src.image import generate_image
import torch


class TestImageGeneration(unittest.TestCase):
    custom_prompt = "a purple crystal, shimmering in the light"

    def test_image_generation_with_default_prompt(self):
        # Arrange
        expected_image_size = (
            1024,
            1024,
        )  # Replace with the expected size of the generated image
        # Act
        result = generate_image(self.custom_prompt)
        # Assert
        self.assertIsInstance(result, Image.Image)
        self.assertEqual(result.size, expected_image_size)


if __name__ == "__main__":
    unittest.main()
