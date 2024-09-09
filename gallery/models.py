from django.db import models


from blurhash import encode
from PIL import Image as PilImage
import numpy as np

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255, blank=True)
    blurhash = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        # Open the uploaded image and generate the blurhash
        if not self.blurhash:
            pil_image = PilImage.open(self.image)
            pil_image = pil_image.convert("RGB")
            width, height = pil_image.size
            pixels = np.array(pil_image)

            # Generate Blurhash with component counts (between 1 and 9)
            self.blurhash = encode(pixels, components_x=4, components_y=3)

        super().save(*args, **kwargs)




