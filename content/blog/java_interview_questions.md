---
title: Java interview questions
date: 2024-07-01
draft: true
summary: |
  A list of questions and answers for a java interview
---

## Java Basic

### Encapsulation types

- `public`
- `private` Only visible inside same class
- `protected` Visible across same package and from subclasses (No matter where subclasses are)
- `package-protected (default)` Visible across same package only

### Why to mark a class as `final`?

According to SOLID, code should be open for extension, however there might some cases where results useful and safe to mark a class as `final`

- If we have security/sensitive logic and want to prevent its update
- If by design users should extend other class instead when adding features, that way the compiler prevents extending from the wrong class.

### When to use `default` in interfaces?

When adding methods to existing interfaces, we can add a 'default' implementation so that classes implementing the interface are not forced to implement the new method.

Prevents existing code gets broken due to interface updates.

### Polymorphism examples in Java Core

The `collections` framework.

- `List` interface -> `ArrayList` and `LinkedList`

## Strings

### StringBuilder



## Testing

### Functional test vs Integration test

**Integration test** is when you verify the interaction between two or more components or your system, for example interaction between two services or between a service and the database.

**Functional test** is when you verify a functionality (Or use case) from an end user perspective. For example

- Check in a reservation
- Create a user
- Post and order