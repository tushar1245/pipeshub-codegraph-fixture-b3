#include <cstdio>
#include <vector>

#include "img/resizer.hpp"

int main() {
    img::Resizer resizer({2, 2});
    std::vector<std::uint8_t> pixels{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
    auto out = resizer.run(pixels, {4, 4});
    std::printf("%zu pixels, target %dx%d\n", out.size(), resizer.target().width, resizer.target().height);
    return 0;
}
