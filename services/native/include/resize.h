#ifndef ACME_RESIZE_H
#define ACME_RESIZE_H

#include <stddef.h>
#include <stdint.h>

typedef struct {
    int width;
    int height;
    uint8_t *pixels;
} image_t;

int clamp_int(int value, int low, int high);
image_t *image_alloc(int width, int height);
void image_free(image_t *img);
int resize_nearest(const image_t *src, image_t *dst);

#endif
