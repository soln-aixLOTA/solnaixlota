name := "ai-service"
version := "0.1.0"
scalaVersion := "2.12.20"

lazy val root = (project in file("."))
  .settings(
    libraryDependencies ++= Seq(
      "com.typesafe.akka" %% "akka-actor-typed" % "2.8.5",
      "com.typesafe.akka" %% "akka-stream" % "2.8.5",
      "com.typesafe.akka" %% "akka-http" % "10.5.2",
      "ch.qos.logback" % "logback-classic" % "1.4.11"
    ),
    bloopExportJarClassifiers := Some(Set("sources"))
  ) 