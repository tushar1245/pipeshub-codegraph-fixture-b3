using Acme.Reporting;
using Xunit;

namespace Acme.Reporting.Tests
{
    public class SalesReportTests
    {
        [Fact]
        public void TotalSumsDailyAmounts()
        {
            var report = new SalesReport(new[] { 10m, 20m, 30.5m });
            Assert.Equal(60.5m, report.Total());
        }

        [Fact]
        public void RenderStartsWithTitle()
        {
            IReport report = new SalesReport(new[] { 1m });
            Assert.Equal("Daily sales", report.Render()[0]);
        }
    }
}
