import XCTest
@testable import Cart

final class CartTests: XCTestCase {
    func testAddingSameSkuMergesQuantity() {
        var cart = Cart()
        cart.add(LineItem(sku: "A1", unitPrice: 2))
        cart.add(LineItem(sku: "A1", unitPrice: 2, quantity: 2))
        XCTAssertEqual(cart.items.count, 1)
        XCTAssertEqual(cart.total(), 6)
    }

    func testStoreSummary() {
        let store = CartStore()
        store.add(sku: "B2", price: 5)
        XCTAssertEqual(store.checkoutTotal(), 5)
    }
}
