// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Cart",
    products: [.library(name: "Cart", targets: ["Cart"])],
    targets: [
        .target(name: "Cart"),
        .testTarget(name: "CartTests", dependencies: ["Cart"]),
    ]
)
