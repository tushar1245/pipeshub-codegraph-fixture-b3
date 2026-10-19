import 'dart:convert';

import 'package:http/http.dart' as http;

import 'cart.dart';

class HttpCartSource extends CartSource {
  HttpCartSource(this.baseUrl, {http.Client? client}) : _client = client ?? http.Client();

  final Uri baseUrl;
  final http.Client _client;

  @override
  Future<List<CartLine>> fetch(String userId) async {
    final response = await _client.get(baseUrl.resolve('/carts/$userId'));
    if (response.statusCode != 200) {
      throw StateError('cart fetch failed: ${response.statusCode}');
    }
    final body = jsonDecode(response.body) as List<dynamic>;
    return body.map((row) => CartLine.fromJson(row as Map<String, dynamic>)).toList();
  }
}

class CartRepository {
  CartRepository(this._source);

  final CartSource _source;
  final Map<String, List<CartLine>> _cache = {};

  Future<List<CartLine>> linesFor(String userId) async {
    return _cache[userId] ??= await _source.fetch(userId);
  }

  Future<int> totalCents(String userId) async {
    final lines = await linesFor(userId);
    return lines.fold<int>(0, (sum, line) => sum + line.totalCents);
  }
}
