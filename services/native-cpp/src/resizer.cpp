#include "img/resizer.hpp"

#include <algorithm>

namespace img {

Resizer::Resizer(Size target) : target_(target) {}

std::vector<std::uint8_t> Resizer::run(const std::vector<std::uint8_t>& pixels, Size source) const {
    std::vector<std::uint8_t> out(static_cast<std::size_t>(target_.width) * target_.height);
    for (int y = 0; y < target_.height; ++y) {
        for (int x = 0; x < target_.width; ++x) {
            out[static_cast<std::size_t>(y) * target_.width + x] = pixels[sourceIndex(x, y, source)];
        }
    }
    return out;
}

int Resizer::sourceIndex(int x, int y, Size source) const {
    int sx = std::min(x * source.width / target_.width, source.width - 1);
    int sy = std::min(y * source.height / target_.height, source.height - 1);
    return sy * source.width + sx;
}

}  // namespace img
