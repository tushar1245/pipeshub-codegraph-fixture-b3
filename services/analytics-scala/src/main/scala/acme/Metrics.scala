package acme

final case class Event(name: String, userId: String, value: Double)

trait Aggregator {
  def metricName(): String
  def aggregate(events: Seq[Event]): Double
}

class SumAggregator extends Aggregator {
  override def metricName(): String = "sum"
  override def aggregate(events: Seq[Event]): Double = events.map(_.value).sum
}

class UniqueUsers extends Aggregator {
  override def metricName(): String = "unique_users"
  override def aggregate(events: Seq[Event]): Double = events.map(_.userId).distinct.size.toDouble
}

object Metrics {
  def defaults: Seq[Aggregator] = Seq(new SumAggregator, new UniqueUsers)

  def summarize(events: Seq[Event], aggregators: Seq[Aggregator]): Map[String, Double] =
    aggregators.map(a => a.metricName() -> a.aggregate(events)).toMap

  def summarizeAll(events: Seq[Event]): Map[String, Double] = summarize(events, defaults)
}
