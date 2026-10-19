using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;

namespace Acme.Reporting
{
    public sealed class SalesReport : IReport
    {
        private readonly IReadOnlyList<decimal> _dailyTotals;

        public SalesReport(IEnumerable<decimal> dailyTotals)
        {
            _dailyTotals = dailyTotals?.ToList() ?? throw new ArgumentNullException(nameof(dailyTotals));
        }

        public string Title => "Daily sales";

        public IReadOnlyList<string> Render()
        {
            var lines = new List<string> { Title };
            lines.AddRange(_dailyTotals.Select((total, day) => FormatLine(day + 1, total)));
            lines.Add(FormatLine(0, Total()));
            return lines;
        }

        public decimal Total() => _dailyTotals.Sum();

        private static string FormatLine(int day, decimal amount) =>
            day == 0
                ? $"Total: {amount.ToString("C", CultureInfo.InvariantCulture)}"
                : $"Day {day}: {amount.ToString("C", CultureInfo.InvariantCulture)}";
    }
}
