package acme

import org.scalatest.funsuite.AnyFunSuite

class JobSpec extends AnyFunSuite {
  test("parse reads a well-formed line") {
    assert(Job.parse("checkout, u1, 12.5").contains(Event("checkout", "u1", 12.5)))
  }

  test("sum adds event values") {
    val events = Seq(Event("a", "u1", 1.0), Event("b", "u2", 2.0))
    assert(new SumAggregator().aggregate(events) == 3.0)
  }
}
