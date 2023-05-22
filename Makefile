CHECKSUM = $(shell cat Dockerfile pip-requirements.txt | sha256sum | cut -d' ' -f1)

CI_IMG = gcr.io/singlestore-public/jira-automation:${CHECKSUM}

.PHONY: build-ci-image
build-ci-image:
	docker build -t "${CI_IMG}" .

.PHONY: push-ci-image
push-ci-image: build-ci-image
	docker push ${CI_IMG}

.PHONY: shell
shell: build-ci-image
	docker run -ti -v ${PWD}:${PWD} -w ${PWD} --entrypoint=bash ${CI_IMG}
