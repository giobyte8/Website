---
title: "Docker multi-platform images"
date: 2023-11-18T12:27:00-06:00
draft: false
summary: |
    Guide to use `docker buildx` command to build multi-architecture docker
    images that can run on multiple CPU architectures

# Custom added attribute
real_date: 2024-03-22T12:27:00-06:00
---

While building docker images very often we need to deploy it into a different
CPU architecture than the one used to build the image.

For example you might be building in a Linux `amd64` server but you'll deploy
into an IoT `arm64` CPU (e.g. A RaspberryPi).

For such scenarios docker includes the `buildx` command, which takes care
of multi-arch support for us.

## Create builder with multi-arch support
Use the `buildx` command to create a specific builder that supports multi-arch
image builds

```shell
docker buildx create --name <name_your_builder> --use
```

**Some useful buildx commands:**
```shell
# List all available builders
docker buildx ls

# Switch to a specific builder
docker buildx use hservices

# List all docker contexts
docker context ls
```

## Building multi-arch image
Once you have created and selected your builder, you can use `docker buildx build`
to create your image.

For this example:
- We want to support `linux/amd64` and `linux/arm64` architectures
- We have a dockerfile named: `test.dockerimage`
- We'll tag our image as: `giobyte8/test:1.0.0`

```shell
# Build and push image to registry
docker buildx build                       \
      --platform linux/amd64,linux/arm64  \
      -t giobyte8/test:1.0.0              \
      -f scanner.dockerfile               \
      --push                              \
      ..
```

> You can remove the `--push` argument to prevent image from being uploaded
> to docker registry

## References

- [Docker blog: Build Multi-arch images with buildx](https://www.docker.com/blog/how-to-rapidly-build-multi-architecture-images-with-buildx/)
- [Docker docs: Multi-platform images](https://docs.docker.com/build/building/multi-platform/)
