from django.shortcuts import render

from registry.models import Repository, Image
from registry.rest import RegistryClient

client = RegistryClient.RestClient("http://localhost:5000")


def index(request):
    repositories = client.list_repositories()

    context = {
        'repositories': repositories
    }
    return render(request, 'registry/index.html', context)


def repository(request, name):
    raw_repo = client.get_repository(name)

    repo = Repository()
    repo.name = raw_repo.get("name")
    repo.settags(raw_repo.get("tags"))

    return render(request, 'registry/repository.html', {'repository': repo})


def image(request, name, tag):
    rsp = client.get_manifest(name, tag)
    raw_image = rsp.content()
    img = Image()
    img.name = raw_image.get("name")
    img.tag = raw_image.get("tag")
    img.digest = rsp.headers()["Docker-Content-Digest"]

    return render(request, 'registry/image.html', {'image': img})
