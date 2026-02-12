---
title: "Working with the Neo4J Java Driver"
date: 2024-05-28T22:04:11-05:00
draft: false
summary: |
    A guide about connections management, read/write transactions and type mapping when using the Neo4J Java Driver.
---

## Connections and Sessions

Connections are managed behind the scenes in a pool by the driver. As final user, you should work with `Session`s instead.

```java
// 1 Create a driver instance
AuthToken auth = AuthTokens.basic(
  "<your_username>",
  "<your_password>"
);
Driver driver = GraphDatabase.driver("neo4j://<your_ip>:<port>", auth);
driver.verifyConnectivity();

// ...

// 2. Now use driver to create a session
//.    try...finally will take care of releasing session resources
try (Session session = driver.session()) {
  // Your transaction code goes here
  // ...
}
```

## Transactions

Driver will work the same for clustered or individual database deployments, there are `read` and `write` transactions.

**Read transaction**

```java
// Write your cypher query as String
String findDir = "MATCH (d:Directory {path: $path}) RETURN d";

return session.executeRead(tx -> {
  
  	// Execute query and pass values for named parameters
    var res = tx.run(
      findDir,
      Values.parameters("path", path)
    );

  	// Retrieve single Record result and then get
    // properties as a Map
    if (res.hasNext()) {
        return rowMapper.from(res.single().get("d").asMap());
    }

    return null;
});
```



**Write transaction**

```java
String mergeDir = """
    MERGE (d:Directory { path: $path })
    ON CREATE
        SET
            d.recursive = $recursive,
            d.status = $status
    ON MATCH
        SET
            d.recursive = $recursive,
            d.status = $status;
""";

// Pretty similar to 'read' query, you can pass values for
// named parameters as a map
session.executeWriteWithoutResult(tCtx -> tCtx.run(
  	mergeDir,
    rowMapper.asMap(directory)
));
```

## Neo4J Type System

Even though Neo4j is written in Java, not all Cypher types map directly into a Java type.

| Java Type       | Cypher Type     | Notes                                                        |
| --------------- | --------------- | ------------------------------------------------------------ |
| `null`          | `null`          |                                                              |
| `List`          | `List`, `Array` | Neo4j can only store a flat array containing strings, booleans or numbers. |
| `Map`           | `Map`           |                                                              |
| `Boolean`       | `Boolean`       |                                                              |
| `Long`          | `Integer`       |                                                              |
| `Double`        | `Float`         |                                                              |
| `String`        | `String`        |                                                              |
| `byte[]`        | `byte[]`        |                                                              |
| `LocalDate`     | `LocalDate`     | See [Temporal Types](https://graphacademy.neo4j.com/courses/app-java/2-interacting/3-type-system/#_temporal_types) |
| `Time`          | `Time`          | See [Temporal Types](https://graphacademy.neo4j.com/courses/app-java/2-interacting/3-type-system/#_temporal_types) |
| `LocalTime`     | `LocalTime`     | See [Temporal Types](https://graphacademy.neo4j.com/courses/app-java/2-interacting/3-type-system/#_temporal_types) |
| `DateTime`      | `DateTime`      | See [Temporal Types](https://graphacademy.neo4j.com/courses/app-java/2-interacting/3-type-system/#_temporal_types) |
| `LocalDateTime` | `LocalDateTime` | See [Temporal Types](https://graphacademy.neo4j.com/courses/app-java/2-interacting/3-type-system/#_temporal_types) |
| `IsoDuration`   | `Duration`      |                                                              |
| `Point`         | `Point`         |                                                              |
| `Node`          | `Node`          | See [Nodes & Relationships](https://graphacademy.neo4j.com/courses/app-java/2-interacting/3-type-system/#_nodes_relationships) |
| `Relationship`  | `Relationship`  | See [Nodes & Relationships](https://graphacademy.neo4j.com/courses/app-java/2-interacting/3-type-system/#_nodes_relationships) |
| `Path`          | `Path`          | See [Nodes & Relationships](https://graphacademy.neo4j.com/courses/app-java/2-interacting/3-type-system/#_nodes_relationships) |

Reference: https://neo4j.com/docs/java-manual/current/data-types/