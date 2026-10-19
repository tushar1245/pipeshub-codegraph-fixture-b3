using System;
using System.Collections.Generic;

namespace Acme.Reporting
{
    public static class ReportRunner
    {
        public static int Print(IReport report)
        {
            var lines = report.Render();
            foreach (var line in lines)
            {
                Console.WriteLine(line);
            }
            return lines.Count;
        }

        public static void Main(string[] args)
        {
            var report = new SalesReport(new List<decimal> { 120.5m, 98.25m, 143m });
            Print(report);
        }
    }
}
