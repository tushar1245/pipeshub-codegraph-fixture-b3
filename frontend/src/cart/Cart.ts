export interface CartLine {
  sku: string;
  quantity: number;
  unitPrice: number;
}

export class Cart {
  private lines: CartLine[] = [];

  add(line: CartLine): void {
    const existing = this.lines.find((l) => l.sku === line.sku);
    if (existing) {
      existing.quantity += line.quantity;
    } else {
      this.lines.push({ ...line });
    }
  }

  remove(sku: string): void {
    this.lines = this.lines.filter((l) => l.sku !== sku);
  }

  total(): number {
    return this.lines.reduce((sum, l) => sum + l.quantity * l.unitPrice, 0);
  }

  totalWithTax(rate: number): number {
    return this.total() * (1 + rate);
  }
}
