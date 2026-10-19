package acme

import scala.io.Source

object Job {
  def parse(line: String): Option[Event] =
    line.split(",").map(_.trim) match {
      case Array(name, user, value) => value.toDoubleOption.map(Event(name, user, _))
      case _                        => None
    }

  def load(path: String): Seq[Event] = {
    val source = Source.fromFile(path)
    try source.getLines().flatMap(parse).toSeq
    finally source.close()
  }

  def main(args: Array[String]): Unit = {
    val events = load(args.headOption.getOrElse("events.csv"))
    Metrics.summarizeAll(events).foreach { case (metric, value) => println(f"$metric%-14s $value%.2f") }
  }
}
