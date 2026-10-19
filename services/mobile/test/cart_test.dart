import 'package:acme_mobile/cart.dart';
import 'package:test/test.dart';

void main() {
  test('totalCents multiplies quantity by unit price', () {
    final line = CartLine(sku: 'A1', quantity: 3, unitCents: 250);
    expect(line.totalCents, 750);
  });

  test('json round trip keeps the sku', () {
    final line = CartLine(sku: 'B2', quantity: 1, unitCents: 99);
    expect(CartLine.fromJson(line.toJson()).sku, 'B2');
  });
}
