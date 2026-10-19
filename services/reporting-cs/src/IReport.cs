using System.Collections.Generic;

namespace Acme.Reporting
{
    public interface IReport
    {
        string Title { get; }

        IReadOnlyList<string> Render();
    }
}
