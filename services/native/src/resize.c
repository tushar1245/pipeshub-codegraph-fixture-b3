#include <stdlib.h>

#include "resize.h"

image_t *image_alloc(int width, int height) {
    image_t *img = malloc(sizeof(image_t));
    if (img == NULL) {
        return NULL;
    }
    img->width = width;
    img->height = height;
    img->pixels = calloc((size_t)width * (size_t)height, 1);
    if (img->pixels == NULL) {
        free(img);
        return NULL;
    }
    return img;
}

void image_free(image_t *img) {
    if (img != NULL) {
        free(img->pixels);
        free(img);
    }
}

int resize_nearest(const image_t *src, image_t *dst) {
    if (src == NULL || dst == NULL || src->width == 0 || src->height == 0) {
        return -1;
    }
    for (int y = 0; y < dst->height; y++) {
        int sy = clamp_int(y * src->height / dst->height, 0, src->height - 1);
        for (int x = 0; x < dst->width; x++) {
            int sx = clamp_int(x * src->width / dst->width, 0, src->width - 1);
            dst->pixels[y * dst->width + x] = src->pixels[sy * src->width + sx];
        }
    }
    return 0;
}
