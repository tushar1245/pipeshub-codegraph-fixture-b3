import Foundation

public protocol CartPricing {
    func total() -> Decimal
}

public struct LineItem: Equatable {
    public let sku: String
    public let unitPrice: Decimal
    public var quantity: Int

    public init(sku: String, unitPrice: Decimal, quantity: Int = 1) {
        self.sku = sku
        self.unitPrice = unitPrice
        self.quantity = quantity
    }

    public func subtotal() -> Decimal {
        unitPrice * Decimal(quantity)
    }
}

public struct Cart: CartPricing {
    public private(set) var items: [LineItem] = []

    public init() {}

    public mutating func add(_ item: LineItem) {
        if let index = items.firstIndex(where: { $0.sku == item.sku }) {
            items[index].quantity += item.quantity
        } else {
            items.append(item)
        }
    }

    public func total() -> Decimal {
        items.reduce(Decimal(0)) { $0 + $1.subtotal() }
    }
}
