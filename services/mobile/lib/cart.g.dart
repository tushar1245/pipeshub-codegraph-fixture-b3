// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'cart.dart';

CartLine _$CartLineFromJson(Map<String, dynamic> json) => CartLine(
      sku: json['sku'] as String,
      quantity: (json['quantity'] as num).toInt(),
      unitCents: (json['unitCents'] as num).toInt(),
    );

Map<String, dynamic> _$CartLineToJson(CartLine instance) => <String, dynamic>{
      'sku': instance.sku,
      'quantity': instance.quantity,
      'unitCents': instance.unitCents,
    };
