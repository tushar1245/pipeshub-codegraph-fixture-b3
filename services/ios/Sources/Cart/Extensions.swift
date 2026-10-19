import Foundation

extension Cart {
    public var isEmpty: Bool {
        items.isEmpty
    }

    public func formattedTotal(locale: Locale = Locale(identifier: "en_US")) -> String {
        let formatter = NumberFormatter()
        formatter.numberStyle = .currency
        formatter.locale = locale
        return formatter.string(from: total() as NSDecimalNumber) ?? "-"
    }
}

extension CartStore {
    public func summary() -> String {
        "\(cart.items.count) items, \(cart.formattedTotal())"
    }
}
