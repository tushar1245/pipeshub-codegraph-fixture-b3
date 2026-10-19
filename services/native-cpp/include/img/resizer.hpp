#pragma once

#include <cstdint>
#include <vector>

namespace img {

struct Size {
    int width;
    int height;
};

class Resizer {
public:
    explicit Resizer(Size target);
    std::vector<std::uint8_t> run(const std::vector<std::uint8_t>& pixels, Size source) const;
    Size target() const { return target_; }

private:
    int sourceIndex(int x, int y, Size source) const;
    Size target_;
};

}  // namespace img
