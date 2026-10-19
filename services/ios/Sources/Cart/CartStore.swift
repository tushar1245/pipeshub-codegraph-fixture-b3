import Foundation

public final class CartStore {
    private(set) var cart: Cart
    private let storageKey: String

    public init(storageKey: String = "acme.cart") {
        self.storageKey = storageKey
        self.cart = Cart()
    }

    public func add(sku: String, price: Decimal) {
        cart.add(LineItem(sku: sku, unitPrice: price))
    }

    public func checkoutTotal() -> Decimal {
        cart.total()
    }
}
