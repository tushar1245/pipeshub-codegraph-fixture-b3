import 'package:json_annotation/json_annotation.dart';

part 'cart.g.dart';

@JsonSerializable()
class CartLine {
  CartLine({required this.sku, required this.quantity, required this.unitCents});

  factory CartLine.fromJson(Map<String, dynamic> json) => _$CartLineFromJson(json);

  final String sku;
  final int quantity;
  final int unitCents;

  int get totalCents => quantity * unitCents;

  Map<String, dynamic> toJson() => _$CartLineToJson(this);
}

abstract class CartSource {
  Future<List<CartLine>> fetch(String userId);
}
