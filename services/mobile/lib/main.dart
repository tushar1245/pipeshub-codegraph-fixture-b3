import 'cart.dart';
import 'cart_repository.dart';

Future<void> main() async {
  final repository = CartRepository(HttpCartSource(Uri.parse('https://api.acme.test')));
  final total = await repository.totalCents('user-1');
  final line = CartLine(sku: 'A1', quantity: 2, unitCents: 450);
  print('cart total: $total cents, sample line: ${line.toJson()}');
}
