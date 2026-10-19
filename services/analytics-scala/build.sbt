ThisBuild / scalaVersion := "2.13.14"

lazy val analytics = (project in file("."))
  .settings(
    name := "acme-analytics",
    libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.18" % Test
  )
