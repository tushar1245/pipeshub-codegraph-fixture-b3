#include <cassert>
#include <vector>

#include "img/resizer.hpp"

static void downscalesToTarget() {
    img::Resizer resizer({1, 1});
    std::vector<std::uint8_t> pixels{9, 9, 9, 9};
    auto out = resizer.run(pixels, {2, 2});
    assert(out.size() == 1);
    assert(out[0] == 9);
}

int main() {
    downscalesToTarget();
    return 0;
}
